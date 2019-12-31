# Simple Cannon shooter Jean Joubert 31 October 2019
# Written on OSX and IDLE
# Some values may nees some adjustment in windows
# sound using os.system afplay for mac OS
# use winsound for windows
# This code can be copied, changed, updated and if improved - Please let me know how!!

import turtle
import random
import os # To play wav sound file using afplay in osX
#import time # and time.sleep(0.017 for windows)


win = turtle.Screen()
win.title('Simple Cannon Shooting Game')
win.setup(800,600)
win.bgpic('back1.gif')
win.tracer(0) # Stops window animation until win.update() - try without this
win.listen() # for key presses

cannon = turtle.Turtle()
cannon.shape('square')
cannon.shapesize(2,2) # Double size both x and y axis
cannon.color('blue')
cannon.up() # Lift pen up (don't want to draw)
cannon.goto(-360, -260)

bullet = turtle.Turtle()
bullet.shape('square')
bullet.shapesize(0.2, 0.7)
bullet.color('red')
bullet.lt(50)
bullet.up()
bullet.goto(-340, -240)
bullet.state = 'ready'

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('red')
pen.goto(200,-275)
pen.write('Score: 0', font=('Courier', 24, 'normal'))


def shoot():
    if bullet.state == 'ready':
        os.system('afplay missile.WAV&')
    bullet.state = 'fire'
   
    
def bullet_shot():
    bullet.fd(10) # Go forward 10 pixels (May need adjustment in windows 0.05, etc)
    # If bullet is outside the screen - reset position for shooting
    if bullet.ycor()<-300 or bullet.ycor()>300 or bullet.xcor()>400: 
        bullet.goto(-340, -240)
        bullet.state = 'ready'
        
    
def turn_right():
    if bullet.state == 'ready':
        bullet.rt(10)
    
    
def turn_left():
    if bullet.state == 'ready':
        bullet.lt(10)
    

win.onkey(shoot, 'space')
win.onkey(turn_left, 'Left')
win.onkey(turn_right, 'Right')

enemy_list = []
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'grey']
game_over = False
score = 0

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
            score += 1
            pen.clear()
            pen.write(f'Score: {score}', font=('Courier', 24, 'normal'))






