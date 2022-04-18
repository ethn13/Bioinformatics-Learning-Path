# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PAD_VEL_DELTA = 2
LEFT = "left"
RIGHT = "right"

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if(direction == RIGHT):
        ball_vel = [random.randrange(120, 240), -random.randrange(60, 180)]
    elif(direction == LEFT):
        ball_vel = [-random.randrange(120, 240), -random.randrange(60, 180)]
    else:
        ball_vel = [100, 5]
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    #Collision (vertical)
    if(ball_pos[1] - BALL_RADIUS <= 0):
        ball_vel[1] = -ball_vel[1]
    if(HEIGHT - BALL_RADIUS - ball_pos[1] <= 0):
        ball_vel[1] = -ball_vel[1]
    # update ball
    ball_pos[0] += ball_vel[0] / 120.0
    ball_pos[1] += ball_vel[1] / 120.0
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white")
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos[1] + paddle1_vel >= 0 and paddle1_pos[1] + paddle1_vel + PAD_HEIGHT <= HEIGHT):
        paddle1_pos[1] += paddle1_vel
    if(paddle2_pos[1] + paddle2_vel >= 0 and paddle2_pos[1] + paddle2_vel + PAD_HEIGHT <= HEIGHT):
        paddle2_pos[1] += paddle2_vel
    # draw paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "white")
    # determine whether paddle and ball collide 
    if(ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH):
        if(ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.1)
        else:
            score1 += 1
            spawn_ball(LEFT)
    if(ball_pos[0] - BALL_RADIUS <= PAD_WIDTH):
        if(ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.1)
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # draw scores
    canvas.draw_text(str(score1), [PAD_WIDTH + (WIDTH/2 - (PAD_WIDTH)/2)/2, 25], 20, "white") 
    canvas.draw_text(str(score2), [WIDTH/2 + (WIDTH/2 - (PAD_WIDTH)/2)/2, 25], 20, "white") 
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel = -PAD_VEL_DELTA
    if(key == simplegui.KEY_MAP["s"]):
        paddle1_vel = PAD_VEL_DELTA
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel = -PAD_VEL_DELTA
    if(key == simplegui.KEY_MAP["down"]):
        paddle2_vel = PAD_VEL_DELTA
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = paddle2_vel = 0

def restart():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)


# start frame
new_game()
frame.start()
