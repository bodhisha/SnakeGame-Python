import turtle
import time
import random
import pygame

pygame.mixer.init()
def music():
    pygame.mixer.music.load("The Perfect Snake Game.mp3")
    pygame.mixer.music.play()
music()
delay = 0.1

#Score
score = 0
high_score = 0

#Set up the screen

wn= turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) 

#Snake head

head=turtle.Turtle()
head.speed(0)
head.shape( "square" )
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

#Trap

trap =turtle.Turtle()
trap.speed(0)
trap.shape("triangle")
trap.color("red")
trap.penup()
trap.goto(100,0)

segments= []


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape=("square")
pen.color=("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High Score: 0", align="center", font=("Courier", 24,"normal"))

#functions
def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
       head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"


def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)
        

#keyboard bindings

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loopp

while True:
    wn.update()
    # collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        pygame.mixer.music.load("270344__littlerobotsoundfactory__shoot-00.wav")

        pygame.mixer.music.play()       
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear segment list
        segments.clear()
        
        music()

        #reset score
        score=0

        #reset delay
        delay=0.1

        pen.clear()
        pen.write("Score: {} High Score :{}".format(score,high_score),align="center", font=("Courier", 24,"normal"))

    # Collision with food
    if head.distance(food)<15:

        #pygame.mixer.music.load("167127__crisstanza__pause.mp3")
        #pygame.mixer.music.play()

        #move food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #shorten the delay
        delay -=0.001
        # add segment
        new_segment= turtle.Turtle()
        new_segment.speed()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # increase score
        score +=10
        if score>high_score:
            high_score=score
        
        pen.clear()
        pen.write("Score: {} High Score :{}".format(score,high_score),align="center", font=("Courier", 24,"normal"))

    #move end segment 
    for index in range(len(segments)-1,0,-1):
        x= segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # move segment 0 to where head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #head collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
             #hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segment list
            segments.clear()
            music()

            #reset score
            score=0

            #reset delay
            delay=0.1

            pen.clear()
            pen.write("Score: {} High Score :{}".format(score,high_score),align="center", font=("Courier", 24,"normal"))


    
            


    time.sleep(delay)
wn.mainloop()