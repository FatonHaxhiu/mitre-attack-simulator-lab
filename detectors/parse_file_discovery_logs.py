def detect_file_discovery():
    try:
        with open('logs/file_discovery.log', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "Simulated file and directory discovery" in line:
                    print("File and Directory Discovery detected (T1083)")
                    return
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    detect_file_discovery()