#!usr/bin/env python
# save file as forloop1.py
print("DEC\t  HEX\t\tBIN\t\tCHAR")
for d in range(32,128):
	h = hex(d)
	h = h.replace("0x", "$ ")
	b = bin(d)
	h = b.replace("0b", "- ")
	c = chr(d)
	# ~ print(str(d)+" "+h ,end = " ")
	print(str(d) + "\t" + h + "\t" + b + "\t" + c)

# ~ str(d)+" "  is call conatination
