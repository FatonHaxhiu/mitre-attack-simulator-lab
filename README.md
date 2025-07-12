# MITRE ATT&CK Technique Simulator & Detection Lab

This project simulates selected MITRE ATT&CK techniques inside Docker containers and detects them using basic log parsing.

---

## Features

- Simulate common MITRE ATT&CK techniques (Credential Dumping - T1003, Persistence via Cron - T1053.003, Account Discovery - T1087.001)
- Use Docker containers for safe, repeatable testing
- Realistic simulation: scripts now perform benign real-world actions (e.g., reading `/etc/passwd`, creating cron jobs)
- Interactive CLI menu for attack simulation and detection
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

5. **Run the interactive CLI menu:**

    ```bash
    python3 lab_manager.py
    ```

    Follow the prompts to simulate and detect different MITRE ATT&CK techniques.

---

## Project Structure

```
mitre-attack-simulator-lab/
│
├── docker-compose.yml
├── simulators/
│   ├── simulate_credential_dumping.py
│   ├── simulate_cron_persistence.py
│   └── simulate_account_discovery.py
├── detectors/
│   ├── parse_sysmon_logs.py
│   ├── parse_cron_logs.py
│   └── parse_account_discovery_logs.py
├── lab_manager.py
├── logs/
├── README.md
└── requirements.txt
```

---

## MITRE ATT&CK Techniques Covered

| Tactic        | Technique Name           | ID         | Simulated | Detected |
|---------------|-------------------------|------------|:---------:|:--------:|
| Credential    | Credential Dumping       | T1003      | ✅        | ✅       |
| Persistence   | Cron Job                 | T1053.003  | ✅        | ✅       |
| Discovery     | Account Discovery        | T1087.001  | ✅        | ✅       |

### Details

- **T1003: Credential Dumping**
    - Simulates user account enumeration as a benign stand-in for credential dumping (`cat /etc/passwd`).
    - Detection via log parsing for related entries.

- **T1053.003: Persistence via Cron**
    - Simulates creation of a cron job (writes to log and actually adds a benign cron job).
    - Detection via log parsing for cron job persistence evidence.

- **T1087.001: Account Discovery**
    - Simulates listing user accounts via `/etc/passwd`.
    - Detection by searching simulation logs for evidence of enumeration.

---

## Usage

1. **Run the CLI menu:**

    ```bash
    python3 lab_manager.py
    ```

2. **Select which technique to simulate or detect.**
3. **View logs in the `logs/` directory for details of simulated actions.**

---

## Contributing

Pull requests welcome! Please open an issue first to discuss major changes or new features.

---

## References

- [MITRE ATT&CK® Framework](https://attack.mitre.org/)
- [Docker Documentation](https://docs.docker.com/)