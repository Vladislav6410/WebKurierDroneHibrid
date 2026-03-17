import subprocess
import time

def check_lte():
    result = subprocess.getoutput("bash ../lte/lte-check.sh")
    return "OK" in result

def switch_to_lora():
    print("[FAILOVER] Switching to LoRa")

def switch_to_lte():
    print("[FAILOVER] Using LTE")

def loop():
    while True:
        if check_lte():
            switch_to_lte()
        else:
            switch_to_lora()
        time.sleep(3)

if __name__ == "__main__":
    loop()