import sys
import os

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
O = '\033[38;5;208m'
P = '\033[38;5;129m'
N = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

MENU = [
    (1, "Tool Info",                     "ops_support/tool_info.py"),
    (2, "Layer7 DDOS",                   "exploitation/layer7_ddos.py"),
    (3, "Trojan Maker",                  "exploitation/trojan_maker.py"),
    (4, "Bruteforce Instagram",          "exploitation/bruteforce_instagram.py"),
    (5, "SQL Injection Auto",            "exploitation/sqli_auto.py"),
    (6, "Layer4 DDOS",                   "exploitation/layer4_ddos.py"),
    (7, "WordPress Bruteforce",          "exploitation/wp_bruteforce.py"),
    (8, "Database Leaker",               "exploitation/database_leaker.py"),
    (9, "Script Deface Generator",       "exploitation/deface_generator.py"),
    (10,"Cpanel Bruteforce",             "exploitation/cpanel_bruteforce.py"),
    (11,"Crack Wifi All Password",       "exploitation/wifi_crack.py"),
    (12,"Bruteforce Facebook Premium",   "exploitation/fb_bruteforce.py"),
    (13,"Database Leaker V2",            "exploitation/database_leaker_v2.py"),
    (14,"Malware Generator",             "exploitation/malware_generator.py"),
    (15,"AutoExploit",                   "exploitation/auto_exploit.py"),
    (16,"Bypass WAF",                    "exploitation/bypass_waf.py"),
    (17,"EMP Attack",                    "exploitation/emp_attack.py"),
    (18,"SQL Vulnerability Scanner",     "vulnerability/sql_vuln_scanner.py"),
    (19,"Cpanel Checker",                "vulnerability/cpanel_checker.py"),
    (20,"Wp Login Checker",              "vulnerability/wp_login_checker.py"),
    (21,"CMS Detector",                  "vulnerability/cms_detector.py"),
    (22,"Hash Cracker",                  "vulnerability/hash_cracker.py"),
    (23,"Website Scanner Info",          "vulnerability/website_info_scanner.py"),
    (24,"XSS Scanner",                   "vulnerability/xss_scanner.py"),
    (25,"Website Vulnerability Scanner", "vulnerability/website_vuln_scanner.py"),
    (26,"Http Header Info",              "vulnerability/http_header_info.py"),
    (27,"Wordpress Scanner",             "vulnerability/wordpress_scanner.py"),
    (28,"CSRF Scanner",                  "vulnerability/csrf_scanner.py"),
    (29,"LFI Scanner",                   "vulnerability/lfi_scanner.py"),
    (30,"Subdomain Finder",              "recon/subdomain_finder.py"),
    (31,"Track IP",                      "recon/ip_tracker.py"),
    (32,"Get IP Website",                "recon/get_ip_website.py"),
    (33,"IP & Domain Port Scanner",      "recon/port_scanner.py"),
    (34,"Domain Grabber",                "recon/domain_grabber.py"),
    (35,"Get Source Code Website",       "recon/get_source_code.py"),
    (36,"Admin Login Page Finder",       "recon/admin_finder.py"),
    (37,"Email Scraper",                 "recon/email_scraper.py"),
    (38,"Cpanel Finder",                 "recon/cpanel_finder.py"),
    (39,"Website Scraper",               "recon/website_scraper.py"),
    (40,"OSINT",                         "osint/osint.py"),
    (41,"Database Finder",               "osint/database_finder.py"),
    (42,"CCTV Finder",                   "osint/cctv_finder.py"),
    (43,"Email Search",                  "osint/email_search.py"),
    (44,"NIK Checker",                   "osint/nik_checker.py"),
    (45,"Phone Number Info",             "osint/phone_info.py"),
    (46,"Lacak Foto",                    "osint/lacak_foto.py"),
    (47,"Cek Rekening",                  "osint/cek_rekening.py"),
    (48,"Da Pa Checker",                 "osint/da_pa_checker.py"),
    (49,"Instagram OSINT",               "osint/instagram_osint.py"),
    (50,"Webshell Finder",               "post_exploit/webshell_finder.py"),
    (51,"Spam WhatsApp",                 "social_eng/spam_whatsapp.py"),
    (52,"Report Instagram",              "social_eng/report_instagram.py"),
    (53,"Spam Bot Telegram",             "social_eng/spam_telegram.py"),
    (54,"Report Facebook",               "social_eng/report_facebook.py"),
    (55,"Python Obfuscation",            "ops_support/python_obfuscation.py"),
    (56,"Dir Buster",                    "ops_support/dir_buster.py"),
    (57,"YouTube Downloader",            "ops_support/youtube_downloader.py"),
]

ITEMS_PER_PAGE = 40
TOTAL_ITEMS = len(MENU)

def draw_page(page_num):
    start = (page_num - 1) * ITEMS_PER_PAGE
    end = min(start + ITEMS_PER_PAGE, TOTAL_ITEMS)
    page_items = MENU[start:end]

    print(f"{BOLD}{C}╔══════════════════════════════════════════════════════════════════════════════╗{N}")
    print(f"{BOLD}{C}║                        DARKSTAR v2.1 CLI — Menu Preview                      ║{N}")
    print(f"{BOLD}{C}╚══════════════════════════════════════════════════════════════════════════════╝{N}")
    print(f"{BOLD}{O}  PAGE {page_num}  ({start+1}–{end}){N}\n")

    half = len(page_items) // 2 + len(page_items) % 2
    for i in range(half):
        left_id, left_name, left_path = page_items[i]
        left_str = f"  {M}[{P}{left_id:02d}{M}] {B}{left_name:<30}{O}"
        right_idx = i + half
        if right_idx < len(page_items):
            right_id, right_name, right_path = page_items[right_idx]
            right_str = f"  {M}[{P}{right_id:02d}{M}] {B}{right_name:<30}{O}"
            print(f"{left_str}║{right_str}")
        else:
            print(left_str)
    print()

    remaining = ITEMS_PER_PAGE - len(page_items)
    if remaining > 0:
        for j in range(remaining):
            empty_id = start + len(page_items) + j + 1
            print(f"  {M}[{P}{empty_id:02d}{M}] {R}{'Coming Soon':<30}{O}")
    print()
    print(f"{BOLD}{C}────────────────────────────────────────────────────────────────────────────────{N}")
    print(f"{BOLD}{O}  Total Tools: {P}{TOTAL_ITEMS}{O} | Slots: 1-80 | Remaining: Coming Soon{N}")
    print(f"{BOLD}{C}────────────────────────────────────────────────────────────────────────────────{N}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    draw_page(1)
    if TOTAL_ITEMS > ITEMS_PER_PAGE:
        draw_page(2)
