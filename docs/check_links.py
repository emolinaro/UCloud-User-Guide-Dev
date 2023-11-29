import os
import concurrent.futures
import requests
import logging
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from tqdm import tqdm

def setup_logging():
    """
    Sets up logging for the script.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("link_checker.log"), logging.StreamHandler()])

def get_all_links_from_file(html_file):
    """
    Extracts all links from a given HTML file.
    
    :param html_file: Path to the HTML file
    :return: Dictionary of links with their respective source files
    """
    links = {}
    try: 
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            for element in soup.find_all(['a', 'link'], href=True):
                link = element['href']
                absolute_link = urljoin(html_file, link)
                links[absolute_link] = html_file

            for element in soup.find_all(['img', 'script'], src=True):
                link = element['src']
                absolute_link = urljoin(html_file, link)
                links[absolute_link] = html_file

    except Exception as e:
        logging.error(f"Error reading file {html_file}: {e}")
    return links

def resolve_relative_path(source_file, link, base_dir):
    """
    Resolves relative paths for a link based on the source file and base directory.
    
    :param source_file: The source HTML file containing the link
    :param link: The link to be resolved
    :param base_dir: The base directory of the source files
    :return: Resolved path of the link
    """
    if not link.startswith(('http://', 'https://')):
        # Check if the link already contains the base directory
        if not link.startswith(base_dir):
            # Relative path
            relative_source_file = os.path.relpath(source_file, start=base_dir)
            relative_dir = os.path.dirname(relative_source_file)
            resolved_path = os.path.normpath(os.path.join(base_dir, relative_dir, link))
        else:
            # The link already contains the base directory
            resolved_path = os.path.normpath(link)

        logging.debug(f"Resolving: Source File: {source_file}, Link: {link}, Resolved Path: {resolved_path}")

        return resolved_path
    else:
        return link  # External link

def check_anchor(file, anchor):
    """
    Checks if an anchor exists in a given HTML file.
    
    :param file: Path to the HTML file
    :param anchor: The anchor ID to check
    :return: Boolean indicating if the anchor exists
    """
    anchor_exists = False
    try:
        with open(file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            anchor_exists = soup.find(id=anchor) is not None
    except Exception as e:
        logging.error(f"Error checking anchor in file {file}: {e}")
    return anchor_exists

def check_local_reference(source_file, link, base_dir):
    """
    Checks if a local link is valid and if an anchor in the link exists.
    
    :param source_file: The source HTML file containing the link
    :param link: The link to be checked
    :param base_dir: The base directory of the source files
    :return: Boolean indicating if the link and anchor are valid
    """
    resolved_path, _, anchor = resolve_relative_path(source_file, link, base_dir).partition('#')

    # Check if the file exists (for local paths)
    if not resolved_path.startswith(('http://', 'https://')) and not os.path.exists(resolved_path):
        logging.warning(f"Broken local reference: {link} in {source_file}")
        return False

    # Check if the anchor exists in the file
    if anchor and not check_anchor(resolved_path, anchor):
        logging.warning(f"Broken anchor in local reference: {link} in {source_file}")
        return False

    return True

def check_links(links, exception_links, progress_bar, base_dir):
    """
    Checks all provided links for validity, including local references and anchors.
    
    :param links: Dictionary of links to check
    :param exception_links: Links to be ignored
    :param progress_bar: tqdm progress bar instance
    :param base_dir: The base directory of the source files
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    timeout_duration = 20  # seconds

    for link in links:
        try:
            file = links[link]
            exception_found = any(link == exception or exception in link for exception in exception_links)

            if not exception_found and link.startswith(('http://', 'https://')):
                response = requests.get(link, headers=headers, allow_redirects=True, timeout=timeout_duration)

                if response.status_code == 403:
                    logging.info(f"Forbidden link: {link} in {file}")
                elif response.status_code != 200:
                    logging.warning(f"Possible issue with link: {link} in {file} (Status code: {response.status_code})")
            elif not exception_found:
                if not check_local_reference(file, link, base_dir):
                    logging.warning(f"Broken link or anchor: {link} in {file}")

            time.sleep(0.1)

        except requests.exceptions.Timeout:
            logging.warning(f"Timeout occurred for link: {link} in {file}")
        except requests.exceptions.SSLError as e:
            logging.error(f"SSL error for link {link} in {file}: {e}")
        except requests.exceptions.TooManyRedirects:
            logging.warning(f"Too many redirects for link: {link} in {file}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking link {link} in {file}: {e}")
        except Exception as e:
            logging.error(f"Unhandled exception for link {link} in {file}: {e}")
        finally:
            progress_bar.update(1)

def get_exceptions(file_path):
    """
    Retrieves a list of links that should be ignored from a file.
    
    :param file_path: Path to the file containing exception links
    :return: List of exception links
    """
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logging.error(f"The ignored links file {file_path} was not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return links

def get_html_files(directory):
    """
    Retrieves all HTML files from a given directory.
    
    :param directory: The directory to scan for HTML files
    :return: List of HTML file paths
    """
    html_files = []
    if not os.path.exists(directory):
        logging.error(f"{directory} does not exist.")
        return html_files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def parse_arguments():
    """
    Parses command line arguments for the script.
    
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Link Checker for HTML files")
    parser.add_argument('--directory', type=str, default='_build/html', help='Directory to scan for HTML files')
    parser.add_argument('--exceptions', type=str, default='ignored_links.txt', help='File with links to ignore')
    parser.add_argument('--threads', type=int, default=os.cpu_count(), help='Number of threads to use')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    setup_logging()

    base_dir = os.path.normpath(args.directory)
    html_files = get_html_files(base_dir)
    exception_links = get_exceptions(args.exceptions)

    all_links = {}
    for file in html_files:
        all_links.update(get_all_links_from_file(file))

    total_links = len(all_links)
    logging.info(f"Total number of links to check: {total_links}")

    num_threads = args.threads
    keys = list(all_links.keys())
    chunk_size = max(1, len(keys) // num_threads) 
    chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)]

    http_session = requests.Session()

    with tqdm(total=total_links, unit="link", desc="Checking Links") as progress_bar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(check_links, {key: all_links[key] for key in chunk}, exception_links, progress_bar, base_dir) for chunk in chunks]
            concurrent.futures.wait(futures)

    logging.info("Link checking completed.")

