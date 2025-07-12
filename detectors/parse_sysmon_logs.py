def parse_sysmon_logs(log_path):
    # Dummy function to parse logs
    try:
        with open(log_path, "r") as f:
            for line in f:
                if "credential dumping" in line.lower():
                    print("Potential credential dumping detected!")
    except FileNotFoundError:
        print("Log file not found.")


if __name__ == "__main__":
    parse_sysmon_logs("logs/credential_dumping.log")
