import random
import numpy
def tupleDivision(a,b):
  c = tuple(ele1 // ele2 for ele1, ele2 in zip(a, b)) 
  return c
def randomNum(e,g):
 return random.randint(int(e),int(g))
def addAllNumInArray(aname):
 return sum(aname)
