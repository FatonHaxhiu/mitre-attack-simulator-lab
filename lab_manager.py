import os


def run_simulator(script):
    os.system(f"python3 simulators/{script}")


def run_detector(script):
    os.system(f"python3 detectors/{script}")


def view_results_log():
    log_path = "results_log.csv"
    if not os.path.isfile(log_path):
        print("No results log found yet.")
        return
    print("\n--- Simulation & Detection Results ---\n")
    with open(log_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())
    print("\n--- End of Results ---\n")


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
        print("11. Simulate PowerShell Execution (T1059.001)")
        print("12. Detect PowerShell Execution")
        print("13. Exit")
        print("14. View Results Log")
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
            run_simulator("simulate_powershell.py")
        elif choice == "12":
            run_detector("detect_powershell.py")
        elif choice == "13":
            print("Exiting.")
            break
        elif choice == "14":
            view_results_log()
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main_menu()
