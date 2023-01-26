import turtle

wn=turtle.Screen()
wn.title('PONG BY SONAL')
wn.bgcolor('black')
wn.setup(width=750,height=600)
wn.tracer(1)

#score 
 

#left side
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_len=1,stretch_wid=6)
paddle_a.penup()
paddle_a.setpos(-357,0)

#Right side
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_len=1,stretch_wid=6)
paddle_b.penup()
paddle_b.setpos(350,0)


# ball

ball=turtle.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.setpos(0,0)
ball.dx=3
ball.dy=3

#score Table

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("courier",24,"normal"))

# function for moving

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    end_fill()

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# keyborad connection

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,"Down")







#main
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>365:
        ball.goto(0,0)
        ball.dx*=-1
        
    if ball.xcor()<-365:
        ball.goto(0,0)
        ball.dx*=-1
    
    if(ball.xcor()>340 and ball.xcor()>340 and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-50)):
        ball.setx(340)
        ball.dx*=-1
    if(ball.xcor()<-340 and ball.xcor()<-340 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-50)):
        ball.setx(-340)
        ball.dx*=-1