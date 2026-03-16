"""Update GoDaddy DNS records for osindo.us to point at Netlify."""
from __future__ import annotations

import json
from typing import Any, List

from connect_godaddy import DOMAIN, GoDaddyClient, GoDaddySDKError  # type: ignore

NETLIFY_APEX_IPS = ["75.2.60.5", "99.83.190.102"]
NETLIFY_CNAME = "osindo-mechanical-services.netlify.app"
TTL = 600


def pretty(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True)


def put_records(client: GoDaddyClient, record_type: str, name: str, data: List[dict[str, Any]]) -> None:
    client._request(  # pylint: disable=protected-access
        "PUT",
        f"/domains/{DOMAIN}/records/{record_type}/{name}",
        payload=data,
    )


def main() -> None:
    client = GoDaddyClient()
    print(f"Updating DNS for {DOMAIN} -> Netlify")

    a_payload = [{"data": ip, "ttl": TTL} for ip in NETLIFY_APEX_IPS]

    put_records(client, "A", "@", a_payload)
    print("A records updated:")
    print(pretty(a_payload))

    cname_payload = [{"data": NETLIFY_CNAME, "ttl": TTL}]
    put_records(client, "CNAME", "www", cname_payload)
    print("CNAME record updated:")
    print(pretty(cname_payload))

    print("✅ GoDaddy DNS now points to Netlify. Allow time for propagation.")


if __name__ == "__main__":
    try:
        main()
    except GoDaddySDKError as exc:  # pragma: no cover
        raise SystemExit(f"GoDaddy API error: {exc}")
