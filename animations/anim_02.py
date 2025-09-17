import time

# Ladebalken Animation
for i in range(21):
    bar = "█" * i + "░" * (20 - i)
    print(f"\rProgress: [{bar}] {i*5}%", end="", flush=True)
    time.sleep(0.1)
print()  # Neue Zeile am Ende
