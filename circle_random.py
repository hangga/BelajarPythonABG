import turtle
import random

# Membuat objek Turtle
pen = turtle.Turtle()

# Mengatur kecepatan pen (0 = secepat mungkin)
pen.speed(0)

# Fungsi untuk menggambar pola lingkaran dengan warna acak
def draw_circle_pattern(size, num_circles):
    for _ in range(num_circles):
        pen.color(random.random(), random.random(), random.random())  # Warna acak
        pen.circle(size)
        pen.left(360 / num_circles)

# Menggambar beberapa pola lingkaran dengan ukuran dan jumlah lingkaran yang berbeda
draw_circle_pattern(50, 10)
draw_circle_pattern(80, 6)
draw_circle_pattern(120, 4)

# Tutup window saat di-klik
turtle.exitonclick()
