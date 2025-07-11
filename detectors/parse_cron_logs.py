def parse_cron_logs(log_path):
    try:
        with open(log_path, 'r') as f:
            for line in f:
                if "cron job" in line.lower() or "ATTACK_T1053.003" in line:
                    print("Potential persistence via cron job detected! (T1053.003)")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    parse_cron_logs('logs/cron_persistence.log')