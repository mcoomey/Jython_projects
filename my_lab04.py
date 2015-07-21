# 
#--------------------------------------------------------------
# This function paints a filled circle of radius R
# and color NewColor on the Canvas, using <Xc,Yc> as
# the coordinates of the center of the circle.
#--------------------------------------------------------------
def addCircleFilled (Canvas,Xc,Yc,R,NewColor=black):
 addOvalFilled(Canvas, int(Xc-R), int(Yc-R), int(R+R), int(R+R), NewColor)
 return 
#--------------------------------------------------------------
# This function paints one anime eyeball on the Canvas,
# centered at <Xc,Yc>. The color of the iris is NewColor, the
# pupil is black, and the highlight is white. The sizes and
# positions of the iris, pupil, and highlight are derived
# from center point <Xc,Yc> and from radius R.
#--------------------------------------------------------------

def Eyeball (Canvas,Xc,Yc,R,NewColor):
  Offset = (R * math.sqrt(2))/4
  addCircleFilled(Canvas, Xc, Yc, R, NewColor)
  addCircleFilled(Canvas, Xc, Yc, R/2, black)
  addCircleFilled(Canvas, Xc+Offset, Yc-Offset, R/4, white)
  return
#--------------------------------------------------------------
# This function paints two anime eyeballs on the canvas.
# It first must determine the correct radius and center
# positions before calling Eyeball twice (once for each eye).
#--------------------------------------------------------------
def Stare (Canvas,NewColor):
  W = getWidth(Canvas)
  H = getHeight(Canvas)
  Xleft = W/4
  Xright = 3*W/4
  Y = H/2
  R = min(Xleft, Y) * 2/3 - 5
  Eyeball(Canvas, Xleft, Y, R, NewColor)
  Eyeball(Canvas, Xright, Y, R, NewColor)
  repaint(Canvas)
  return
#--------------------------------------------------------------
# This function establishes the size of the canvas and the
# color of the anime eyes. These values are currently hard-
# coded into the program, but could be input from the user
# instead.
#--------------------------------------------------------------
def Run():
 Canvas = makeEmptyPicture(640,400,white)
 show(Canvas)
 Stare(Canvas,blue)
 return 