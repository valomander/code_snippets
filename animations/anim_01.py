import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Einfache Animation eines wandernden Punkts
for i in range(20):
    clear_screen()
    print(" " * i + "●")
    time.sleep(0.1)
