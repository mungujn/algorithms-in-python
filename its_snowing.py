''' 
    Randomly places n snowflakes to simulate snowing.
    Applies The Koch snowflake algorithm(recursion type) 
    
    Adjust n in __main__ to 1 and order to 5 plus length to 100 to see true form of 1 snowflake 
    Catalyst Code Competition Practice 
'''

from turtle import *
from random import randint

# recursive function to create koch snowflakes
def snowflake(lengthSide, levels):    
    if levels == 0:         
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
    right(120) 
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
  
# main function 
if __name__ == "__main__":
    #adjust n here 
    x,y,n = 0,0,200

    while n>0: 
        penup()       
        setpos(randint(-300,300),randint(-300,300))
        # Choose colours and size
        color("sky blue", "white")
        bgcolor("black")

        #adjust order and size
        order = 2                
        length = 10.0   
    
        # Pull the pen up – no drawing when moving.          
        penup()                 
        backward(length/2.0)  
        # Pull the pen down – drawing when moving.         
        pendown()            
        # Make it fast
        tracer(100)
        hideturtle()

        begin_fill()
        for i in range(3):     
            snowflake(length, order) 
            right(120)
        end_fill()

        # Make the last parts appear
        update()

        # Next snowflake position.
        penup()   
        setpos(0,0)
        n-=1
     # To control the closing windows of the turtle 
    mainloop()   




