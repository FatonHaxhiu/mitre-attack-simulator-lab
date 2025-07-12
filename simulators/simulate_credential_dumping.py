import os


def simulate_credential_dumping():
    os.makedirs("logs", exist_ok=True)
    # Simulate credential dumping by listing user accounts
    users = os.popen("cat /etc/passwd").read()
    with open("logs/credential_dumping.log", "w") as f:
        f.write("Simulated credential dumping technique (T1003) executed.\n")
        f.write("User accounts found:\n")
        f.write(users)


if __name__ == "__main__":
    simulate_credential_dumping()
