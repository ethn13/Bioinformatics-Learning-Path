# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
running = False
success_attempt = 0
total_attempt = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    msecs = t % 10
    secs = (t - msecs) % 600 / 10
    minutes = t // 600
    str_t = str(minutes) + ":"
    if(secs < 10):
        str_t += "0"
    str_t += str(secs)
    str_t += "." + str(msecs)
    return str_t
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = True
    timer.start()

def stop():
    global success_attempt, total_attempt, running
    if(running):
        running = False
        total_attempt += 1
        if(t % 10 == 0):
            success_attempt += 1
        timer.stop()
    
def reset():
    global t, running, success_attempt, total_attempt
    running = False
    timer.stop()
    t = 0
    msec = 0
    success_attempt = 0
    total_attempt = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [120, 150], 20, "Red")
    canvas.draw_text(str(success_attempt) + "/" + str(total_attempt), [250, 30], 20, "Red")
    
# create frame and register event handlers
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()

# Please remember to review the grading rubric
