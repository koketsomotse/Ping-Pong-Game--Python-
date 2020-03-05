
#impoert the turtle module
import turtle
#importing the sound using windows
import winsound


#setting up the screen of the game
wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score for both players

score_a = 0
score_b = 0

#crerating Player A
player_a=turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("red")
#need to resize the size of player A
player_a.shapesize(stretch_wid = 6, stretch_len=1)
player_a.penup()
player_a.goto(-350,0)


#creating Player B
player_b=turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("blue")
#need to resize the size of player B
player_b.shapesize(stretch_wid = 6, stretch_len=1)
player_b.penup()
player_b.goto(350,0)


#creating The Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
#everytime our ball moves, it moves at 1 pixl per sec
ball.dx = 0.5
ball.dy = 0.5


#Pen for the scoring

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 26, "normal"))





#functions
#Moving player A
def player_a_up():
    y = player_a.ycor()
    #adding 20 pixles up
    y = y + 20
    player_a.sety(y)


def player_a_down():
    y = player_a.ycor()
    #adding 20 pixles up
    y = y - 20
    player_a.sety(y)



#Moving player B
def player_b_up():
    y = player_b.ycor()
    #adding 20 pixles up
    y = y + 20
    player_b.sety(y)


def player_b_down():
    y = player_b.ycor()
    #adding 20 pixles up
    y = y - 20
    player_b.sety(y)




#Keyborad binding
wn.listen()
wn.onkeypress(player_a_up,"w")
wn.onkeypress(player_a_down,"s")
wn.onkeypress(player_b_up,"Up")
wn.onkeypress(player_b_down,"Down")
     


#main game loop

while True:
    #everytime the game plays, it will update
    wn.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder checking
    
    #top boarder
    if ball.ycor() > 290:
        ball.sety(290)
        #this reverses the dirction of the ball
        ball.dy *= -1
        #adding sound
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

      #bottom boarder  
    if ball.ycor() <- 290:
        ball.sety(-290)
        #this reverses the dirction of the ball
        ball.dy *= -1
        #adding sound
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        #clears the current score on the game
        pen.clear()
        #update the printed score
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 26, "normal"))


    if ball.xcor()< -390:
                  
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        #clears the current score on the game
        pen.clear()
        #update the printed score
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 26, "normal"))



    #Player and ball collicions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #adding sound
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        #adding sound
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
