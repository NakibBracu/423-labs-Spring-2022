from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#(x0,y0)--> start
#(x1,y1)--> end
#DDA
# -1<=m<=1 ; x+=1; y+=m else
# y+=1,x+=1/m
#dhal = kotidoyer ontor/bhujdoyer ontor
#3 portion left, mid, right
#left portion is dotted pixel have gaps between points

def bam(x0,y0, x1, y1):
    glBegin(GL_POINTS)
    if (x0 != x1):
        dhal = (y1-y0)/(x1-x0)
    else:
        dhal = 4e19  #infinity

    if (dhal < 1 and dhal > -1): #-1<m<1
        while(x0 != x1):
            if (x0 % 15 == 0):#dotted line aksi tai emon (gap making er jonno)
                glVertex2f(x0, round(y0))
            x0 = x0+1
            y0 = y0 + dhal
    else:
        while(y0 != y1):
            if (y0 % 15 == 0):
                glVertex2f(round(x0), y0)
            y0 = y0 + 1
            x0 = x0 + (1/dhal)
    glVertex2f(x1, y1)#last point of line
    glEnd()


def majkahne(x0, y0, x1, y1):
    glBegin(GL_POINTS)
    if (x0 != x1):
        dhal = (y1-y0)/(x1-x0)
    else:
        dhal = 4e19 

    if (dhal < 1 and dhal > -1):
        while(x0 != x1):#last point er ag porjonto
            glVertex2f(x0, round(y0))
            x0 = x0 + 1
            y0 = y0 + dhal
    else:
        while(y0 != y1):#last point er ag porjonto
            glVertex2f(round(x0), y0)
            y0 = y0 + 1
            x0 = x0 + (1/dhal)
    glVertex2f(x1, y1)
    glEnd()


def dan(x0, y0, x1, y1):
    glBegin(GL_POINTS)
    if (x0 !=x1):
        dhal = (y1-y0)/(x1-x0)
    else:
        dhal = 4e19  

    if (dhal < 1 and dhal > -1):
        while(x0 != x1):
            glVertex2f(x0, round(y0))
            x0 = x0 + 1
            y0 = y0 + dhal
    else:
        while(y0 != y1):
            glVertex2f(round(x0), y0)
            y0 = y0 + 1
            x0 = x0 + (1/dhal)
    glVertex2f(x1, y1)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(5)
    bam(225,175,225,575)
    majkahne(225,300,325,300)
    dan(325,175,325,575)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("18301203-task3")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
