WinSec-Analyzer

A simple Python tool for analyzing Windows Security Event Logs (".evtx").

The project focuses on detecting failed login attempts and generating a basic security report.

Features

- Read Windows Security ".evtx" files.
- Detect failed login events (Event ID 4625).
- Count total failed login attempts.
- Count failed login attempts per username.
- Track failed login events without a username.
- Generate a text-based security report.
- Display warnings for users with 3 or more failed login attempts.

Requirements

- Python 3
- python-evtx
- lxml

Installation

Install the required packages:

pip install python-evtx lxml

Usage

1. Create a folder named "private_data".
2. Place your Windows Security log file inside it as "security.evtx".
3. Create a folder named "reports".
4. Run the program:

python winsec.py

The generated report will be saved to:

"reports/security_report.txt"

Security Notes

Windows Security logs may contain sensitive information. Do not upload real ".evtx" files or generated reports to public repositories.

The warnings are based on a simple failed-login threshold and do not necessarily indicate an attack.

Version

v0.1.0 — Initial version.

Author

Developed as a Python cybersecurity learning project.