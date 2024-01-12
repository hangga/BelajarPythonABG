import turtle

# Membuat objek Turtle
pen = turtle.Turtle()

# Mengatur kecepatan pen (0 = secepat mungkin)
pen.speed(1)

# Menggambar garis lurus(awal ke arah x)
pen.forward(100)

# Putar pen sejauh 90 derajat (belok kanan/ bawah)
pen.right(90)

# Menggambar garis lagi
pen.forward(100)

# Tutup window saat di-klik
turtle.exitonclick()
