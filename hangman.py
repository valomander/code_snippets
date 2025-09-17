frames = [
    """
    +---+
    |   |
        |
        |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========
    """
]

variable = 0  
last_variable = -1  

while True:
    # Beispiel: Variable hochzählen
    variable += 1  

    if variable != last_variable:
        if 0 <= variable < len(frames):
            print(frames[variable])
        last_variable = variable

    if variable >= len(frames):
        break
