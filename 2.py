# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 7 [Вперёд 12 Налево 120].
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.







import turtle
SCALE = 30
turtle.tracer(0)

turtle.left(90)
for i in range(7):
    turtle.forward(12 * SCALE)
    turtle.left(120)

turtle.penup()
for x in range(-10, 25):
    for y in range(-10, 20):
        turtle.setpos(x * SCALE, y * SCALE)
        turtle.dot(3, 'red')
turtle.done()