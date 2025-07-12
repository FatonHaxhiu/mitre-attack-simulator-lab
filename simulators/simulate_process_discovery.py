import os


def simulate_process_discovery():
    os.makedirs("logs", exist_ok=True)
    procs = os.popen("ps aux").read()
    with open("logs/process_discovery.log", "w") as f:
        f.write("Simulated process discovery (T1057).\n")
        f.write(procs)


if __name__ == "__main__":
    simulate_process_discovery()
