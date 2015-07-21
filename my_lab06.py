# William T. Verts

#----------------------------------------------------------
# Functions that operate on individual pixels.
# All new pixel functions will appear in this list.
#----------------------------------------------------------
def Pixel_Average_RGB(px):
    return ((getRed(px) + getGreen(px) + getBlue(px)) / 3)
    
#----------------------------------------------------------

def Pixel_Mono(px):    
    if Pixel_Average_RGB(px) > 127:
        setColor(px, white)
    else:
        setColor(px, black)
    
    return
#----------------------------------------------------------

def alt_Pixel_Gray4(px):
    average = Pixel_Average_RGB(px)
    
    if (average <64):
        setColor(px, black)
    elif (average < 128):
        setColor(px, darkGray)
    elif (average < 192):
        setColor(px, lightGray)
    else:
        setColor(px, white)
    return
    
#----------------------------------------------------------

def Pixel_Gray4(px):
    grayScale = (black, darkGray, lightGray, white)
    index = Pixel_Average_RGB(px) / 64
    setColor(px, grayScale[index])

    return
    
#----------------------------------------------------------

def Pixel_RGB(px):
    setRed(px, (getRed(px) / 128) * 255)
    setGreen(px, (getGreen(px) / 128) * 255)
    setBlue(px, (getBlue(px) / 128) * 255)
  
    return
    
#----------------------------------------------------------

def Pixel_Gray(px):
    ave = Pixel_Average_RGB(px)
    setColor(px, makeColor(ave, ave, ave))
    return
    
#----------------------------------------------------------

def Pixel_Negate(px):
    setColor(px, makeColor(255-getRed(px), 255-getGreen(px), 255-getBlue(px)))
    return
    
#----------------------------------------------------------

def Pixel_Lighter(px):
    #get new color values but make sure not more than 255
    newRed = min(getRed(px)+20, 255)
    newGreen = min(getGreen(px)+20, 255)
    newBlue = min(getBlue(px)+20, 255)
    setColor(px, makeColor(newRed, newGreen, newBlue))
    return
    
#----------------------------------------------------------

def Pixel_Darker(px):
    #get new color values but make sure not less than 0
    newRed = max(getRed(px)-20, 0)
    newGreen = max(getGreen(px)-20, 0)
    newBlue = max(getBlue(px)-20, 0)
    setColor(px, makeColor(newRed, newGreen, newBlue))
    return
    
#----------------------------------------------------------

def Pixel_Inc_R(px):
    #get new red value but make sure not more than 255
    newRed = min(getRed(px)+20, 255)
    setColor(px, makeColor(newRed, getGreen(px), getBlue(px)))
    return
    
#----------------------------------------------------------

def Pixel_Inc_G(px):
    #get new green value but make sure not more than 255
    newGreen = min(getGreen(px)+20, 255)
    setColor(px, makeColor(getRed(px), newGreen, getBlue(px)))
    return
    
#----------------------------------------------------------

def Pixel_Inc_B(px):
    #get new blue value but make sure not more than 255
    newBlue = min(getBlue(px)+20, 255)
    setColor(px, makeColor(getRed(px), getGreen(px), newBlue))
    return
    
#----------------------------------------------------------
def Pixel_Dec_R(px):
    #get new red value but make sure not less than 0
    newRed = max(getRed(px)-20, 0)
    setColor(px, makeColor(newRed, getGreen(px), getBlue(px)))

    return
    
#----------------------------------------------------------

def Pixel_Dec_G(px):
    #get new green value but make sure not less than 0
    newGreen = max(getGreen(px)-20, 0)
    setColor(px, makeColor(getRed(px), newGreen, getBlue(px)))
 
    return
    
#----------------------------------------------------------

def Pixel_Dec_B(px):
    #get new blue value but make sure not less than 0
    newBlue = max(getBlue(px)-20, 0)
    setColor(px, makeColor(getRed(px), getGreen(px), newBlue))

    return

#----------------------------------------------------------

def SwapPixel(PX1, PX2):
    C1 = getColor(PX1)
    C2 = getColor(PX2)
    setColor(PX1, C2)
    setColor(PX2, C1)
    return

#----------------------------------------------------------

def Mirror(Canvas):
    width = getWidth(Canvas)-1
    for Y in range(getHeight(Canvas)-1):
        for X in range(width/2):
            PX1 = getPixel(Canvas, X, Y)
            PX2 = getPixel(Canvas, width-X, Y)
            SwapPixel(PX1, PX2)
        repaint(Canvas)
    return

#----------------------------------------------------------

def Flip(Canvas):
    height = getHeight(Canvas)-1
    for X in range(getWidth(Canvas)-1):
        for Y in range(height/2):
            PX1 = getPixel(Canvas, X, Y)
            PX2 = getPixel(Canvas, X, height-Y)
            SwapPixel(PX1, PX2)
        repaint(Canvas)
    return
    
#----------------------------------------------------------
# Function that scans an image and calls function 'FN' on
# every pixel, repainting the canvas after each line of
# the image has been processed.  The actual function used
# by FN is passed in from outside, through the parameters.
#----------------------------------------------------------

def Process(Canvas,FN):
    for Y in range(getHeight(Canvas)):
        for X in range(getWidth(Canvas)):
            FN(getPixel(Canvas,X,Y))
        repaint(Canvas)
    return

#----------------------------------------------------------
# Return a new canvas from an external graphics file

def OpenFile ():
    Filename = pickAFile()
    if Filename == None:
        return None
    else:
        return makePicture(Filename)

#----------------------------------------------------------
# Save canvas to an external file
SequenceNumber = 0
BaseFolder = ''

def SaveFile (Canvas):
    global SequenceNumber, BaseFolder
    
    SequenceNumber += 1
    
    SequenceString = str(SequenceNumber)
    while (len(SequenceString)<5):
        SequenceString = '0' + SequenceString
    FileName = BaseFolder + 'SAVE' + SequenceString + '.jpg'
    writePictureTo(Canvas, FileName)
    return

#----------------------------------------------------------
# Interactive command processor.  Note that Message is a
# multiline string so line-breaks are included when the
# requestString function is called.  Note as well that
# all commands are single characters, and that many upper
# and lower case letters are treated identically (this need
# not be the case, as new commands in this assignment will
# use upper case letters to do one thing and lower case to
# do another).
#----------------------------------------------------------

def Main():
    
    global BaseFolder
    BaseFolder = pickAFolder()
    
    # make sure they didn't click 'Cancel'
    while (BaseFolder == None):
        BaseFolder = pickAFolder()
        
    Message = """Enter a Command.
    
O=Open, S=Save, M=Mirror, F=Flip
2=Mono, 4=Gray4, 8=RGB, ~=PixelGrey, -=Negate,
>=Lighten, <=Darken
R G B = Increase saturation of R, G, or B
r g b = Decrease saturation of R, G, or B
Q=Quit"""

    Canvas = OpenFile()
    
    if Canvas != None:
        Done = False
        
        while (not Done):
            repaint(Canvas)
            Input = requestString(Message)
        
            if Input != None:           # only process input -- ignore clicked 'cancel'

                if len(Input) != 1:     # user typed too many or no characters
                    Command = 0         # so force an Illegal Command message
                else:
                    Command = Input[0]  # get the command character
        
                # go and dispatch the command
            
                if   (Command == "q") or (Command == "Q"): Done = True
                elif (Command == "o") or (Command == "O"): Canvas = OpenFile()
                elif (Command == "s") or (Command == "S"): SaveFile(Canvas)
                elif (Command == "m") or (Command == "M"): Mirror(Canvas)
                elif (Command == "f") or (Command == "F"): Flip(Canvas)
                elif (Command == "2"): Process(Canvas,Pixel_Mono)
                elif (Command == "4"): Process(Canvas,Pixel_Gray4)
                elif (Command == "8"): Process(Canvas,Pixel_RGB)
                elif (Command == "~"): Process(Canvas,Pixel_Gray)
                elif (Command == "-"): Process(Canvas,Pixel_Negate)
                elif (Command == ">"): Process(Canvas,Pixel_Lighter)
                elif (Command == "<"): Process(Canvas,Pixel_Darker)
                elif (Command == "R"): Process(Canvas,Pixel_Inc_R)
                elif (Command == "G"): Process(Canvas,Pixel_Inc_G)
                elif (Command == "B"): Process(Canvas,Pixel_Inc_B)
                elif (Command == "r"): Process(Canvas,Pixel_Dec_R)
                elif (Command == "g"): Process(Canvas,Pixel_Dec_G)
                elif (Command == "b"): Process(Canvas,Pixel_Dec_B)
                else: showError("Illegal Command")    
        
        Canvas.hide()    # we're exiting the while loop so clean up the screen
        del Canvas       #  and delete the Canvas variable
    return
    

def WTV_Main():

    global BaseFolder
    BaseFolder = pickAFolder()
    
    Message = """Enter a Command.
    
O=Open, S=Save, M=Mirror, F=Flip
2=Mono, 4=Gray4, 8=RGB, ~=PixelGrey, -=Negate,
>=Lighten, <=Darken
R G B = Increase saturation of R, G, or B
r g b = Decrease saturation of R, G, or B
Q=Quit"""

    Canvas = makeEmptyPicture(320,200)
    Done = False
    while (not Done):
        repaint(Canvas)
        Input = requestString(Message) + " "    
        Command = Input[0]
        if   (Command == "q") or (Command == "Q"): Done = True
        elif (Command == "o") or (Command == "O"): Canvas = OpenFile()
        elif (Command == "s") or (Command == "S"): SaveFile(Canvas)
        elif (Command == "m") or (Command == "M"): Mirror(Canvas)
        elif (Command == "f") or (Command == "F"): Flip(Canvas)
        elif (Command == "2"): Process(Canvas,Pixel_Mono)
        elif (Command == "4"): Process(Canvas,Pixel_Gray4)
        elif (Command == "8"): Process(Canvas,Pixel_RGB)
        elif (Command == "~"): Process(Canvas,Pixel_Gray)
        elif (Command == "-"): Process(Canvas,Pixel_Negate)
        elif (Command == ">"): Process(Canvas,Pixel_Lighter)
        elif (Command == "<"): Process(Canvas,Pixel_Darker)
        elif (Command == "R"): Process(Canvas,Pixel_Inc_R)
        elif (Command == "G"): Process(Canvas,Pixel_Inc_G)
        elif (Command == "B"): Process(Canvas,Pixel_Inc_B)
        elif (Command == "r"): Process(Canvas,Pixel_Dec_R)
        elif (Command == "g"): Process(Canvas,Pixel_Dec_G)
        elif (Command == "b"): Process(Canvas,Pixel_Dec_B)
        else: showError("Illegal Command")    
    return