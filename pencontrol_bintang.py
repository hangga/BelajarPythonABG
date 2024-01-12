import turtle

# Membuat objek Turtle
pen = turtle.Turtle()

# Mengatur kecepatan pen (1 = sangat lambat, 10 = sangat cepat)
pen.speed(1)

# Menggambar sebuah bintang dengan 5 segi
for _ in range(5):
    pen.forward(100)  # Panjang sisi
    pen.right(144)    # Sudut dalam bintang

# Mengisi warna pada bintang
pen.fillcolor("yellow")
pen.begin_fill()

for _ in range(5):
    pen.forward(100)
    pen.right(144)

pen.end_fill()

# Tutup window saat di-klik
turtle.exitonclick()
