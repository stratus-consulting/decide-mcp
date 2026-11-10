"""Stratus DECIDE example client. Stratus Consulting Group, MIT License.

Submit discovery findings to DECIDE over REST and print the open risks.

Usage:
    export DECIDE_API_KEY=...        # issued by Stratus
    python validate.py request.json

Standard library only.
"""
import json
import os
import sys
import urllib.error
import urllib.request

URL = "https://stratus-decide.onrender.com/v1/discovery/validate"


def main(path: str) -> None:
    key = os.environ.get("DECIDE_API_KEY")
    if not key:
        sys.exit("Set DECIDE_API_KEY first.")

    with open(path, "rb") as f:
        body = f.read()

    req = urllib.request.Request(
        URL,
        data=body,
        headers={"X-API-Key": key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.load(resp)
    except urllib.error.HTTPError as e:
        retry = e.headers.get("Retry-After")
        sys.exit(f"HTTP {e.code}: {e.read().decode()}" + (f" (retry after {retry}s)" if retry else ""))

    print("Summary:", result["summary"])
    for risk in result["risks"]:
        print(f"\n- {risk['message']}\n  Next step: {risk['next_step']}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "request.json")
