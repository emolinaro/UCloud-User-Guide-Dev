from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import os
import concurrent.futures

class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_all_links_from_file(html_file):
    """
    Scans the file and retrieves all links from the html attributes: href, src
    They can be a url to a web page, a local resource, or an internal reference to an element in another html file.
    """
    links = {}
    try: 
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
            for element in soup.find_all(['a','link'], href=True):
                link = element['href']
                absolute_link = urljoin(html_file, link)
                links[absolute_link] = html_file

            for element in soup.find_all(['img', 'script'], src=True):
                link = element['src']
                absolute_link = urljoin(html_file, link)
                links[absolute_link] = html_file

    except Exception as e:
        print(f"{ConsoleColors.FAIL}An error occurred: {e} {ConsoleColors.ENDC}")
    return links

def check_anchor(file, anchor):
    """
    Returns true if the provided file has an element with the provided anchor (or id)
    """
    anchor_exists = False
    try:
        with open(file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            anchor_exists = soup.find(id=anchor) is not None
    except Exception as e:
        print(f"{ConsoleColors.FAIL}An error occurred: {e}{ConsoleColors.ENDC}")
    return anchor_exists

def check_links(links, exception_links):
    """
    Checks the provided links in search for broken urls and references to non existent resources.
    Links from exception_links are not checked.
    """
    for link in links:
        file  = links[link]
        exception_found = False

        for exception in exception_links:  
            if link == exception or exception in link: 
                exception_found = True
                break

        if not exception_found:       
            if link.startswith(('http://', 'https://')):
                try:
                    response = requests.head(link)
                    if response.status_code != 200:
                        if response.status_code == 403:
                            print(f"Forbidden link: {link} in {file}")
                        else:
                            print(f"Broken link: {link} in {file}")
                except requests.exceptions.RequestException as e:
                    print(f"{ConsoleColors.WARNING}Error checking response status of link {link} in {file}: {e}{ConsoleColors.ENDC}")
            else:
                path, sep, anchor = link.partition('#')
                if not os.path.exists(path):
                    print(f"Broken local reference: {link} in {file}. {file} does not exist.")
                else:
                    if anchor != '' and not check_anchor(path, anchor):
                        print(f"Broken anchor in local reference: {link} in {file}. {link} does not exist.")                    

def get_exceptions(file_path):
    """
    Loads a list of links that must not be checked from ignored_links.txt
    They can be full URLs or base URLs (e.g https://cloud.sdu.dk/login or https://cloud.sdu.dk).
    If a base url is used, it will not check any path that uses that base url.
    """
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    links.append(stripped_line)
    except FileNotFoundError:
        print(f"{ConsoleColors.FAIL}The ignored links file {file_path} was not found.{ConsoleColors.ENDC}")
    except Exception as e:
        print(f"{ConsoleColors.FAIL}An error occurred: {e}{ConsoleColors.ENDC}")
    return links

def get_html_files(directory):
    """
    Searches for all html files in the provided directory and returns a list of paths.
    """
    html_files = []
    if not os.path.exists(directory):
        print(f"{ConsoleColors.FAIL}{directory} does not exist. {ConsoleColors.ENDC}")
        return html_files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files
     
if __name__ == "__main__":
    
    # Get all html files from _build folder
    html_files = get_html_files("_build/html")

    #Get all links that shouldn't be checked
    exception_links = get_exceptions("ignored_links.txt")

    all_links = {}
    # Get all links from the html files
    for file in html_files:
        all_links.update(get_all_links_from_file(file))
    
    # For parallel execution
    num_threads = os.cpu_count()
    keys = list(all_links.keys())
    chunk_size = len(keys) // num_threads # makes the division and rounds down to the nearest int
    chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)] # divides the keys into chunks of keys

    print(f"{ConsoleColors.HEADER}Total nº of links to check: {len(all_links.keys())}, using {num_threads} threads{ConsoleColors.ENDC}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use submit to schedule the tasks for each chunk
        futures = [executor.submit(check_links, {key: all_links[key] for key in chunk}, exception_links) for chunk in chunks]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    # For non parallel execution use this line 
    # check_links(all_links, exception_links)
