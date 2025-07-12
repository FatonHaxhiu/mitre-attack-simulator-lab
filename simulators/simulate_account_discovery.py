import os

def simulate_account_discovery():
    os.makedirs("logs", exist_ok=True)
    users = os.popen('cat /etc/passwd').read()
    with open('logs/account_discovery.log', 'w') as f:
        f.write("Simulated account discovery technique (T1087.001) executed.\n")
        f.write("User accounts:\n")
        f.write(users)

if __name__ == "__main__":
    simulate_account_discovery()