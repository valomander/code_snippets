# -*- coding: utf-8 -*-
import turtle

# --- Font Dictionaries ---
# Font 0: 7-Segment Display Style
segments_7seg = {
    # Zahlen (0-9)
    "0": [(0,0),(20,0),(20,30),(0,30),(0,0),(0,15),(20,15)],  # 8 ohne Mitte
    "1": [(20,0),(20,30)],
    "2": [(0,30),(20,30),(20,15),(0,15),(0,0),(20,0)],
    "3": [(0,30),(20,30),(20,0),(0,0),(10,15),(20,15)],
    "4": [(0,30),(0,15),(20,15),(20,30),(20,0)],
    "5": [(20,30),(0,30),(0,15),(20,15),(20,0),(0,0)],
    "6": [(20,30),(0,30),(0,0),(20,0),(20,15),(0,15)],
    "7": [(0,30),(20,30),(20,0)],
    "8": [(0,0),(20,0),(20,30),(0,30),(0,0),(0,15),(20,15)],
    "9": [(0,15),(0,30),(20,30),(20,0),(0,0),(20,15)],
    
    # Buchstaben (7-Segment Style)
    "a": [(0,0),(0,15),(20,15),(20,30),(20,0),(0,15),(20,15)],
    "b": [(0,0),(0,30),(20,30),(20,15),(0,15),(20,15),(20,0),(0,0)],
    "c": [(20,0),(0,0),(0,30),(20,30)],
    "d": [(0,0),(0,30),(15,30),(20,25),(20,5),(15,0),(0,0)],
    "e": [(20,0),(0,0),(0,30),(20,30),(0,15),(15,15)],
    "f": [(0,0),(0,30),(20,30),(0,15),(15,15)],
    "g": [(20,30),(0,30),(0,0),(20,0),(20,15),(10,15)],
    "h": [(0,0),(0,30),(0,15),(20,15),(20,30),(20,0)],
    "i": [(20,0),(20,30)],
    "j": [(20,30),(20,0),(0,0),(0,10)],
    "k": [(0,0),(0,30),(0,15),(20,30),(0,15),(20,0)],
    "l": [(0,30),(0,0),(20,0)],
    "m": [(0,0),(0,30),(10,20),(20,30),(20,0)],
    "n": [(0,0),(0,30),(20,0),(20,30)],
    "o": [(0,0),(0,30),(20,30),(20,0),(0,0)],
    "p": [(0,0),(0,30),(20,30),(20,15),(0,15)],
    "q": [(20,0),(20,30),(0,30),(0,0),(20,0)],
    "r": [(0,0),(0,30),(20,30),(20,15),(0,15),(20,0)],
    "s": [(20,30),(0,30),(0,15),(20,15),(20,0),(0,0)],
    "t": [(0,30),(20,30),(10,30),(10,0)],
    "u": [(0,30),(0,0),(20,0),(20,30)],
    "v": [(0,30),(10,0),(20,30)],
    "w": [(0,30),(0,0),(10,10),(20,0),(20,30)],
    "x": [(0,0),(20,30),(10,15),(0,30),(20,0)],
    "y": [(0,30),(10,15),(20,30),(10,15),(10,0)],
    "z": [(0,30),(20,30),(0,0),(20,0)],
    
    # Sonderzeichen
    "-": [(0,15),(20,15)],
    "_": [(0,0),(20,0)],
    ":": [(10,8),(10,10),(10,20),(10,22)],
    ".": [(18,0),(20,0),(20,2),(18,2),(18,0)],
    "!": [(10,0),(10,5),(10,10),(10,30)],
    "?": [(0,20),(5,30),(15,30),(20,20),(10,15),(10,10),(10,0),(10,5)],
    "(": [(15,0),(5,10),(5,20),(15,30)],
    ")": [(5,0),(15,10),(15,20),(5,30)],
    "/": [(0,0),(20,30)],
    "\\": [(0,30),(20,0)],
    "+": [(10,5),(10,25),(0,15),(20,15)],
    "=": [(0,10),(20,10),(0,20),(20,20)],
    "*": [(10,5),(10,25),(5,10),(15,20),(15,10),(5,20)],
    " ": [],  # Leerzeichen
}

# Font 1: Standard Block Letters
segments_standard = {
    # Zahlen (0-9) - Standard Block Style
    "0": [(2,0),(18,0),(18,28),(2,28),(2,0),(15,25),(5,5)],
    "1": [(10,0),(10,28),(7,25)],
    "2": [(2,28),(18,28),(18,14),(2,14),(2,0),(18,0)],
    "3": [(2,28),(18,28),(18,14),(10,14),(18,14),(18,0),(2,0)],
    "4": [(2,28),(2,14),(18,14),(15,28),(15,0)],
    "5": [(18,28),(2,28),(2,14),(18,14),(18,0),(2,0)],
    "6": [(18,25),(15,28),(5,28),(2,25),(2,3),(5,0),(15,0),(18,3),(18,14),(2,14)],
    "7": [(2,28),(18,28),(10,0)],
    "8": [(2,14),(5,28),(15,28),(18,14),(15,0),(5,0),(2,14),(18,14)],
    "9": [(18,14),(2,14),(2,25),(5,28),(15,28),(18,25),(18,3),(15,0),(5,0),(2,3)],
    
    # Buchstaben a-z (Standard Block Style)
    "a": [(2,0),(2,20),(5,28),(15,28),(18,20),(18,0),(2,14),(18,14)],
    "b": [(2,0),(2,28),(15,28),(18,25),(18,17),(15,14),(2,14),(15,14),(18,11),(18,3),(15,0),(2,0)],
    "c": [(18,25),(15,28),(5,28),(2,25),(2,3),(5,0),(15,0),(18,3)],
    "d": [(2,0),(2,28),(12,28),(18,22),(18,6),(12,0),(2,0)],
    "e": [(18,0),(2,0),(2,28),(18,28),(2,14),(15,14)],
    "f": [(2,0),(2,28),(18,28),(2,14),(15,14)],
    "g": [(18,3),(15,0),(5,0),(2,3),(2,25),(5,28),(15,28),(18,25),(18,14),(10,14)],
    "h": [(2,0),(2,28),(2,14),(18,14),(18,28),(18,0)],
    "i": [(6,0),(14,0),(10,0),(10,28),(6,28),(14,28)],
    "j": [(18,28),(18,3),(15,0),(8,0),(5,3),(5,8)],
    "k": [(2,0),(2,28),(2,14),(18,28),(2,14),(18,0)],
    "l": [(2,28),(2,0),(18,0)],
    "m": [(2,0),(2,28),(8,18),(12,18),(18,28),(18,0)],
    "n": [(2,0),(2,28),(18,0),(18,28)],
    "o": [(5,0),(15,0),(18,3),(18,25),(15,28),(5,28),(2,25),(2,3),(5,0)],
    "p": [(2,0),(2,28),(18,28),(18,14),(2,14)],
    "q": [(5,0),(15,0),(18,3),(18,25),(15,28),(5,28),(2,25),(2,3),(5,0),(14,6),(20,0)],
    "r": [(2,0),(2,28),(18,28),(18,14),(2,14),(18,0)],
    "s": [(18,25),(15,28),(5,28),(2,25),(2,17),(5,14),(15,14),(18,11),(18,3),(15,0),(5,0),(2,3)],
    "t": [(2,28),(18,28),(10,28),(10,0)],
    "u": [(2,28),(2,3),(5,0),(15,0),(18,3),(18,28)],
    "v": [(2,28),(8,0),(12,0),(18,28)],
    "w": [(2,28),(5,0),(10,14),(15,0),(18,28)],
    "x": [(2,0),(18,28),(10,14),(2,28),(18,0)],
    "y": [(2,28),(10,14),(18,28),(10,14),(10,0)],
    "z": [(2,28),(18,28),(2,0),(18,0)],
    
    # Sonderzeichen
    "-": [(4,14),(16,14)],
    "_": [(2,0),(18,0)],
    ":": [(10,8),(10,10),(10,18),(10,20)],
    ".": [(8,0),(12,0),(12,4),(8,4),(8,0)],
    "!": [(10,0),(10,3),(10,8),(10,28)],
    "?": [(2,20),(5,28),(15,28),(18,20),(10,14),(10,8),(10,0),(10,3)],
    "(": [(14,0),(6,10),(6,18),(14,28)],
    ")": [(6,0),(14,10),(14,18),(6,28)],
    "/": [(2,0),(18,28)],
    "\\": [(2,28),(18,0)],
    "+": [(10,4),(10,24),(2,14),(18,14)],
    "=": [(4,10),(16,10),(4,18),(16,18)],
    "*": [(10,6),(10,22),(6,12),(14,16),(14,12),(6,16)],
    " ": [],  # Leerzeichen
}

def normalize_text(text):
    """Wandelt Umlaute in normale Buchstaben um und macht alles klein"""
    replacements = {
        # Deutsche Umlaute
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        'Ä': 'ae', 'Ö': 'oe', 'Ü': 'ue',
        # Andere Umlaute
        'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'å': 'a',
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
        'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i',
        'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o',
        'ù': 'u', 'ú': 'u', 'û': 'u',
        'ç': 'c', 'ñ': 'n',
        'À': 'a', 'Á': 'a', 'Â': 'a', 'Ã': 'a', 'Å': 'a',
        'È': 'e', 'É': 'e', 'Ê': 'e', 'Ë': 'e',
        'Ì': 'i', 'Í': 'i', 'Î': 'i', 'Ï': 'i',
        'Ò': 'o', 'Ó': 'o', 'Ô': 'o', 'Õ': 'o',
        'Ù': 'u', 'Ú': 'u', 'Û': 'u',
        'Ç': 'c', 'Ñ': 'n'
    }
    
    result = ""
    for char in text.lower():  # Erst alles kleinschreiben
        result += replacements.get(char, char)
    return result

def draw_segment_char(t, char, size=1, font_type=0):
    """Zeichnet einen Buchstaben im gewählten Font-Style"""
    # Wähle das richtige Font-Dictionary
    if font_type == 0:
        font_dict = segments_7seg
        char_width = 30
        line_thickness = 3
    else:  # font_type == 1
        font_dict = segments_standard
        char_width = 25
        line_thickness = 2
    
    if char not in font_dict:
        # Zeichne Fragezeichen für unbekannte Zeichen
        char = "?"
    
    if char == " ":  # Leerzeichen
        t.penup()
        t.forward(char_width*size)
        return
        
    coords = font_dict[char]
    if not coords:  # Leere Liste für Leerzeichen
        t.penup()
        t.forward(char_width*size)
        return
    
    t.penup()
    start_x, start_y = t.xcor(), t.ycor()
    
    # Setze Linienstärke je nach Font
    t.pensize(int(line_thickness*size))
    t.goto(start_x + coords[0][0]*size, start_y + coords[0][1]*size)
    t.pendown()
    
    for x, y in coords[1:]:
        t.goto(start_x + x*size, start_y + y*size)
    
    t.penup()
    t.goto(start_x + char_width*size, start_y)  # Abstand zum nächsten Zeichen

def draw_text(t, text, size=1, max_width=700, font_type=0):
    """Zeichnet ganzen Text im gewählten Font-Style"""
    start_x, start_y = t.xcor(), t.ycor()
    current_x = start_x
    line_height = 50 * size
    
    char_width = 30 if font_type == 0 else 25
    
    for char in text:
        # Prüfe Zeilenumbruch
        if current_x + char_width*size > start_x + max_width and char != " ":
            # Neue Zeile
            start_y -= line_height
            t.goto(start_x, start_y)
            current_x = start_x
        
        draw_segment_char(t, char, size, font_type)
        current_x = t.xcor()

def setup_screen():
    """Schwarzer Bildschirm für beide Font-Types"""
    screen = turtle.Screen()
    screen.title("Multi-Font Text Renderer")
    screen.bgcolor("black")
    screen.setup(width=1200, height=800)
    return screen

def setup_turtle():
    """Grüne Turtle für beide Font-Types"""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.color("#00ff00")  # Terminal-Grün
    t.pensize(2)
    return t

def main():
    """Hauptprogramm"""
    screen = setup_screen()
    t = setup_turtle()
    
    print("=== Multi-Font Text Renderer ===")
    print("📟 Font 0: 7-Segment LCD Style (wie Digitaluhren)")  
    print("🔤 Font 1: Standard Block Letters (normale Schrift)")
    print("✓ Alle Buchstaben werden kleingeschrieben")
    print("✓ Umlaute: ä→ae, ö→oe, ü→ue, ß→ss")
    print()
    print("Befehle:")
    print("  'exit' - Programm beenden")
    print("  'clear' - Bildschirm löschen")  
    print("  'font 0' - 7-Segment LCD Style")
    print("  'font 1' - Standard Block Letters")
    print("  'color [farbe]' - Farbe ändern (z.B. 'color red')")
    print("  'size [zahl]' - Größe ändern (z.B. 'size 2')")
    print("-" * 60)
    
    current_size = 1.5
    current_font = 0  # Standard: 7-Segment
    
    # Startposition
    t.goto(-500, 300)
    
    while True:
        try:
            user_input = input("Text eingeben: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == "exit":
                break
            elif user_input.lower() == "clear":
                t.clear()
                t.goto(-500, 300)
                print("Bildschirm gelöscht.")
                continue
            elif user_input.lower().startswith("font "):
                try:
                    font_num = int(user_input[5:].strip())
                    if font_num in [0, 1]:
                        current_font = font_num
                        font_name = "7-Segment LCD" if font_num == 0 else "Standard Block"
                        print(f"Font geändert zu: {font_num} ({font_name})")
                    else:
                        print("Nur Font 0 (7-Segment) oder Font 1 (Standard) verfügbar!")
                except:
                    print("Ungültige Font-Nummer!")
                continue
            elif user_input.lower().startswith("color "):
                try:
                    color = user_input[6:].strip()
                    t.color(color)
                    print(f"Farbe geändert zu: {color}")
                except:
                    print("Ungültige Farbe!")
                continue
            elif user_input.lower().startswith("size "):
                try:
                    new_size = float(user_input[5:].strip())
                    if 0.5 <= new_size <= 4:
                        current_size = new_size
                        print(f"Größe geändert zu: {current_size}")
                    else:
                        print("Größe muss zwischen 0.5 und 4 liegen!")
                except:
                    print("Ungültige Größe!")
                continue
            
            # Text normalisieren und anzeigen
            normalized = normalize_text(user_input)
            if normalized != user_input.lower():
                print(f"'{user_input}' → '{normalized}'")
            
            # Text zeichnen mit gewähltem Font
            draw_text(t, normalized, size=current_size, font_type=current_font)
            
            # Neue Zeile für nächsten Input
            current_y = t.ycor() - (60 * current_size)
            t.goto(-500, current_y)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Fehler: {e}")
    
    print("Text-Renderer beendet.")
    turtle.bye()

if __name__ == "__main__":
    main()
