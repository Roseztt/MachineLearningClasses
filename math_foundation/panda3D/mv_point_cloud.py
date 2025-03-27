#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π
from panda3d.core import LineSegs, NodePath, PointLight
from panda3d.core import Material, TransparencyAttrib
from direct.gui.OnscreenImage import OnscreenImage
import math

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		self.cloud = point_cloud(self, mean=[2,1,1])
		self.accept("m", self.move_cloud)

	def move_cloud(self):
		X = self.cloud.pos()
		X = X - np.array([0.2, 0, 0.2])
		self.cloud.redraw(X)
		

app = cloud_of_points()
app.run()


