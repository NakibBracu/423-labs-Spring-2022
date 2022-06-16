import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Ghorer chal banacci nicherta diye
def chal():
    glBegin(GL_TRIANGLES)
    glVertex2f(250, 400)
    glVertex2f(350, 500)
    glVertex2f(450, 400)
    glEnd()

#ghorer edge banabo eifunction barbar call kore
def edges_draw(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
#jalana nicher function diye quadratic way te draw korbo (unused)
# def jalana(x0,y0,x1,y1,x2,y2,x3,y3):
#     glBegin(GL_QUADS)
#     glVertex2f(x0,y0)
#     glVertex2f(x1,y1)
#     glVertex2f(x2, y2)
#     glVertex2f(x3, y3)
#     glEnd()

#dorjar lock just a point
def dorja_lock():
    glBegin(GL_POINTS)
    glVertex2f(360, 240)
    glEnd()

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
    glColor3f(1.0, 1.0, 0.0)#holud color
    glPointSize(5)
    chal() #erpor 14 ta line draw korsi mainly to shape the home
    edges_draw(259, 399, 259, 199)
    edges_draw(439, 399, 439, 199)
    edges_draw(259, 199, 439, 199)
    edges_draw(319, 199, 319, 299)
    dorja_lock()
    edges_draw(379, 199, 379, 299)
    edges_draw(319, 299, 379, 299)
    edges_draw(279, 369, 279, 329)
    edges_draw(279, 369, 319, 369)
    edges_draw(279, 329, 319, 329)
    edges_draw(319, 369, 319, 329)
    edges_draw(419, 369, 419, 329)
    edges_draw(379, 369, 419, 369)
    edges_draw(379, 329, 419, 329)
    edges_draw(379, 369, 379, 329)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("18301203-task2")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()