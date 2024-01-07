import turtle
import random

# Atur layar
wn = turtle.Screen()
wn.title("Loncat-Loncatan dengan Turtle")
wn.bgcolor("white")
wn.setup(width=600, height=400)

# Tambahkan kura-kura
kura_kura = turtle.Turtle()
kura_kura.shape("turtle")
kura_kura.color("green")
kura_kura.penup()
kura_kura.speed(0)
kura_kura.goto(-250, -190)

# Fungsi untuk melompat
def loncat():
    y = kura_kura.ycor()
    y += 20
    kura_kura.sety(y)

# Tambahkan rintangan
rintangan = turtle.Turtle()
rintangan.shape("square")
rintangan.color("red")
rintangan.shapesize(stretch_wid=1, stretch_len=2)
rintangan.penup()
rintangan.speed(0)
rintangan.goto(300, -180)

# Loop utama permainan
while True:
    wn.update()

    # Gerakkan rintangan ke kiri
    rintangan.setx(rintangan.xcor() - 5)

    # Pengecekan bertabrakan dengan rintangan
    if kura_kura.xcor() + 20 > rintangan.xcor() - 20 and kura_kura.xcor() - 20 < rintangan.xcor() + 20:
        if kura_kura.ycor() + 20 > rintangan.ycor() - 10 and kura_kura.ycor() - 20 < rintangan.ycor() + 10:
            rintangan.goto(300, -180)
            kura_kura.goto(-250, -190)

    # Pengecekan jika kura-kura jatuh
    if kura_kura.ycor() < -190:
        kura_kura.goto(-250, -190)

# Hubungkan fungsi dengan tombol spasi
wn.listen()
wn.onkeypress(loncat, "space")
