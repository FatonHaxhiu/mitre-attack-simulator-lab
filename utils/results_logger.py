import csv
import os
from datetime import datetime

RESULTS_LOG = "results_log.csv"


def log_result(technique, script, action, result, details):
    file_exists = os.path.isfile(RESULTS_LOG)
    with open(RESULTS_LOG, mode="a", newline="") as csvfile:
        fieldnames = ["timestamp", "technique", "script", "action", "result", "details"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "technique": technique,
                "script": script,
                "action": action,
                "result": result,
                "details": details,
            }
        )
