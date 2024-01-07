import turtle
import time
import random

# Atur layar
wn = turtle.Screen()
wn.title("Tangkap Bola dengan Turtle")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Tambahkan paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Tambahkan bola
bola = turtle.Turtle()
bola.shape("circle")
bola.color("red")
bola.penup()
bola.speed(0)
bola.goto(random.randint(-290, 290), 290)

# Fungsi untuk bergerak ke kiri
def go_left():
    x = paddle.xcor()
    if x > -280:
        paddle.setx(x - 20)

# Fungsi untuk bergerak ke kanan
def go_right():
    x = paddle.xcor()
    if x < 280:
        paddle.setx(x + 20)

# Hubungkan fungsi dengan tombol panah kiri dan kanan
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Atur pergerakan bola
bola.dx = 2
bola.dy = -2

# Loop utama permainan
while True:
    wn.update()

    # Gerakkan bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Batasi bola agar tidak keluar dari layar
    if bola.xcor() > 290 or bola.xcor() < -290:
        bola.dx *= -1

    if bola.ycor() > 290:
        bola.goto(random.randint(-290, 290), 290)
        bola.dy *= -1

    # Pengecekan bertabrakan dengan paddle
    if (bola.ycor() < -240 and bola.ycor() > -250) and (bola.xcor() > paddle.xcor() - 50 and bola.xcor() < paddle.xcor() + 50):
        bola.sety(-240)
        bola.dy *= -1

    # Pengecekan akhir permainan
    if bola.ycor() < -290:
        time.sleep(1)
        bola.goto(random.randint(-290, 290), 290)
        bola.dy *= -1

# Penutupan layar jika permainan selesai
wn.bye()
