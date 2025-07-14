# Contributing to MITRE ATT&CK Simulator Lab

Thank you for considering contributing!

## How to Add a New Technique

1. **Simulation Script**
   - Name your file `simulate_<technique>.py` (e.g., `simulate_powershell.py`).
   - Simulate the technique in a safe, contained manner.
2. **Detection Script**
   - Name your file `detect_<technique>.py` (e.g., `detect_powershell.py`).
   - Implement detection logic for the technique.
3. **Register scripts**
   - Add your new scripts to the CLI/menu.
4. **Testing**
   - Validate your scripts locally before submitting a PR.

## Submitting Changes

- Fork this repository and create your branch.
- Open a Pull Request with a clear description.
- Please follow coding style and provide meaningful commit messages.

## Need Help?

- Open an Issue for questions or discussion.