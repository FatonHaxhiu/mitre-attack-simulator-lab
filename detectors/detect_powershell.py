import psutil


def detect():
    print("[*] Detecting PowerShell process...")
    found = False
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] and "powershell" in proc.info["name"].lower():
            print(f"[!] Potential PowerShell process detected: {proc.info['name']}")
            found = True
    if not found:
        print("[+] No PowerShell process detected.")


if __name__ == "__main__":
    detect()
