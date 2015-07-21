#--------------------------------------------------------------------------------
# Bouncing Ball - Lecture of February 17, 2015
# Copyright (C) 2015 -- Dr. William T. Verts
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Important helper routines
#--------------------------------------------------------------------------------

def INT(N):                                                 # Return closest integer to N
    return int(round(N))                                    # See page 168 in "Companion"

def addCircle (Canvas, X, Y, R, NewColor=black):            # See page 180 in "Companion"
    addOval(Canvas, INT(X-R), INT(Y-R), INT(2*R+1), INT(2*R+1), NewColor)
    return
    
def addCircleFilled (Canvas, X, Y, R, NewColor=black):      # See page 180 in "Companion"
    addOvalFilled(Canvas, INT(X-R), INT(Y-R), INT(2*R+1), INT(2*R+1), NewColor)
    return
    
def addCircleGeneral (Canvas, X, Y, R, InColor=white, OutColor=black):
    addCircleFilled(Canvas, X, Y, R, InColor)
    addCircle(Canvas, X, Y, R, OutColor)
    return
 
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

import time        # load external library of functions, including "sleep"
                      
def Main():
    Canvas = makeEmptyPicture(600, 400)                 # Set size of Canvas here
    show(Canvas)                                        # Show blank canvas on screen
    X = getWidth(Canvas) / 2                            # Compute X center based on current size
    Y = getHeight(Canvas) / 2                           # Compute Y center based on current size
    R = 50                                              # Radius
    Xd= 1                                               # Initial X direction
    Yd= 1                                               # Initial Y direction
    while (True):                                       # Infinite loop
        setAllPixelsToAColor(Canvas,white)              # Remove to get "trails"
        addCircleGeneral(Canvas, X, Y, R, yellow, red)  # Yellow balls with red border
        repaint(Canvas)                                 # Show current image
        X = X + Xd                                      # Update center X of ball
        Y = Y + Yd                                      # Update center Y of ball
        if (X + R) >= getWidth(Canvas): Xd = -1         # Bounce off right wall
        if (X - R) <= 0: Xd = 1                         # Bounce off left wall
        if (Y + R) >= getHeight(Canvas): Yd = -1        # Bounce off bottom wall
        if (Y - R) <= 0: Yd = 1                         # Bounce off top wall
        time.sleep(0.001)                               # Seconds to sleep
    return                                              # Is this statement ever executed?
    