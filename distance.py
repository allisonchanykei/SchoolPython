#!/usr/bin/env python

import math
def distance(x1,y1,x2,y2):
	d = math.sqrt((x2-x1)**2+(y1-y2)**2)
	if d < 0:
		d = -d
	return d

print distance (4,3,0,0)
