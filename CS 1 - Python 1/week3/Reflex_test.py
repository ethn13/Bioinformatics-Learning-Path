# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True
text_color = "black"


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def start():
    global first_click, total_ticks, text_color
    if(first_click):
        text_color = "black"
        first_click = False
        total_ticks = 0
        timer.start()
def end():
    global first_click, text_color
    first_click = True
    timer.stop()
    text_color = "white"

# Draw handler
def draw(canvas):
    canvas.draw_text(str(total_ticks*10) + " ms", [100, 100], 20, text_color)
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start timer", start, 200)
frame.add_button("End timer", end, 200)
timer = simplegui.create_timer(10, tick)
frame.set_draw_handler(draw)

# Start timer
frame.start()
