from  sys import getsizeof as s

import turtle

# Set the background color
turtle.bgcolor("orange")

# Create a turle
t = turtle.Turtle()
t.width(2)
t.speed(1)
t.color("red")


class point :
  def color(self,color):
    t.dot(10, color)

  def __init__(self,x=0,y=0) :
    self.x=x
    self.y=y

  def show(self) :
    self.color('blue')

  def hide(self):
    self.color('orange')

  def move_to(self,x,y):
    print('at',x,y)
    self.hide()
    t.penup()
    self.x = x
    self.y = y
    t.goto(self.x, self.y)
    t.pendown()
    self.show()

class circle(point) :
  def __init__(self,x=0,y=0,r=1) :
    super().__init__(x,y)
    self.r=r

  def color(self,color) :
    t.dot(self.r*10,color)

# tests

def go_point() :
  p=point()
  p.show()
  for i in range(1,20) :
    p.move_to(10*i,10*i)

def go_circle():
  c=circle(r=10)
  c.show()
  for i in range(1,20) :
    c.move_to(10*i,10*i)

go_point()
go_circle()




