# first example of drawing on the canvas

import simplegui

# define draw handler
def draw_text(canvas):
    canvas.draw_text("Hello!", [100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "white", "black")

# create frame
frame = simplegui.create_frame("Test", 300, 200)

# register draw handler    
frame.set_draw_handler(draw_text)

# start frame
frame.start()