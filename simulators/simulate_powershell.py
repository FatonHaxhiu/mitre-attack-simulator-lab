import subprocess
import shutil
import sys
import os
from results_logger import log_result

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))


def simulate():
    print("[*] Simulating PowerShell command execution...")
    powershell = shutil.which("powershell") or shutil.which("pwsh")
    if not powershell:
        print("[!] PowerShell not found on this system. Simulation cannot proceed.")
        log_result(
            "T1059.001",
            "simulate_powershell.py",
            "simulation",
            "failed",
            "PowerShell not found",
        )
        sys.exit(1)
    command = f"{powershell} -Command \"Write-Output 'Simulating PowerShell attack'\""
    try:
        subprocess.run(command, shell=True, check=True)
        print("[+] PowerShell simulation completed.")
        log_result(
            "T1059.001",
            "simulate_powershell.py",
            "simulation",
            "success",
            "PowerShell command executed",
        )
    except Exception as e:
        print(f"[!] Simulation failed: {e}")
        log_result(
            "T1059.001", "simulate_powershell.py", "simulation", "failed", str(e)
        )


if __name__ == "__main__":
    simulate()
