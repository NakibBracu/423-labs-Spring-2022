import random
#random point generate korbo tai random library import korbo
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# nicher function diye point draw korbo
# x0,y0 te sthananko change hoye hoye asbe and draw korbo
#eikhane randomly point generate korte hobe
#so points draw function e (x,y) co-ordinates pathabo
#loop use korbo jeta 50 bar ghurbe
#random point generate and draw them

def draw_the_points(x0, y0):
    glPointSize(6) #point size = 6
    glBegin(GL_POINTS) # point neya suru
    glVertex2f(x0, y0) #point gula exact sthananko peye draw hobe
    glEnd()  #point draw sesh


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    # points has been drawn via this loop
    for i in range(0, 50):
        draw_the_points(x_ongsher_point[i], y_ongsher_point[i])
    glutSwapBuffers()

x_ongsher_point = []
y_ongsher_point = []
#loop chalacci 50 bar and prottekbar random point generate kortesi 
#x onngsher jonno kortasi and y ongsher jonno kortesi
for j in range(0, 50):
    x_ongsher_point.append(random.randint(20, 550))
    y_ongsher_point.append(random.randint(20, 550))

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("18301203-task-1")#output terminal er column name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
