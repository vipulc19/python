# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0		# to keep track of tenth of seconds
success = stops = 0
running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t/600
    D = t%10
    B = (t%600)/10
    return str(A)+":"+'%02d' %B+"."+str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global running, stops, success
    if(running == True):
        timer.stop()
        running = False
        stops += 1
        if(counter%10 == 0):
            success += 1
            
def reset():
    timer.stop()
    global counter, success, stops, running
    counter = success = stops = 0	
    running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [125,100], 24, "White")
    canvas.draw_text(str(success)+"/"+str(stops),[270,30],18,"White")
    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100,tick)

# start frame
frame.start()
#timer.start()
# Please remember to review the grading rubric
