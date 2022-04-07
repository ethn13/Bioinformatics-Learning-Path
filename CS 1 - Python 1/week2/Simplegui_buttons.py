#starting point of a calculator
import simplegui

#initialize globals
store = 12
operand = 3

#define event handler functions that manipulate store and operand
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store += operand
    output()
    
def subtract():
    global store, operand
    store -= operand
    output()
    

# Create a frame
frame = simplegui.create_frame("Calculator", 200, 200)

# Register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 50)
frame.add_button("Add", add, 100)
frame.add_button("Subtract", subtract, 50)


# Start frame
frame.start()
