# DARKSTAR v2.1 CLI

**Ultimate Command‑Line Hacking Toolkit**  
*Professional Penetration Testing Framework – Highly Customizable · Lightweight · Fast*

DARKSTAR is a comprehensive CLI toolkit for security professionals, offering **57 production‑ready modules** across 7 categories. Each tool runs as a standalone plugin, allowing easy addition or removal without touching the core engine. The framework features an interactive dynamic menu, automatic plugin discovery, and a clean, matrix‑inspired colour scheme.

---

## 🔥 Features

- **57 specialized tools** organized by category  
- **Plug‑and‑play plugin system** – just drop a `.py` file into the correct folder  
- **Colour‑coded terminal UI** with a Matrix‑style palette  
- **Automatic plugin discovery** – no hard‑coded menus  
- **Lightweight & fast** – runs on Kali Linux, Termux, Windows (WSL), and macOS  
- **Multi‑wordlist support** (local files + online URLs)  
- **Anti‑block mechanisms** – user‑agent rotation, proxy support, cooldown timers  
- **Threading & async** for high‑speed operations  
- **Works with Python 3.10+** and only standard pip‑installable dependencies  

---

## 📦 Menu Overview (Page 1)

| No. | Tool Name                    | Category          |
|-----|------------------------------|-------------------|
| 01  | Tool Info                    | Ops Support       |
| 02  | Layer7 DDOS                  | Exploitation      |
| 03  | Trojan Maker                 | Exploitation      |
| 04  | Bruteforce Instagram         | Exploitation      |
| 05  | SQL Injection Auto           | Exploitation      |
| 06  | Layer4 DDOS                  | Exploitation      |
| 07  | WordPress Bruteforce         | Exploitation      |
| 08  | Database Leaker              | Exploitation      |
| 09  | Script Deface Generator      | Exploitation      |
| 10  | Cpanel Bruteforce            | Exploitation      |
| 11  | Crack Wifi All Password      | Exploitation      |
| 12  | Bruteforce Facebook Premium  | Exploitation      |
| 13  | Database Leaker V2           | Exploitation      |
| 14  | Malware Generator            | Exploitation      |
| 15  | AutoExploit                  | Exploitation      |
| 16  | Bypass WAF                   | Exploitation      |
| 17  | EMP Attack                   | Exploitation      |
| 18  | SQL Vulnerability Scanner    | Vulnerability     |
| 19  | Cpanel Checker               | Vulnerability     |
| 20  | Wp Login Checker             | Vulnerability     |
| 21  | CMS Detector                 | Vulnerability     |
| 22  | Hash Cracker                 | Vulnerability     |
| 23  | Website Scanner Info         | Vulnerability     |
| 24  | XSS Scanner                  | Vulnerability     |
| 25  | Website Vulnerability Scanner| Vulnerability     |
| 26  | Http Header Info             | Vulnerability     |
| 27  | Wordpress Scanner            | Vulnerability     |
| 28  | CSRF Scanner                 | Vulnerability     |
| 29  | LFI Scanner                  | Vulnerability     |
| 30  | Subdomain Finder             | Reconnaissance    |
| 31  | Track IP                     | Reconnaissance    |
| 32  | Get IP Website               | Reconnaissance    |
| 33  | IP & Domain Port Scanner     | Reconnaissance    |
| 34  | Domain Grabber               | Reconnaissance    |
| 35  | Get Source Code Website      | Reconnaissance    |
| 36  | Admin Login Page Finder      | Reconnaissance    |
| 37  | Email Scraper                | Reconnaissance    |
| 38  | Cpanel Finder                | Reconnaissance    |
| 39  | Website Scraper              | Reconnaissance    |
| 40  | OSINT                        | OSINT             |

**→ Next page for more tools (41‑57 + Coming Soon)**

## 📦 Menu Overview (Page 2)

| No. | Tool Name                    | Category          |
|-----|------------------------------|-------------------|
| 41  | Database Finder              | OSINT             |
| 42  | CCTV Finder                  | OSINT             |
| 43  | Email Search                 | OSINT             |
| 44  | NIK Checker                  | OSINT             |
| 45  | Phone Number Info            | OSINT             |
| 46  | Lacak Foto                   | OSINT             |
| 47  | Cek Rekening                 | OSINT             |
| 48  | Da Pa Checker                | OSINT             |
| 49  | Instagram OSINT              | OSINT             |
| 50  | Webshell Finder              | Post‑Exploitation |
| 51  | Spam WhatsApp                | Social Engineering|
| 52  | Report Instagram             | Social Engineering|
| 53  | Spam Bot Telegram            | Social Engineering|
| 54  | Report Facebook              | Social Engineering|
| 55  | Python Obfuscation           | Ops Support       |
| 56  | Dir Buster                   | Ops Support       |
| 57  | YouTube Downloader           | Ops Support       |
| 58‑80 | *Coming Soon*               | –                 |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip
- Git (optional)

### Installation
```bash
git clone https://github.com/Mr-Pstar7/Preview-DarkStar.git
cd Preview-DarkStar
pip install -r config/requirements.txt
```

### Running DARKSTAR
```bash
python darkstar.py
```
On Linux/Termux, you may need to run with `python3` instead.  
For the best experience, use a terminal with true‑colour support (e.g., Windows Terminal, Tilix, Termux).

---

## 📁 Project Structure

```
DARKSTAR/
├── darkstar.py                 # CLI entry point
├── config/
│   ├── __init__.py
│   ├── settings.py             # Colour constants, meta info
│   └── requirements.txt        # Python dependencies
├── core/
│   ├── __init__.py
│   ├── engine.py               # Plugin manager & menu
│   └── utils.py                # Terminal helpers
├── plugins/
│   ├── __init__.py             # Auto‑discovery
│   ├── exploitation/           # 17 tools
│   ├── vulnerability/          # 12 tools
│   ├── recon/                  # 10 tools
│   ├── osint/                  # 10 tools
│   ├── post_exploit/           # 1 tool
│   ├── social_eng/             # 4 tools
│   └── ops_support/            # 3 tools
├── data/
│   ├── wordlists/
│   └── payloads/
├── modules/                    # External libs (pystyle, etc.)
└── output/                     # All tool outputs
    ├── reports/
    └── shells/
```

---

## ⚙️ Customization

- **Adding a new tool:** create a `.py` file inside the appropriate `plugins/<category>` folder and define the required attributes (`_name`, `_priority`, `_darkstar_plugin = True`, and a `run()` function). The engine will automatically add it to the menu.
- **Changing colours:** edit `config/settings.py`.
- **Managing dependencies:** add new packages to `config/requirements.txt`.

---

## ❗ Disclaimer

**DARKSTAR is intended for legal security assessments only.**  
Misuse of this tool may violate local, national, or international laws. The author assumes **no liability** for any damage caused by improper usage. Always obtain explicit written permission before testing any system.

---

## 📬 Contact

- **Author:** MrPstar7  
- **GitHub:** [https://github.com/Mr-Pstar7](https://github.com/Mr-Pstar7)  
- **Telegram:** [t.me/MrPstar7](https://t.me/MrPstar7)  
- **Instagram:** [pstar7.dev](https://instagram.com/pstar7.dev)

---

© 2025 MrPstar7. All rights reserved.
