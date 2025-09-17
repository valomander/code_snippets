import time
import os

frames = [
    """
    \o/
     |
    / \\
    """,
    """
     o
    /|\\
    / \\
    """,
    """
     o
     |\\
    / \\
    """
]

def animate_frames():
    for _ in range(10):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)

animate_frames()
