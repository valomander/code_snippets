import turtle
import turtle_renderer as tr

# Bildschirm + Turtle initialisieren
screen = tr.setup_screen()
t = tr.setup_turtle()

# Text zeichnen
text = tr.normalize_text("Hallo Welt!")
text1 = tr.normalize_text("hi")
tr.draw_text(t, text, size=2, font_type=1)
tr.draw_text(t, text1, size=2, font_type=1)

# Fenster offen halten
turtle.done()
