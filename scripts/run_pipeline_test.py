"""Quick test script to create a channel and run a pipeline against local backend

Usage:
    python scripts/run_pipeline_test.py --base http://127.0.0.1:8000
"""
import time
import argparse
import requests


def create_channel(base_url, name="TestChannel"):
    url = f"{base_url}/api/v1/channels"
    payload = {"name": name, "platform": "youtube", "mode": "curated"}
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()


def run_pipeline(base_url, channel_id, keyword="cats"):
    url = f"{base_url}/api/v1/pipeline/run"
    payload = {"channel_id": channel_id, "mode": "curated", "content_keyword": keyword}
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()


def get_pipeline(base_url, pipeline_id):
    url = f"{base_url}/api/v1/pipeline/{pipeline_id}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="http://127.0.0.1:8000", help="Base URL for backend")
    args = parser.parse_args()

    base = args.base.rstrip("/")
    print("Creating channel...")
    ch = create_channel(base)
    print("Channel created:", ch.get("id"))

    print("Running pipeline...")
    p = run_pipeline(base, ch.get("id"), keyword="funny cats")
    pipeline_id = p.get("id")
    print("Pipeline started:", pipeline_id)

    # Poll until finished
    for _ in range(30):
        time.sleep(1)
        status = get_pipeline(base, pipeline_id)
        print("Status:", status.get("status"))
        if status.get("status") != "running":
            print("Final pipeline data:")
            print(status)
            break


if __name__ == "__main__":
    main()
