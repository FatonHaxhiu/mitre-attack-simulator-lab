import os

def simulate_cron_persistence():
    os.makedirs("logs", exist_ok=True)
    cron_job = "* * * * * /usr/bin/evil_script.sh # ATTACK_T1053.003\n"
    with open('logs/cron_persistence.log', 'w') as f:
        f.write("Simulating adding the following cron job:\n")
        f.write(cron_job)

if __name__ == "__main__":
    simulate_cron_persistence()