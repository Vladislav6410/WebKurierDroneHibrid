import time
from failover import check_lte

MODE = "LTE"

def loop():
    global MODE

    while True:
        if check_lte():
            MODE = "LTE"
        else:
            MODE = "LORA"

        print("[COMMS MODE]", MODE)
        time.sleep(2)

if __name__ == "__main__":
    loop()