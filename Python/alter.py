#!/usr/bin/env python
#alter.py
#Code by Peter Van and Connor Combs
from mcpi.minecraft import Minecraft
from mcpi import block
import time
# ~ mc = Minecraft.create()	
mc = Minecraft.create("10.183.3.20", 4711)

a = 1
o_2 = -2
o_1 = -1
o0 = 0
o1 = 1
o2 = 2
o2_5 = 2.5
o3 = 3
o4 = 4
o5 = 5
o6 = 6
o7 = 7
o8 = 8
o_10 = -10
o10 = 10
c = 1
o43 = 43
o44 = 44
o45 = 45
o155 = 155
mc.postToChat("BOW TO THE ALTER!!!")
while c < 80:
	mc.setBlocks(-10,0,-10,10,100,10,0)
	mc.setBlock(0,o3,4,45)
	mc.setBlock(0,o4,4,45)
	mc.setBlock(0,o5,4,45)
	mc.setBlock(1,o5,4,45)
	mc.setBlock(-1,o5,4,45)
	mc.setBlock(0,o6,4,155)
	mc.setBlock(-1,o6,4,45)
	mc.setBlock(1,o6,4,45)
	mc.setBlock(-2,o6,4,45)
	mc.setBlock(2,o6,4,45)	
	mc.setBlock(0,o7,4,45)
	mc.setBlock(1,o7,4,45)
	mc.setBlock(-1,o7,4,45)
	mc.setBlock(0,o8,4,45)
	mc.setBlock(0,o1,4,43)
	mc.setBlock(0,o1,5,43)
	mc.setBlock(0,o1,3,43)
	mc.setBlock(1,o1,4,43)
	mc.setBlock(-1,o1,4,43)
	mc.setBlock(0,o1,4,43)
	mc.setBlock(0,-5,4,44)
	mc.setBlock(-2,o1,4,44)
	mc.setBlock(2,o1,4,44)
	mc.setBlock(0,o1,6,44)
	mc.setBlock(0,o1,2,44)
	mc.setBlock(1,o1,3,44)
	mc.setBlock(1,o1,5,44)
	mc.setBlock(-1,o1,3,44)
	mc.setBlock(-1,o1,5,44)

	o_2 += 1
	o_1 += 1
	o0 += 1
	o1 += 1
	o2 += 1
	o2_5 += 1
	o3 += 1
	o4 += 1
	o5 += 1
	o6 += 1
	o7 += 1
	o8 += 1
	o_10 += 1
	o_10 += 1
	c += 1
	time.sleep(0.25)
	if c == 79:
		c -= 80
		o_2 -= 78
		o_1 -= 78
		o0 -= 78
		o1 -= 78
		o2 -= 78
		o2_5 -= 78
		o3 -= 78
		o4 -= 78
		o5 -= 78
		o6 -= 78
		o7 -= 78
		o8 -= 78
		o_10 -= 78
		o10 -= 78
		o43 += 1
		o44 += 1		
		o45 += 1
		o155 += 1
		
#Code by Peter Van and Connor Combs
