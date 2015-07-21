# William T. Verts - Lab #3
import time
def MakeImage(NewWidth,NewHeight,NewSeparation):
    MyCanvas = makeEmptyPicture(NewWidth,NewHeight,yellow)
    show(MyCanvas)
    width = NewWidth-1
    height = NewHeight-1
    for y in range(0,height, NewSeparation):
        addLine(MyCanvas, 0, y, width, y, blue)
        time.sleep(0.2)
        repaint(MyCanvas)

    for x in range(0,width, NewSeparation):
        addLine(MyCanvas, x, 0, x, height, red)
        time.sleep(0.2)
        repaint(MyCanvas)
        
    return
    
def Run():
    W = requestIntegerInRange("Enter Width [1..1024]",1,1024)
    H = requestIntegerInRange("Enter Height [1..768]",1,768)
    N = requestIntegerInRange("Enter Steps [1..50]",1,50)
    MakeImage(W,H,N)
    return 