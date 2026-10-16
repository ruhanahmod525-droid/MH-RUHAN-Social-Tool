
import os
import subprocess
import shutil
import time

# MH RUHAN SOCIAL MEDIA TOOL

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

links = {
    "1": ("Facebook",
          "https://www.facebook.com/share/1CKMq1xpjK/"),
    "2": ("YouTube",
          "https://www.youtube.com/@RuhanAhmod-c8g"),
    "3": ("TikTok",
          "https://www.tiktok.com/@its_ruhan63"),
    "4": ("WhatsApp",
          "https://wa.me/itsruhan11?s=t")
}

def banner():
    os.system("clear")
    print(CYAN + BOLD)
    print("╔══════════════════════════════╗")
    print("║                              ║")
    print("║          MH RUHAN            ║")
    print("║      SOCIAL MEDIA TOOL       ║")
    print("║                              ║")
    print("╚══════════════════════════════╝")
    print(RESET)

def open_link(url):
    try:
        if shutil.which("termux-open-url"):
            subprocess.run(
                ["termux-open-url", url],
                check=True
            )
        else:
            print(RED + "termux-open-url not found!")
            print("Install/update Termux tools first.")
            print(RESET)
            return

        print(GREEN + "Opening link..." + RESET)
        time.sleep(1)

    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def main():
    while True:
        banner()

        print(YELLOW + "[1] Facebook")
        print("[2] YouTube")
        print("[3] TikTok")
        print("[4] WhatsApp")
        print("[0] Exit" + RESET)

        print("-" * 32)
        choice = input(CYAN + "Choose an option: " + RESET).strip()

        if choice == "0":
            print(GREEN + "Thanks for using MH RUHAN!")
            break

        elif choice in links:
            name, url = links[choice]
            print(GREEN + f"\nOpening {name}..." + RESET)
            open_link(url)
            input("\nPress Enter to return to menu...")

        else:
            print(RED + "\nInvalid option! Try again." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()
