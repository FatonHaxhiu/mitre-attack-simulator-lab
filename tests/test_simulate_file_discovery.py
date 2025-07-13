import os
import simulators.simulate_file_discovery as sfd


def test_simulate_file_discovery_creates_log(tmp_path, monkeypatch):
    # Patch the log directory to a temp path
    monkeypatch.chdir(tmp_path)
    sfd.simulate_file_discovery()
    log_path = tmp_path / "logs" / "file_discovery.log"
    assert log_path.exists()
    content = log_path.read_text()
    assert "Simulated file and directory discovery" in content
