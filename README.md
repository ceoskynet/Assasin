# Assasin

# Assassin - Account Hunting Tool

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Ethical Use](https://img.shields.io/badge/Purpose-Ethical%20Use%20Only-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

**Assassin** is a Python-based **account hunting tool** designed for **ethical purposes only**. It helps identify active accounts on a target website by testing credentials (email, username, and password). Assassin supports custom wordlists or dynamically generates test credentials in real-time if no wordlist is provided.

This tool is strictly for **legal use**, such as identifying and reporting sensitive data exposures responsibly to website administrators.

---

## Features

- **Dynamic Target Website Input**:
  - Prompt to input the **target website's login endpoint** (e.g., `https://example.com/login`).
  
- **Custom Wordlist Support**:
  - Accepts a wordlist file with credentials (`email,username,password`) for testing.
  - Automatically loads and processes the wordlist for testing.

- **Dynamic Credential Generation**:
  - If no wordlist is provided, the tool generates test credentials in real-time.

- **Active Account Detection**:
  - Identifies accounts with valid credentials by analyzing server responses.

- **Anti-Bot Measures**:
  - Random delays between credential tests to reduce the risk of detection by anti-bot systems.

- **Ethical Use Header**:
  - Displays a visually appealing ANSI-styled header with a clear disclaimer: **"For Ethical Purposes Only"**.

---

## Usage

### Prerequisites

1. **Python 3.6+** installed on your system.
2. Install the required Python library:
   ```bash
   pip install requests

```git clone https://github.com/yourusername/assassin-tool.git
```cd assassin-tool
```python assassin.py


