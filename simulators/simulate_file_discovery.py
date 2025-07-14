import os


def simulate_file_discovery():
    os.makedirs("logs", exist_ok=True)
    files = os.popen("ls -l /tmp").read()
    with open("logs/file_discovery.log", "w") as f:
        f.write("Simulated file and directory discovery (T1083).\n")
        f.write(files)


if __name__ == "__main__":
    simulate_file_discovery()
