import subprocess

def print_menu():
    print("\nMITRE ATT&CK Lab Menu")
    print("1. Simulate Credential Dumping (T1003)")
    print("2. Detect Credential Dumping")
    print("3. Simulate Persistence via Cron (T1053.003)")
    print("4. Detect Persistence via Cron")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Select an action: ")
        if choice == "1":
            subprocess.run(["python3", "simulators/simulate_credential_dumping.py"])
        elif choice == "2":
            subprocess.run(["python3", "detectors/parse_sysmon_logs.py"])
        elif choice == "3":
            subprocess.run(["python3", "simulators/simulate_cron_persistence.py"])
        elif choice == "4":
            subprocess.run(["python3", "detectors/parse_cron_logs.py"])
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()