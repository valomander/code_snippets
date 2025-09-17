import time
import sys

def spinner_animation():
    spinner = ['|', '/', '-', '\\']
    for _ in range(50):
        for char in spinner:
            sys.stdout.write(f'\rLoading {char}')
            sys.stdout.flush()
            time.sleep(0.1)

spinner_animation()
