import psutil
import sys
import os
from results_logger import log_result

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))


def detect():
    print("[*] Detecting PowerShell process...")
    found = False
    details = ""
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] and "powershell" in proc.info["name"].lower():
            print(f"[!] Potential PowerShell process detected: {proc.info['name']}")
            details = f"Detected process: {proc.info['name']}"
            found = True
    if found:
        log_result("T1059.001", "detect_powershell.py", "detection", "success", details)
    else:
        print("[+] No PowerShell process detected.")
        log_result(
            "T1059.001",
            "detect_powershell.py",
            "detection",
            "success",
            "No PowerShell process detected",
        )


if __name__ == "__main__":
    detect()
