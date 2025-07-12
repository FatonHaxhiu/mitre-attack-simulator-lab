# MITRE ATT&CK Simulator Lab

A hands-on lab for simulating and detecting MITRE ATT&CK techniques on Linux systems.  
Easily run benign simulations of common attacker behaviors and test detection scripts in a safe, educational environment.

---

## Features

- Simulates multiple MITRE ATT&CK techniques on Linux (expandable)
- Detection scripts for each simulated technique
- Simple command-line interface (CLI) for selecting simulations/detections
- Modular and easy to extend with new techniques
- Continuous integration (CI) with linting and runtime checks

---

## Usage

1. **Clone the repository**
2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the lab manager:**  
   ```bash
   python3 lab_manager.py
   ```

---

## Available Techniques

| #  | Technique Name                  | ATT&CK ID   | Simulator Script                       | Detector Script                       |
|----|---------------------------------|-------------|----------------------------------------|---------------------------------------|
| 1  | Credential Dumping              | T1003       | simulate_credential_dumping.py         | parse_sysmon_logs.py                  |
| 2  | Persistence via Cron            | T1053.003   | simulate_cron_persistence.py           | parse_cron_logs.py                    |
| 3  | Account Discovery               | T1087.001   | simulate_account_discovery.py          | parse_account_discovery_logs.py        |
| 4  | File & Directory Discovery      | T1083       | simulate_file_discovery.py             | parse_file_discovery_logs.py          |
| 5  | Process Discovery               | T1057       | simulate_process_discovery.py          | parse_process_discovery_logs.py       |

> **Note:** All scripts are in the `simulators/` and `detectors/` folders.

---

## Menu Options

The CLI menu (`lab_manager.py`) lets you:
- Run a technique simulation (writes logs as if an attack occurred)
- Run the detection script for that technique (parses logs and reports detection)

---

## Project Structure

```
mitre-attack-simulator-lab/
│
├── simulators/
│   ├── simulate_credential_dumping.py
│   ├── simulate_cron_persistence.py
│   ├── simulate_account_discovery.py
│   ├── simulate_file_discovery.py
│   └── simulate_process_discovery.py
│
├── detectors/
│   ├── parse_sysmon_logs.py
│   ├── parse_cron_logs.py
│   ├── parse_account_discovery_logs.py
│   ├── parse_file_discovery_logs.py
│   └── parse_process_discovery_logs.py
│
├── lab_manager.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## How to Add a New Technique

1. Write a simulator script in `simulators/` (simulate the technique and log output)
2. Write a detection script in `detectors/` (detect the simulated activity)
3. Add menu options in `lab_manager.py` for your scripts
4. Update this README table

---

## Contributing

Pull requests are welcome!  
Please run CI checks and follow PEP8 formatting (auto-format with [black](https://github.com/psf/black) or [autopep8](https://github.com/hhatto/autopep8)).

---

## License

MIT License

---