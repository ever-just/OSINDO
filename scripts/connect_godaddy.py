"""Utility script to verify GoDaddy connectivity for osindo.us.

This script expects the shared GoDaddy SDK checkout to live at
~/Documents/GoDaddySDK (per workspace convention). Ensure the following
environment variables are set before running it:

    export GODADDY_API_KEY="..."
    export GODADDY_API_SECRET="..."
    export GODADDY_API_ENV="production"  # or ote

Usage:
    python scripts/connect_godaddy.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

SDK_PATH = Path.home() / "Documents" / "GoDaddySDK"
if not SDK_PATH.exists():
    raise SystemExit(
        "Expected GoDaddy SDK at ~/Documents/GoDaddySDK. "
        "Clone or download it, then try again."
    )

if str(SDK_PATH) not in sys.path:
    sys.path.insert(0, str(SDK_PATH))

try:
    from godaddy_sdk import GoDaddyClient, GoDaddySDKError
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "GoDaddy SDK dependencies missing. Activate ~/Documents/GoDaddySDK/.venv "
        "and run 'pip install -r requirements.txt'."
    ) from exc

DOMAIN = os.environ.get("OSINDO_DOMAIN", "osindo.us")


def pretty(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def main() -> None:
    print(f"Connecting to GoDaddy for domain: {DOMAIN}")
    client = GoDaddyClient()

    try:
        domain_info = client.get_domain(DOMAIN)
    except GoDaddySDKError as err:
        raise SystemExit(f"Failed to fetch domain details: {err}")

    print("\nDomain details:")
    print(pretty(domain_info))

    print("\nCurrent A record (@):")
    try:
        records = client.list_records(DOMAIN, record_type="A", name="@")
    except GoDaddySDKError as err:
        raise SystemExit(f"Failed to fetch DNS records: {err}")

    print(pretty(records))
    print("\n✅ GoDaddy SDK connection confirmed.")


if __name__ == "__main__":
    main()
