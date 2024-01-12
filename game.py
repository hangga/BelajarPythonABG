import turtle
import random

# Membuat objek turtle untuk pemain
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=4)
player.penup()
player.speed(0)
player.goto(0, -250)

# Membuat objek turtle untuk bola
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(1)
ball.goto(random.randint(-200, 200), 250)

# Fungsi untuk menggerakkan pemain ke kiri
def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

# Fungsi untuk menggerakkan pemain ke kanan
def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# Mengatur keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Main game loop
while True:
    # Menggerakkan bola ke bawah
    y = ball.ycor()
    y -= 10
    ball.sety(y)

    # Memeriksa apakah bola ditangkap oleh pemain
    if player.distance(ball) < 30:
        ball.goto(random.randint(-200, 200), 250)
        print("Bola Ditangkap!")

    # Memeriksa apakah bola mencapai bagian bawah layar
    if ball.ycor() < -300:
        ball.goto(random.randint(-200, 200), 250)

    # Memperbarui tampilan grafis
    turtle.update()
