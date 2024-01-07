import turtle
import random

# Atur layar
wn = turtle.Screen()
wn.title("Berburu Makanan dengan Turtle")
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

# Fungsi untuk bergerak ke kanan
def kanan():
    x = kura_kura.xcor()
    x += 20
    kura_kura.setx(x)

# Fungsi untuk bergerak ke kiri
def kiri():
    x = kura_kura.xcor()
    x -= 20
    kura_kura.setx(x)

# Fungsi untuk membuat makanan
def buat_makanan():
    makanan = turtle.Turtle()
    makanan.shape("circle")
    makanan.color("red")
    makanan.penup()
    makanan.speed(0)
    x = random.randint(150, 290)
    y = random.randint(-190, 190)
    makanan.goto(x, y)
    return makanan

# Inisialisasi makanan pertama
makanan = buat_makanan()

# Hubungkan fungsi dengan tombol panah dan spasi
wn.listen()
wn.onkeypress(naik, "Up")
wn.onkeypress(turun, "Down")
wn.onkeypress(kanan, "Right")
wn.onkeypress(kiri, "Left")

# Loop utama permainan
while True:
    wn.update()

    # Pengecekan bertabrakan dengan makanan
    if kura_kura.xcor() + 20 > makanan.xcor() - 10 and kura_kura.xcor() - 20 < makanan.xcor() + 10:
        if kura_kura.ycor() + 20 > makanan.ycor() - 10 and kura_kura.ycor() - 20 < makanan.ycor() + 10:
            makanan.hideturtle()
            makanan = buat_makanan()

# Penutupan layar jika permainan selesai
wn.bye()
