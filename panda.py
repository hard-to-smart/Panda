
import turtle
import time
import math

# Initializing turtle and screen
def initialize_turtle():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    t = turtle.Turtle()
    t.pensize(6)
    t.speed(0)
    return t, screen

# moving to a position
def go(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    
# Drawing the wall line
def draw_wall_line(t):
    go(t, -300, -100)
    t.forward(600)
# Ears
def draw_ear(t, x, y):
    t.fillcolor("#282928")
    go(t, x, y)
    t.begin_fill()
    t.circle(45)
    t.end_fill()

def draw_ears(t):
    draw_ear(t, 150, 95)  # Right ear
    draw_ear(t, -50, 130)  # Left ear
# Head
def draw_head(t):
    t.fillcolor("white")
    go(t, -120, 70)
    t.setheading(-100)
    t.begin_fill()
    t.circle(90, 30)
    t.circle(160, 120)
    t.circle(90, 30)
    t.circle(151, 180)
    t.end_fill()

# nose
def draw_nose(t):
    t.fillcolor("black")
    go(t, 20, 60)
    t.setheading(-5)
    t.begin_fill()
    t.circle(-30, 40)
    t.circle(-5, 90)
    t.circle(-20, 115)
    t.circle(-8, 180)
    t.end_fill()

    go(t, 18, 40)
    t.setheading(-110)
    t.pensize(5)
    t.forward(5)
    t.circle(15, 140)
    t.circle(15, -140)
    t.circle(-15, 140)
# hands
def draw_hand(t, x, y, heading, forward1, circle1, forward2, circle2, circle3, circle4, heading2, circle5):
    t.fillcolor("#323232")
    go(t, x, y)
    t.setheading(heading)
    t.begin_fill()
    t.forward(forward1)
    t.circle(circle1[0], circle1[1])
    t.forward(forward2)
    t.circle(circle2[0], circle2[1])
    t.circle(circle3[0], circle3[1])
    t.circle(circle4[0], circle4[1])
    t.circle(circle4[2], circle4[3])
    t.setheading(heading2)
    t.circle(circle5[0], circle5[1])
    t.end_fill()

def draw_hands(t):
    draw_hand(t, -100, -5, -125, 40, (50, 123), 50, (-10, 30), (20, 120), (45, 120, 45, -17), 148, (-160, 25))  # Left hand
    draw_hand(t, 150, -30, -39, 0, (-55, 145), 75, (10, 30), (-20, 120), (-45, 100, 50, -20), 19, (160, 28))  # Right hand


#  eye shape
def draw_eye_shape(t, x, y, heading, circle_params):
    t.fillcolor("#424242")
    t.pensize(4)
    go(t, x, y)
    t.setheading(heading)
    t.begin_fill()
    for radius, extent in circle_params:
        t.circle(radius, extent)
    t.end_fill()

#  black ratina
def draw_ratina(t, x, y):
    go(t, x, y)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

#  lens
def draw_lens(t, x, y):
    go(t, x, y)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(6)
    t.end_fill()

# Drawing left and right eyes
def draw_eyes(t):
    # Left eye
    left_eye_params = [(20, 160), (-20, 70), (20, 160), (50, 105)]
    draw_eye_shape(t, -70, 45, -70, left_eye_params)

    # Right eye
    right_eye_params = [(20, 160), (50, 110), (20, 160), (-20, 70)]
    draw_eye_shape(t, 70, 25, -120, right_eye_params)
   
#  Z
def draw_and_undo_z(t, x, y, size, angle, delay=0.2):
    go(t, x, y)
    t.setheading(angle)
    t.write("Z", font=("Arial", size, "bold"))
    time.sleep(delay) 
    t.undo()  
# Draw the sleeping symbols
def draw_sleeping_symbols(t):
    draw_and_undo_z(t, 60, 100, 48, -20, 1)
    draw_and_undo_z(t, 100, 130, 36, -20, 1)
    
colors = ["red", "purple", "gold", "green", "blue", "indigo", "violet"]

# writing text
def write_curved_text(t, text, radius, angle):
    start_x = -170
    start_y = radius - radius * math.sin(math.radians(angle*2))
    
    go(t, start_x,start_y)
    t.setheading(-angle / 2)
    
    angle_increment = angle / len(text)
    
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        t.color(color)
        
        cur_angle = angle_increment * i
        x = radius * math.sin(math.radians(cur_angle))
        y = radius - radius * math.cos(math.radians(cur_angle))
        
        go(t, start_x + y, start_y + x)
        t.write(char, align="center", font=("Comic Sans MS", 36, "bold"))

def draw_panda():
    t, screen = initialize_turtle()
    draw_wall_line(t)
    draw_hands(t)
    draw_ears(t)
    draw_head(t)
    draw_eyes(t)
    draw_nose(t) 
    t.hideturtle()
    for _ in range(3):
        draw_sleeping_symbols(t)
    draw_ratina(t, -45, 70)
    draw_ratina(t, 90, 35)
    draw_lens(t, -40, 75)
    draw_lens(t, 95, 40)
  
    write_curved_text(t, "Have a nice day!", 200, 200) 
    screen.bgcolor("lemonchiffon")
    turtle.done()


draw_panda()