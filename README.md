# WA Number Checker (Termux CLI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge&logo=gnubash)
![Author](https://img.shields.io/badge/Author-Sajjadul%20Khan%20Abir-cyan?style=for-the-badge)

A clean, box-styled Termux command-line utility to check WhatsApp number availability directly from your Android terminal.

---

## Installation (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone [https://github.com/sajjadulkhanabir143/WA-Number-Checker.git](https://github.com/sajjadulkhanabir143/WA-Number-Checker.git)
cd WA-Number-Checker
pip install -r requirements.txt
python wa_checker.py
