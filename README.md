# MITRE ATT&CK Technique Simulator & Detection Lab

This project simulates selected MITRE ATT&CK techniques inside Docker containers and detects them using basic log parsing.

---

## Features

- Simulate common MITRE ATT&CK techniques (e.g., Credential Dumping - T1003, Persistence via Cron - T1053.003)
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

3. **Create the logs directory (if it doesn't exist):**

    ```bash
    mkdir -p logs
    ```

4. **Start Docker containers:**

    ```bash
    docker-compose up -d
    ```

5. **Simulate an attack:**

    - Credential Dumping (T1003):

        ```bash
        python3 simulators/simulate_credential_dumping.py
        ```

    - Persistence via Cron (T1053.003):

        ```bash
        python3 simulators/simulate_cron_persistence.py
        ```

6. **Detect the attack:**

    - Credential Dumping:

        ```bash
        python3 detectors/parse_sysmon_logs.py
        ```

    - Persistence via Cron:

        ```bash
        python3 detectors/parse_cron_logs.py
        ```

---

## Project Structure

```
mitre-attack-simulator-lab/
│
├── docker-compose.yml
├── simulators/
│   ├── simulate_credential_dumping.py
│   └── simulate_cron_persistence.py
├── detectors/
│   ├── parse_sysmon_logs.py
│   └── parse_cron_logs.py
├── logs/
├── README.md
└── requirements.txt
```

---

## MITRE ATT&CK Techniques Covered

- **T1003: Credential Dumping**
    - Simulates creation of logs indicating credential dumping activity.
    - Detection via log parsing for related keywords.

- **T1053.003: Persistence via Cron**
    - Simulates creation of a malicious cron job.
    - Detection via log parsing for evidence of cron job persistence.

---

## Contributing

Pull requests welcome! Please open an issue first to discuss major changes or new features.

---

## References

- [MITRE ATT&CK® Framework](https://attack.mitre.org/)
- [Docker Documentation](https://docs.docker.com/)