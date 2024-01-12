import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Mengatur kecepatan turtle
t.speed(2)

# Inisialisasi variabel
length = 10
angle = 90

# Menggambar pola spiral dengan perulangan while
while length < 200:
    t.forward(length)
    t.right(angle)
    length += 10

# Menutup jendela grafis setelah selesai
turtle.done()