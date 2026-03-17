import time
import requests

SERVER = "http://core.webkurier/api/ping"

def check_lte():
    try:
        r = requests.get(SERVER, timeout=2)
        return r.status_code == 200
    except:
        return False

def loop():
    while True:
        status = check_lte()
        print("[HEARTBEAT] LTE:", status)
        time.sleep(2)

if __name__ == "__main__":
    loop()