# Simple Cannon shooting game with classes J Joubert October 2019
# Written in OSX - some values may need adjustment in windows
# Sound using os.system afplay for max OS
# use winsound for windows

# Still a work in progress

import turtle
import random
import os # To play wav file using afplay

win = turtle.Screen()
win.title('Simple cannon shooter')
win.bgcolor('black')
win.setup(800,600)
win.tracer(0)
win.listen()


cannon = turtle.Turtle()
cannon.shape('square')
cannon.shapesize(2,2)
cannon.up()
cannon.color('blue')
cannon.goto(-360, -260)


class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.shapesize(2,2)
        self.up()
        self.color('red')
        self.dx = -0.5
        self.goto(420, random.randint(0,250))


    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor())


class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.2, 0.7)
        self.up()
        self.color('yellow')
        self.lt(50)
        self.goto(-340, -240)
        self.state = 'ready'

    def shoot(self):
        self.state = 'fire'

    def move(self): 
        self.fd(10)

    def right(self):
        self.rt(10)

    def left(self):
        self.lt(10)
       
class Scoreboard(turtle.Pen):
    def __init__(self):
        super().__init__(shape='circle')
        self.hideturtle()
        self.up()
        self.color('red')
        self.goto(200,-200)
        self.write('Score: 0', align='center', font=('Courier', 24, 'normal'))


game_over = False  
enemy_list = []
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple']

bullet = Bullet()
pen = Scoreboard()
score = 0

win.onkey(bullet.shoot, 'space')
win.onkey(bullet.right, 'Right')
win.onkey(bullet.left, 'Left')

while not game_over:
    win.update()
    
    delay = random.random()
    # Create enemies
    if len(enemy_list) < 10 and delay < 0.02:
        enemy = Enemy()
        enemy.color(random.choice(colors))
        enemy_list.append(enemy)

    # Move enemies left
    for i in enemy_list:
        i.move()

        # Game over if enemy goes out on the left
        if i.xcor()<-400:
            game_over = True

        # If enemy is shot, reset bullet and remove enemy from list
        if i.distance(bullet)<30:
            os.system('afplay pop.wav&') # & is added to continue game while sound playing
            i.goto(1000,1000)
            enemy_list.remove(i)
            bullet.state = 'ready'
            bullet.goto(-340,-240)
            pen.clear()
            score += 1
            pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
            
    # If you shoot, move the bullet forward until out of the screen, then reset
    if bullet.state == 'fire':
        bullet.move()
        if bullet.xcor()<-400 or bullet.xcor()>400 or bullet.ycor()<-300 or bullet.ycor()>300:
            bullet.state = 'ready'
            bullet.goto(-340, -240)
    


# Game over
pen.clear()
pen.goto(0,0)
pen.write(f'GAME OVER\nScore: {score}', align='center', font=('Courier', 36, 'normal'))
