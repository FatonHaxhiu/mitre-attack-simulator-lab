# MITRE ATT&CK Technique Simulator & Detection Lab

This project simulates selected MITRE ATT&CK techniques inside Docker containers and detects them using basic log parsing.

---

## Features

- Simulate common MITRE ATT&CK techniques (e.g., Credential Dumping - T1003)
- Use Docker containers for safe, repeatable testing
- Basic log-based detection of attack techniques
- Cross-platform: Run on Windows 11 with WSL & Docker

---

## Getting Started

### Prerequisites

- Windows 11
- [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Python 3.x

### Setup

1. **Clone the repo:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/mitre-attack-simulator-lab.git
    cd mitre-attack-simulator-lab
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Start Docker containers:**

    ```bash
    docker-compose up -d
    ```

4. **Simulate an attack:**

    ```bash
    python simulators/simulate_credential_dumping.py
    ```

5. **Detect the attack:**

    ```bash
    python detectors/parse_sysmon_logs.py
    ```

---

## Project Structure

```
mitre-attack-simulator-lab/
│
├── docker-compose.yml
├── simulators/
│   └── simulate_credential_dumping.py
├── detectors/
│   └── parse_sysmon_logs.py
├── logs/
├── README.md
└── requirements.txt
```

---

## MITRE ATT&CK Techniques Covered

- T1003: Credential Dumping (demo)

---

## Contributing

Pull requests welcome!