<div align="center">

![Author](https://img.shields.io/badge/Author-chr3st5an-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python->=3.8-blue?style=for-the-badge&logo=python)
![Version](https://img.shields.io/badge/Version-1.0.0-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

# TokenVerifier

#### Verify discord user tokens easy and fast

[Repository](https://github.com/chr3st5an/token-verifier) ᛫ [Report Bug](https://github.com/chr3st5an/token-verifier/issues)

</div>

</br>

## Disclaimer

---

**THIS SCRIPT** was made for <u>**educational purposes**</u>. By using **THIS SCRIPT** you agree that you hold <u>**responsibility and accountability**</u> of any consequences caused by <u>**your actions**</u>.

</br>

## Features

---

This program allows you to easily check which discord user tokens are valid and which aren't. The main goal of this program is it, to do it fast and reliable while being relative resource lightweight. This is achieved by using an asynchronously programming style.

</br>

## Getting Started

---

### Prerequisites

In order to use this script, you will need Python 3.8 or later and pip. You can download Python from the [official website](https://python.org/downloads). Once installed, you should automatically have pip. You can verify this by running the following commands in a terminal or command prompt:

- python

```bash
python -V
```

- pip

```bash
python -m pip -V # or just 'pip -V'
```

You are ready to go if everything worked perfectly. Otherwise check out this [installation guide](https://realpython.com/installing-python/).

### Installation

1. Clone this repository

```bash
git clone https://github.com/chr3st5an/token-verifier.git
```

> If you do not have `git`, download this repository as ZIP archive by clicking on the green `code` button > `Download ZIP`. Unzip the folder.

2. Navigate into the just downloaded folder

```bash
cd token-verifier
```

3. Install dependencies

```bash
python -m pip install -r ./requirements.txt
```

</br>

## Usage

---

You can use this tool by simple running the `verifier.py` file:

```bash
python verifier.py
```

The program will now ask you for the file which contains the tokens. It's import to either enter an absolute or relative path to the file, e.g. `C:\Users\Example\tokens.txt` or `..\tokens.txt`. If the tokens aren't saved in a file yet, create a simple `txt` file and save them in there.

Once you enter path, the program will do it's magic and show you which tokens are valid and which aren't.

</br>

## License

---

This project is licensed under the `MIT` license. For more information check out the `LICENSE` file.
