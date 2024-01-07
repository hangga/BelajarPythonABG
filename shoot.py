import turtle
import random
import math

# Atur layar
wn = turtle.Screen()
wn.title("Menembak Balon dengan Turtle")
wn.bgcolor("white")
wn.setup(width=600, height=400)

# Tambahkan kura-kura
kura_kura = turtle.Turtle()
kura_kura.shape("turtle")
kura_kura.color("green")
kura_kura.penup()
kura_kura.speed(0)
kura_kura.goto(-250, 0)

# Fungsi untuk bergerak ke atas
def naik():
    y = kura_kura.ycor()
    y += 20
    kura_kura.sety(y)

# Fungsi untuk bergerak ke bawah
def turun():
    y = kura_kura.ycor()
    y -= 20
    kura_kura.sety(y)

# Fungsi untuk menembak
def tembak():
    peluru = turtle.Turtle()
    peluru.shape("triangle")
    peluru.color("black")
    peluru.shapesize(stretch_wid=0.5, stretch_len=1)
    peluru.penup()
    peluru.speed(1)
    peluru.goto(kura_kura.xcor(), kura_kura.ycor())

    # Hitung arah tembakan menggunakan trigonometri
    angle = math.atan2(0, 300)  # Arah tembakannya, misalnya ke kanan
    peluru.setheading(math.degrees(angle))
    peluru.showturtle()

    while peluru.xcor() < 300:
        peluru.forward(10)

        # Pengecekan bertabrakan dengan balon
        for balon in balons:
            if (
                peluru.xcor() + 10 > balon.xcor() - 20
                and peluru.xcor() - 10 < balon.xcor() + 20
                and peluru.ycor() + 10 > balon.ycor() - 20
                and peluru.ycor() - 10 < balon.ycor() + 20
            ):
                balon.hideturtle()
                peluru.hideturtle()
                balons.remove(balon)

# Fungsi untuk membuat balon
def buat_balons():
    balon = turtle.Turtle()
    balon.shape("circle")
    balon.color("red")
    balon.penup()
    balon.speed(0)
    x = random.randint(150, 290)
    y = random.randint(-190, 190)
    balon.goto(x, y)
    return balon

# Inisialisasi list balon
balons = [buat_balons() for _ in range(5)]

# Hubungkan fungsi dengan tombol panah dan spasi
wn.listen()
wn.onkeypress(naik, "Up")
wn.onkeypress(turun, "Down")
wn.onkeypress(tembak, "space")

# Loop utama permainan
while True:
    wn.update()
