import detectors.parse_file_discovery_logs as pfd


def test_detect_file_discovery_detects(capfd, tmp_path, monkeypatch):
    logs_dir = tmp_path / "logs"
    logs_dir.mkdir()
    log_file = logs_dir / "file_discovery.log"
    log_file.write_text("Simulated file and directory discovery (T1083).\n")
    monkeypatch.chdir(tmp_path)
    pfd.detect_file_discovery()
    out, _ = capfd.readouterr()
    assert "File and Directory Discovery detected (T1083)" in out
