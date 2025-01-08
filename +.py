import turtle
import math

# Konfigurasi turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

# Fungsi bentuk hati
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Membuat animasi tulisan "Iya" di atas hati
def draw_text(text, position, color, font_size):
    t.penup()
    t.goto(position)
    t.color(color)
    style = ("Arial", font_size, "bold")
    t.write(text, font=style, align="center")
    t.pendown()

# Gambar hati
t.penup()
t.goto(0, 0)
t.pendown()
for n in range(100):
    x, y = corazon(n * 0.1)
    t.goto(x * 10, y * 10)

# Tulis teks "Iyq"
draw_text("Iya", (0, -50), "white", 30)

# Sembunyikan penunjuk dan selesai
t.hideturtle()
turtle.done()