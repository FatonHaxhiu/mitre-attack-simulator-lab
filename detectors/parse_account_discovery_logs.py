def parse_account_discovery_logs(log_path):
    try:
        with open(log_path, "r") as f:
            content = f.read()
            if "account discovery" in content.lower() and "/etc/passwd" in content:
                print("Potential account discovery detected! (T1087.001)")
            elif "account discovery" in content.lower():
                print("Account discovery detected (T1087.001)")
            else:
                print("No account discovery detected.")
    except FileNotFoundError:
        print("Log file not found.")


if __name__ == "__main__":
    parse_account_discovery_logs("logs/account_discovery.log")
