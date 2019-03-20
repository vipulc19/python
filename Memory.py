# implementation of card game - Memory

import simplegui
import random

lst=[]
for x in range(8):
    lst.append(x)
for x in range(8):
    lst.append(x)
   
# helper function to initialize globals
def new_game():
    random.shuffle(lst)
    global index1,index2,i,state,moves,exposed
    index1,index2,i,state,moves = 0, 0, 0, 0, 0
    exposed=[False]*16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global index1, index2,i,state,moves
     
    index1 = index2
    index2=i
    i = pos[0] // 50;
    
    if(exposed[i]==False):
        exposed[i]=True
        if(state==2):          
            if(lst[index1]!=lst[index2]):
                exposed[index1]=False
                exposed[index2]=False

        if(state==0):
            state=1
        elif(state==1):
            state=2
            moves+=1
        else:
            state=1		
         
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global lst
    for i in range(16):
        canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
        if(exposed[i]==True):
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(lst[i]), (i*50+11, 69), 55, "Black")

    label.set_text("Turns = " + str(moves))        
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric