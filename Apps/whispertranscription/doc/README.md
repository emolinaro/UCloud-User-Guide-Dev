# Whisper Transcription

[![](badges/release-1.1-blue.svg)](https://cloud.sdu.dk/app/jobs/create?app=whispertranscription&version=1.1)
![type](badges/type-batch-yellow.svg)
![access](badges/access-open-green.svg)

- **Operating System:** ![](./badges/Ubuntu-22.10-lightseagreen.svg)
- **Terminal:** ![](./badges/tini-0.19.0-lightseagreen.svg) ![](./badges/tmux-3.3a-lightseagreen.svg)
- **Shell:** ![](./badges/bash-5.2.2-lightseagreen.svg) ![](./badges/fish-3.5.1-lightseagreen.svg) ![](./badges/zsh-5.9-lightseagreen.svg)
- **Editor:** ![](./badges/emacs-27.1-lightseagreen.svg) ![](./badges/nano-6.4-lightseagreen.svg) ![](./badges/vim-9.0-lightseagreen.svg)
- **Package Manager:** ![](./badges/apt-2.5.3-lightseagreen.svg) ![](./badges/conda-23.1.0-lightseagreen.svg) ![](./badges/dpkg-1.21.9-lightseagreen.svg) ![](./badges/npm-8.18.0-lightseagreen.svg) ![](./badges/pip-23.0.1-lightseagreen.svg)
- **Programming Language:** ![](./badges/GCC-12.2.0-lightseagreen.svg) ![](./badges/OpenJDK-11.0.19-lightseagreen.svg) ![](./badges/Python-3.10.10-lightseagreen.svg) ![](./badges/Python-2.7.18-lightseagreen.svg)
- **Utility:** ![](./badges/Lmod-8.7-lightseagreen.svg)
- **Extension:** ![](./badges/OpenMPI-4.1.4-lightseagreen.svg)

---

This utility is used to make a transcription of a voice or video recording, using the
[Whisper](https://openai.com/research/whisper) large language model from [OpenAI](http://openai.com/).

## Input format

The app can process `.mp3`, `.mp4`, `.m4a`, `.wav` and `.mpg` files.

## Output format

- CSV: \
  Contains every parameter outputted from the whisper model.

- DOTE: \
  [DOTE](https://www.dote.aau.dk/) Transcription software developed by the [BigSoftVideo](https://www.dote.aau.dk/about) team at AAU

- DOCX: \
  [Office Open XML Document](https://en.wikipedia.org/wiki/Office_Open_XML_file_formats) (Microsoft Word)

- JSON: \
  JavaScript Object Notation

- SRT: \
  [SubRip file format](https://en.wikipedia.org/wiki/.srt), widely adopted subtitle format

- TSV: \
  [Tab-separated value](https://en.wikipedia.org/wiki/Tab-separated_values) file contain start, end and text

- TXT: \
  Pure text file with the transcription

- VTT: \
  [Web Video Text Tracks](https://en.wikipedia.org/wiki/WebVTT) format

- ZIP: \
  Archive with all of the output files. If Archive Password is set, then the archive is encrypted with [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

## Output Folder

By default the transcript files are saved in `/Jobs/Whisper Transcription/<job-id>/out`. The user can select an other directory using the corresponding optional parameter.

## Interactive mode

The _Interactive mode_ parameter is used to start an interactive job session where the user can either select "Open terminal" or "Open interface". The latter gives access to a JupyterLab workspace to run notebooks.
