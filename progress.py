import os
import sys
import time
import subprocess
import signal

if len(sys.argv) != 4:
    print("Usage: python3 progress.py <file> <tag> <repo>")
    sys.exit(1)

FILE = sys.argv[1]
TAG_NAME = sys.argv[2]
REPO = sys.argv[3]

TOTAL_SIZE = os.path.getsize(FILE)
TOTAL_MB = TOTAL_SIZE / (1024 * 1024)
START_TIME = time.time()

try:
    net_device = os.popen("ip route | awk '/default/ {print $5}'").read().strip()
    net_path = f"/sys/class/net/{net_device}/statistics/tx_bytes"
    with open(net_path, "r") as f:
        INITIAL_BYTES = int(f.read().strip())
except:
    INITIAL_BYTES = 0

def format_eta(seconds):
    return f"{int(seconds // 60):02}:{int(seconds % 60):02}"

def signal_handler(sig, frame):
    sys.stdout.write("\nUpload canceled. Exiting.\n")
    proc.terminate()
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

proc = subprocess.Popen(["gh", "release", "upload", TAG_NAME, FILE, "--repo", REPO],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

bar_width = 25
last_update_time = 0

while proc.poll() is None:
    time.sleep(0.5)

    try:
        with open(net_path, "r") as f:
            current_bytes = int(f.read().strip())
    except:
        current_bytes = INITIAL_BYTES

    uploaded_mb = (current_bytes - INITIAL_BYTES) / (1024 * 1024)
    uploaded_mb = min(uploaded_mb, TOTAL_MB)  

    percent = int((uploaded_mb / TOTAL_MB) * 100)
    elapsed_time = time.time() - START_TIME
    speed_mbps = uploaded_mb / elapsed_time if elapsed_time > 0 else 0
    eta = format_eta((TOTAL_MB - uploaded_mb) / speed_mbps if speed_mbps > 0 else 0)

    if time.time() - last_update_time >= 0.5:
        bar = "#" * (percent * bar_width // 100) + "." * (bar_width - (percent * bar_width // 100))
        sys.stdout.write(f"\r[{bar}] {percent}% | {int(uploaded_mb)}MB / {int(TOTAL_MB)}MB | {int(speed_mbps)}MB/s | ETA: {eta}")
        sys.stdout.flush()
        last_update_time = time.time()

sys.stdout.write("\n")
