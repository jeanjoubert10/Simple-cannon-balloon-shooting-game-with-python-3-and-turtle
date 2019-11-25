# Simple Cannon shooting game with classes J Joubert October 2019
# Written in OSX - some values may need adjustment in windows
# Sound using os.system afplay for max OS
# use winsound for windows
# Game class allows for start/game over screen/restart game



import turtle
import random
import os # To play wav file using afplay


class Cannon(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.shapesize(2,2)
        self.color('blue')
        self.goto(-360, -260)


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


class Game():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.title('Simple cannon shooter')
        self.win.bgcolor('black')
        self.win.setup(800,600)
        self.win.tracer(0)
        self.win.listen()

        
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple']
        self.pen = Scoreboard()
        
        
    def new_game(self):
        
        self.pen.clear()
        self.pen.goto(200,-200)
        self.pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))
        self.cannon = Cannon()
        self.bullet = Bullet()
        self.enemy_list = []
        self.score = 0


        self.run()
        
    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()

        

    def events(self):
        self.win.onkey(self.bullet.shoot, 'space')
        self.win.onkey(self.bullet.right, 'Right')
        self.win.onkey(self.bullet.left, 'Left')
     

    def update(self):
        self.win.update()
        
        self.delay = random.random()

       
        # Create enemies
        if len(self.enemy_list) < 10 and self.delay < 0.02:
            self.enemy = Enemy()
            self.enemy.color(random.choice(self.colors))
            self.enemy_list.append(self.enemy)

        # Move enemies left
        for i in self.enemy_list:
            i.move()

            # Game over if enemy goes out on the left
            if i.xcor()<-400:
                self.playing = False
                os.system('say "game over"')

            # If enemy is shot, reset bullet and remove enemy from list
            if i.distance(self.bullet)<30:
                os.system('afplay pop.wav&') # & is added to continue game while sound playing
                i.goto(1000,1000)
                self.enemy_list.remove(i)
                self.bullet.state = 'ready'
                self.bullet.goto(-340,-240)
                self.pen.clear()
                self.score += 1
                self.pen.write(f'Score: {self.score}', align='center', font=('Courier', 24, 'normal'))
            
        # If you shoot, move the bullet forward until out of the screen, then reset
        if self.bullet.state == 'fire':
            self.bullet.move()
            if self.bullet.xcor()<-400 or self.bullet.xcor()>400 or self.bullet.ycor()<-300 or self.bullet.ycor()>300:
                self.bullet.state = 'ready'
                self.bullet.goto(-340, -240)


    def show_start_screen(self):
      
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('Simple Cannon shooter using Python 3 and Turtle\n\n Press the "space" key to continue',
                      align='center', font=('Courier', 24, 'normal'))


    def show_game_over_screen(self):
        for i in self.enemy_list:
            i.goto(1000,1000)
            self.bullet.goto(1000,1000)
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write(f'GAME OVER - Score: {self.score} \n\n Press the "space" key for new game',
                      align='center', font=('Courier', 24, 'normal'))


    def wait_for_keypress(self):
        self.waiting = False


  


game = Game()
game.show_start_screen()

while True:
    game.new_game()
    game.show_game_over_screen()


   
    
 
