# Simple cannon shooting playing with simple gravity in python 3 and turtle
# Jean Joubert 29 December 2019
# Written in osX and IDLE
# Sound using afplay (os.system) for mac osX - use winsound in windows

import turtle
from math import *
import random, os
# import time # and time.sleep(0.017) windows


win = turtle.Screen()
win.title('Simple Shooter')
win.setup(800,600)
win.bgpic('back1.gif')
win.tracer(0)
win.listen()

cannon = turtle.Turtle()
cannon.shape('square')
cannon.shapesize(2,2)
cannon.color('blue')
cannon.up()
cannon.goto(-360, -260)

bullet = turtle.Turtle()
bullet.shape('square')
bullet.shapesize(0.2, 0.7)
bullet.color('red')
bullet.lt(50)
bullet.up()
bullet.goto(-340, -240)
bullet.state = 'ready'
bullet.speed = 22

# bullet.heading() gives the current direction in degrees
# radians() convert degrees to radians for sin/cos/tan
# round(x,2) rounds to 2 decimals
# dx = speed * cos(angle in radians)
# dy = speed * sin(angle in radians)
bullet.dx = bullet.speed * round(cos(radians(bullet.heading())),2)
bullet.dy = bullet.speed * round(sin(radians(bullet.heading())),2)

gravity = 0.4

# For information about speed, angle, dx, dy
pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.up()
pen1.goto(220,-275)
pen1.color('red')
pen1.write(f'bullet speed: {bullet.speed}\nbullet heading: {bullet.heading()}\nbullet.dx: {bullet.dx}\nbullet.dy: {bullet.dy}',
          align='left', font=('Courier', 14, 'normal'))

# Score
pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.goto(0,-275)
pen.color('red')
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))


def shoot():
    if bullet.state == 'ready':
        os.system('afplay missile.WAV&')
    bullet.state = 'fire'
    
    
    
def bullet_shot():
    bullet.goto(bullet.xcor()+bullet.dx, bullet.ycor()+bullet.dy)
    bullet.dy -= gravity

    
    if bullet.ycor()<-300 or bullet.xcor()>400 or bullet.xcor()<-400: 
        bullet.goto(-340, -240)
        bullet.state = 'ready'
        bullet.dx = bullet.speed * round(cos(radians(bullet.heading())),2)
        bullet.dy = bullet.speed * round(sin(radians(bullet.heading())),2)
         

def turn_right():
    if bullet.state == 'ready':
        bullet.rt(10)
        bullet.dx = bullet.speed * round(cos(radians(bullet.heading())),2)
        bullet.dy = bullet.speed * round(sin(radians(bullet.heading())),2)
        pen1.clear()
        pen1.write(f'bullet speed: {bullet.speed}\nbullet heading: {bullet.heading()}\nbullet.dx: {bullet.dx}\nbullet.dy: {bullet.dy}',
              align='left', font=('Courier', 14, 'normal'))

def turn_left():
    if bullet.state == 'ready':
        bullet.lt(10)
        bullet.dx = bullet.speed * round(cos(radians(bullet.heading())),2)
        bullet.dy = bullet.speed * round(sin(radians(bullet.heading())),2)
        pen1.clear()
        pen1.write(f'bullet speed: {bullet.speed}\nbullet heading: {bullet.heading()}\nbullet.dx: {bullet.dx}\nbullet.dy: {bullet.dy}',
              align='left', font=('Courier', 14, 'normal'))

win.onkey(shoot, 'space')
win.onkey(turn_left, 'Left')
win.onkey(turn_right, 'Right')

enemy_list = []
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'grey']
score = 0
game_over = False


while not game_over:
    win.update()
    #time.sleep(0.017) # windows?
    
    if bullet.state == 'fire':
        bullet_shot()


    # Create enemies if there is less than 10 
    delay = random.random() # Creates probability 0-1
    if len(enemy_list)<10 and delay < 0.05: # Can play with this delay
        enemy = turtle.Turtle()
        enemy.shape('circle')
        enemy.shapesize(2,2)
        enemy.color(random.choice(colors))
        enemy.up()
        enemy.goto(420, random.randint(0,280))
        enemy_list.append(enemy)

    for i in enemy_list:
        # Enemies move left
        i.goto(i.xcor()-0.5, i.ycor()) # Value may need adjustment in Windows e.g. 0.01

        # If enemy out on the left - game over
        if i.xcor()<-420:
            i.goto(1000,1000) # Hide off screen
            enemy_list.remove(i)
            game_over = True
            pen.goto(0,0)
            pen.clear()
            pen.write(f'GAME OVER\nScore: {score}',align='center',
                      font=('Courier', 36, 'normal'))
            
        # If bullet hits enemy
        if bullet.distance(i) < 30:
            os.system('afplay pop.wav&') # & added to continue game while sound playing
            i.goto(1000,1000) # Hide off screen
            enemy_list.remove(i)
            bullet.goto(-340, -240)
            bullet.state = 'ready'
            bullet.dx = bullet.speed * round(cos(radians(bullet.heading())),2)
            bullet.dy = bullet.speed * round(sin(radians(bullet.heading())),2)
            score += 1
            pen.clear()
            pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))



    
