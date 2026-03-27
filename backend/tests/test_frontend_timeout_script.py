from __future__ import annotations

import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "frontend-timeout.sh"


def run_script(mode: str, **env_overrides: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(env_overrides)
    return subprocess.run(
        ["bash", str(SCRIPT_PATH), mode],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )


def test_default_dev_timeout() -> None:
    result = run_script("dev")
    assert result.returncode == 0
    assert result.stdout.strip() == "120"


def test_default_prod_timeout() -> None:
    result = run_script("prod")
    assert result.returncode == 0
    assert result.stdout.strip() == "600"


def test_global_timeout_override_applies_to_all_modes() -> None:
    result = run_script("prod", DEER_FLOW_FRONTEND_TIMEOUT="900")
    assert result.returncode == 0
    assert result.stdout.strip() == "900"


def test_mode_specific_override_is_used_when_global_override_is_missing() -> None:
    result = run_script("prod", DEER_FLOW_FRONTEND_TIMEOUT_PROD="480")
    assert result.returncode == 0
    assert result.stdout.strip() == "480"


def test_invalid_mode_returns_error() -> None:
    result = run_script("weird-mode")
    assert result.returncode != 0
    assert "Unknown frontend startup mode" in result.stderr
