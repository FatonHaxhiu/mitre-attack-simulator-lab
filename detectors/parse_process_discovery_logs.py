def detect_process_discovery():
    try:
        with open("logs/process_discovery.log", "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Simulated process discovery" in line:
                    print("Process Discovery detected (T1057)")
                    return
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    detect_process_discovery()
