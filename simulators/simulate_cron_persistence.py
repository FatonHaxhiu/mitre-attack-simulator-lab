import os


def simulate_cron_persistence():
    os.makedirs("logs", exist_ok=True)
    cron_job = (
        "* * * * * /usr/bin/echo 'Hello from ATT&CK T1053.003' # ATTACK_T1053.003\n"
    )
    with open("logs/cron_persistence.log", "w") as f:
        f.write("Simulating adding the following cron job:\n")
        f.write(cron_job)
    # Actually (safely) add the cron job for the current user
    os.system(f'(crontab -l; echo "{cron_job.strip()}") | sort | uniq | crontab -')


if __name__ == "__main__":
    simulate_cron_persistence()
