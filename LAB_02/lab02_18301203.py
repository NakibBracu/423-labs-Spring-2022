from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#as my id is 18301203
#So i have to show last 2 digit and it is 0 and 3
def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #  line_draw_with_points method call korlam
    line_draw_with_points()

    glutSwapBuffers()

# put your drawing codes inside this 'line_draw_with_points' function


def line_draw_with_points():
    glColor3d(0, 1, 0)
    glBegin(GL_POINTS)

    # 0 draw korbo nicher pexel gula diye method call er maddhome
    line_draw_using_midpoint(50, 50, 50, 450)
    line_draw_using_midpoint(50, 50, 200, 50)
    line_draw_using_midpoint(50, 450, 200, 450) 
    line_draw_using_midpoint(200, 50, 200, 450)
    
    #3 draw korbo necher pixel gula diye method call er maddhome
    line_draw_using_midpoint(250, 50, 400, 50)
    line_draw_using_midpoint(250, 250, 400, 250)
    line_draw_using_midpoint(250, 450, 400, 450)
    line_draw_using_midpoint(400, 50, 400, 450)
     

    glEnd()


def line_draw_using_midpoint(x_1, y_1, x_2, y_2):
    
   #Midpoint line drawing algo use korbo
    #(x_1,y_1) ---> starting point
    #(x_2,y_2) ---> ending point
    # 2 points er distance ber korte hobe zone ber korar jonno

    x_difference = x_2 - x_1 #del x ber korlam
    y_difference = y_2 - y_1 #del y ber korlam

    # eikhane zone ber kortesi
    zone = zone_ber_koro(x_difference, y_difference)

 
    # jekono zone theke zone 0 te convert kortesi point gula
    x_1, y_1 = any_zone_points_to_zone0_points(x_1, y_1, zone)
    x_2, y_2 = any_zone_points_to_zone0_points(x_2, y_2, zone)


    # abaro x,y er difference ner korbo
    x_difference = x_2 - x_1 
    y_difference = y_2 - y_1


    #niche hisab er subidharte intial difference and differnce east and difference north east er jonno hisab kore raklam
    difference = 2 * y_difference - x_difference #2dy-dx
    difference_east = 2 * y_difference #2dy
    difference_north_east = 2 * (y_difference - x_difference)#2dy-2dx=2(dy-dx)


    # position NE ba E jetai asuk nah ken x uvoi khetrei bare but y khali north east er khetrei bare
    #tai loop oivabei auto x update hobe x for both cases of northeast and east
    for x in range(x_1, x_2 + 1):
        if difference < 0:#east
            difference += difference_east
        else:#NE
            difference += difference_north_east
            y_1 += 1
        # ekon sobgulake abar ager zone e ferot pathate hobe zone 0 theke cause only midpoint algo er jonno
        # ansilam zone 0 te
        x, y = get_back_to_original_zone_from_zone0(x, y_1, zone)
        # line akbe ekon point gula diye
        glVertex2d(x, y)


def zone_ber_koro(x_difference, y_difference):
   #ekon zone ber korar zonno lagbe dx,dy orthat x,y er difference
    if abs(x_difference) >= abs(y_difference):
        if x_difference >= 0 and y_difference >= 0: # mod dx > mod dy , dx>=0, dy>=0 ==> zone 0
            return 0
        if x_difference >= 0 and y_difference <= 0: # mod dx > mod dy , dx>=0, dy<=0 ==> zone 7
            return 7
        if x_difference <= 0 and y_difference >= 0: # mod dx > mod dy , dx<=0, dy>=0 ==> zone 3
            return 3
        return 4 # mod dx > mod dy , dx<=0, dy<=0 ==> zone 4
    else:
        if x_difference >= 0 and y_difference >= 0: # mod dx < mod dy , dx>=0, dy>=0 ==> zone 1
            return 1
        if x_difference >= 0 and y_difference <= 0: # mod dx < mod dy , dx>=0, dy<=0 ==> zone 6
            return 6
        if x_difference <= 0 and y_difference >= 0: # mod dx < mod dy , dx<=0, dy>=0 ==> zone 2
            return 2
        return 5 #mod dx < mod dy , dx<=0, dy<=0 ==> zone 5


def any_zone_points_to_zone0_points(x, y, zone):
 # zone 0 te convert korbo sob point mid point algo use korar jonno
 #8 way symmetry follow kore korbo sob
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return -y, x
    return x, -y


def get_back_to_original_zone_from_zone0(x, y, zone):
# 8 way symmentry follow kore zone 0 te convert kore ja paisilam ta reverse korle original zone e ferot jabe
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    return x, -y


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Lab02_18301203")
glutDisplayFunc(showScreen)

init()

glutMainLoop()
