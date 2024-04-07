import random
import turtle as t  # import python turtle library

winWidth = 800
winHeight = 600
score = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("Shooting Game")
window.bgcolor("green")
window.setup(width=winWidth, height=winHeight)
window.tracer(False)

# Creating the shooter
shooter = t.Turtle()
shooter.speed(0)
shooter.shape("square")
shooter.color("white")
shooter.shapesize(stretch_wid=1, stretch_len=1)
shooter.penup()
shooter.goto(0, (-winHeight / 2) + 20)

# Creating the bullet
bullet = t.Turtle()
bullet.speed(0)
bullet.shape("circle")
bullet.color("red")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.penup()
bullet.hideturtle()

# Creating the enemy
enemy = t.Turtle()
enemy.speed()
enemy.shape("square")
enemy.color("black")
enemy.shapesize(stretch_wid=1, stretch_len=1)
enemy.penup()
enemy.goto(0, (winHeight / 2) + 1)

isShot = False


def moveLeft():
    x = shooter.xcor()
    x = x - 90
    shooter.setx(x)


def moveRight():
    x = shooter.xcor()
    x = x + 90
    shooter.setx(x)


def shoot():
    global isShot
    isShot = True
    bullet.goto(shooter.xcor(), shooter.ycor())
    bullet.showturtle()


window.listen()
window.onkeypress(moveLeft, 'l')
window.onkeypress(moveRight, 'r')
window.onkeypress(shoot, 's')

i = 0
while True:

    if i == 3000:
        enemyY = enemy.ycor()
        enemyX = random.randint(-int(winWidth / 2), int(winWidth / 2))
        enemy.sety(enemyY - 9)
        enemy.setx(enemyX)
        i = 0

    if isShot:
        y = bullet.ycor()
        y = y + 0.5
        bullet.sety(y)
        if bullet.distance(enemy) < 20:
            bullet.hideturtle()
            enemy.goto(0, (winHeight / 2) + 10)
            isShot = False
            score += 1

    if enemy.ycor() <= -winHeight / 2:
        enemy.clear()
        shooter.clear()
        bullet.clear()
        t.write(f"Your score: {score}", align="center", font=('Courier', 32, 'bold'))

    i += 1
    window.update()
