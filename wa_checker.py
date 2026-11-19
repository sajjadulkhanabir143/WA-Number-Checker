import os
import sys
import time
import json
import threading
import requests

# Color Palette
C_CYAN = "\033[96m"
C_BLUE = "\033[94m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"
C_YELLOW = "\033[93m"
C_MAGENTA = "\033[95m"
C_WHITE = "\033[97m"
C_DIM = "\033[2m"
C_BOLD = "\033[1m"
C_RESET = "\033[0m"

BANNER = rf"""{C_CYAN}{C_BOLD}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ███████╗ █████╗      ██╗     ██╗ █████╗ ██████╗        ║
║   ██╔════╝██╔══██╗     ██║     ██║██╔══██╗██╔══██╗       ║
║   ███████╗███████║     ██║     ██║███████║██║  ██║       ║
║   ╚════██║██╔══██║██   ██║██   ██║██╔══██║██║  ██║       ║
║   ███████║██║  ██║╚█████╔╝╚█████╔╝██║  ██║██████╔╝       ║
║   ╚══════╝╚═╝  ╚═╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝        ║
║                                                          ║
║          {C_WHITE}SAJJADUL KHAN ABIR  •  WA CHECKER v2.0{C_CYAN}          ║
╠══════════════════════════════════════════════════════════╣
║  {C_YELLOW}GitHub :{C_WHITE} github.com/sajjadulkhanabir143{C_CYAN}                 ║
║  {C_YELLOW}Mode   :{C_WHITE} Termux Interactive WhatsApp Lookup{C_CYAN}             ║
╚══════════════════════════════════════════════════════════╝{C_RESET}
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_box(title, lines, color=C_GREEN):
    width = 56
    print(f"\n{color}┌{'─' * width}┐")
    print(f"│ {C_BOLD}{title:<{width - 1}}{C_RESET}{color}│")
    print(f"├{'─' * width}┤")
    for line in lines:
        print(f"│ {C_WHITE}{line:<{width - 1}}{color}│")
    print(f"└{'─' * width}┘{C_RESET}")

def check_whatsapp(phone_number, nonce="456a28b7e0"):
    url = "https://www.idtexpress.com/wp-admin/admin-ajax.php"

    payload = {
        "action": "idt_whatsapp_checker",
        "nonce": nonce,
        "phone_number": phone_number
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "origin": "https://www.idtexpress.com",
        "referer": "https://www.idtexpress.com/whatsapp-checker/",
        "accept-language": "en-US,en;q=0.9"
    }

    stop_spinner = False

    def spinner_task():
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        while not stop_spinner:
            sys.stdout.write(f"\r{C_MAGENTA}[{frames[i % len(frames)]}] Querying server for {phone_number}...{C_RESET}")
            sys.stdout.flush()
            i += 1
            time.sleep(0.08)
        sys.stdout.write("\r" + " " * 65 + "\r")
        sys.stdout.flush()

    t = threading.Thread(target=spinner_task)
    t.start()

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        raw_text = response.text.strip()

        if raw_text in ("0", "-1"):
            return False, "Session Nonce Expired", ["Site nonce expired (0/-1).", "Update 'nonce' value inside wa_checker.py."]

        data = response.json()
        formatted_lines = [f"Target Number : {phone_number}"]
        if isinstance(data, dict):
            for k, v in data.items():
                val_str = json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v)
                formatted_lines.append(f"{k.capitalize():<13} : {val_str[:38]}")
        else:
            formatted_lines.append(f"Result        : {str(data)[:38]}")

        return True, "LOOKUP RESULT", formatted_lines

    except ValueError:
        return False, "INVALID RESPONSE", [f"HTTP Status: {response.status_code}", "Server did not return valid JSON."]
    except requests.RequestException as e:
        return False, "NETWORK ERROR", [str(e)[:52]]
    finally:
        stop_spinner = True
        t.join()

def main():
    clear_screen()
    print(BANNER)
    print(f"{C_DIM}Tip: Include country code (e.g., +88017XXXXXXXX). Type 'exit' to quit.{C_RESET}")

    try:
        while True:
            phone = input(f"\n{C_CYAN}┌──({C_YELLOW}WA-CHECK{C_CYAN})─[{C_WHITE}Phone Number{C_CYAN}]\n└─▶ {C_RESET}").strip()

            if phone.lower() in ("exit", "quit", "q"):
                print(f"\n{C_YELLOW}[*] Session terminated. Goodbye!{C_RESET}")
                break

            if not phone:
                print(f"{C_RED}[!] Please enter a valid phone number.{C_RESET}")
                continue

            success, title, lines = check_whatsapp(phone)
            print_box(title, lines, color=C_GREEN if success else C_RED)

    except KeyboardInterrupt:
        print(f"\n\n{C_YELLOW}[*] Interrupted by user. Exiting...{C_RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
