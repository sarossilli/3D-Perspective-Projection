
# course: CS2300
# section: 1
# due date: 04/25/20
# name: Sam Rossilli
# email: srossill@uccs.edu
# description: Checks to see if a point is within a subspace of basis vectors

import math
import tkinter as tk
from tkinter import Canvas
import numpy as np


SCREEN_H = 720
SCREEN_W = 1280

F = 1
PROJ_MAT = [[F, 0, 0, 0],
            [0, F, 0, 0],
            [0, 0, 1, 0]]


class triangle:
    def __init__(self, vecA, vecB, vecC):
        self.vectors = [(vecA), (vecB), (vecC)]

    # Function to draw a triangle using canvas
    def draw(self, canvas):
        p1 = self.vectors[0]
        p2 = self.vectors[1]
        p3 = self.vectors[2]

        # L1
        canvas.create_line(p1[0], SCREEN_H - p1[1],
                           p2[0], SCREEN_H - p2[1], width=5, fill='#ffb37d')
        # L2
        canvas.create_line(p2[0], SCREEN_H - p2[1],
                           p3[0], SCREEN_H - p3[1], width=5, fill='#ffb37d')
        # L3
        canvas.create_line(p3[0], SCREEN_H - p3[1],
                           p1[0], SCREEN_H - p1[1], width=5, fill='#ffb37d')
        return True

    # Function to make a new projected trangle
    def project(self, matrix):
        vecs = []
        for vec in self.vectors:
            a = vec[0:3]
            a.append(1)  # Make Homogen Cord
            v_proj = np.matmul(matrix, a)
            z = v_proj[2]
            if z > 0:
                v_proj = [v_proj[0]/z, v_proj[1]/z, 1]
            else:
                v_proj = [0, 0, 0]
            vecs.append(list(v_proj))
        return triangle(vecs[0], vecs[1], vecs[2])

    # Functions to make a new rotated trangle
    def rotate_z(self, fTheta):
        m = [[math.cos(fTheta), math.sin(fTheta), 0, 0],
             [-math.sin(fTheta), math.cos(fTheta), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        vecs = []
        for vec in self.vectors:
            x = vec[0:3]
            x.append(1)
            v_rot = np.matmul(m, x)
            vecs.append(list(v_rot))
        return triangle(vecs[0], vecs[1], vecs[2])

    def rotate_x(self, fTheta):
        m = [[1, 0, 0, 0],
             [0, math.cos(fTheta), math.sin(fTheta), 0],
             [0, -math.sin(fTheta), math.cos(fTheta), 0],
             [0, 0, 0, 1]]
        vecs = []
        for vec in self.vectors:
            x = vec[0:3]
            x.append(1)
            v_rot = np.matmul(m, x)
            vecs.append(list(v_rot))
        return triangle(vecs[0], vecs[1], vecs[2])

    def translate(self, x, y, z):
        vectors = []
        for vec in self.vectors:
            vec[0] += x
            vec[1] += y
            vec[2] += z
            vectors.append(vec)
        return triangle(vectors[0], vectors[1], vectors[2])

    def scale(self, x, y, z):
        vectors = []
        for vec in self.vectors:
            vec[0] *= x
            vec[1] *= y
            vec[2] *= z
            vectors.append(vec)
        return triangle(vectors[0], vectors[1], vectors[2])


# Class represents a hard-coded cube in 3D space
class Box:
    def __init__(self):
        self.tris = [
            # Front
            (triangle([0.0, 0.0, 0.0], [
                0.0, 1.0, 0.0], [1.0, 1.0, 0.0])),
            (triangle([0.0, 0.0, 0.0], [
                1.0, 1.0, 0.0], [1.0, 0.0, 0.0])),

            # Right
            (triangle([1.0, 0.0, 0.0], [
                1.0, 1.0, 0.0], [1.0, 1.0, 1.0])),
            (triangle([1.0, 0.0, 0.0], [
                1.0, 1.0, 1.0], [1.0, 0.0, 1.0])),
            # Back
            (triangle([1.0, 0.0, 1.0], [
                1.0, 1.0, 1.0], [0.0, 1.0, 1.0])),
            (triangle([1.0, 0.0, 1.0], [
                0.0, 1.0, 1.0], [0.0, 0.0, 1.0])),
            # Left
            (triangle([0.0, 0.0, 1.0], [
                0.0, 1.0, 1.0], [0.0, 1.0, 0.0])),
            (triangle([0.0, 0.0, 1.0], [
                0.0, 1.0, 0.0], [0.0, 0.0, 0.0])),
            # Top
            (triangle([0.0, 1.0, 0.0], [
                0.0, 1.0, 1.0], [1.0, 1.0, 1.0])),
            (triangle([0.0, 1.0, 0.0], [
                1.0, 1.0, 1.0], [1.0, 1.0, 0.0])),
            # Bot
            (triangle([1.0, 0.0, 1.0], [
                0.0, 0.0, 1.0], [0.0, 0.0, 0.0])),
            (triangle([1.0, 0.0, 1.0], [
                0.0, 0.0, 0.0], [1.0, 0.0, 0.0])),
        ]


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


def render_loop():
    global th

    w.delete('all')
    for triangle in box.tris:
        triangle = triangle.rotate_x(th)
        triangle = triangle.rotate_z(th*0.3)

        triangle = triangle.translate(0, 0, 3.0)
        # PROJ
        triangle = triangle.project(PROJ_MAT)

        triangle = triangle.translate(1, .7, .7)
        triangle = triangle.scale(500, 500, 1)

        triangle.draw(w)
    w.pack()
    th += .01
    root.after(3, render_loop)


th = .1  # Global Theta for rotation

root = tk.Tk()
app = Window(root)
w = tk.Canvas(root, width=SCREEN_W, height=SCREEN_H, bg='#000000')

box = Box()

render_loop()
root.mainloop()
