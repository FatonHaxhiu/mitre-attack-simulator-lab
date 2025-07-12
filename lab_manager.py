import os


def run_simulator(script):
    os.system(f"python3 simulators/{script}")


def run_detector(script):
    os.system(f"python3 detectors/{script}")


def main_menu():
    while True:
        print("\nMITRE ATT&CK Lab Menu")
        print("1. Simulate Credential Dumping (T1003)")
        print("2. Detect Credential Dumping")
        print("3. Simulate Persistence via Cron (T1053.003)")
        print("4. Detect Persistence via Cron")
        print("5. Simulate Account Discovery (T1087.001)")
        print("6. Detect Account Discovery")
        print("7. Simulate File and Directory Discovery (T1083)")
        print("8. Detect File and Directory Discovery")
        print("9. Simulate Process Discovery (T1057)")
        print("10. Detect Process Discovery")
        print("11. Exit")
        choice = input("Select an action: ")
        if choice == "1":
            run_simulator("simulate_credential_dumping.py")
        elif choice == "2":
            run_detector("parse_sysmon_logs.py")
        elif choice == "3":
            run_simulator("simulate_cron_persistence.py")
        elif choice == "4":
            run_detector("parse_cron_logs.py")
        elif choice == "5":
            run_simulator("simulate_account_discovery.py")
        elif choice == "6":
            run_detector("parse_account_discovery_logs.py")
        elif choice == "7":
            run_simulator("simulate_file_discovery.py")
        elif choice == "8":
            run_detector("parse_file_discovery_logs.py")
        elif choice == "9":
            run_simulator("simulate_process_discovery.py")
        elif choice == "10":
            run_detector("parse_process_discovery_logs.py")
        elif choice == "11":
            print("Exiting.")
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main_menu()
