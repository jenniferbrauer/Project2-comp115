import turtle

def draw_circles(t, num_circles, size, decrease_amount):
  for _ in range(num_circles):
      t.circle(size)
      size -= decrease_amount


def draw_special(t, size, repeat, num_circles, decrease_amount):
  for _ in range(repeat):
      draw_circles(t, num_circles, size, decrease_amount)
      t.right(360 / repeat)

def draw_picture(size, repeat, num_circles, decrease_amount):
    wn = turtle.Screen()
    wn.bgcolor('seagreen')
    t = turtle.Turtle()
    t.speed(0)

    colors = ['rebeccapurple', 'darkmagenta', 'violet', 'lightpink', 'lavender']

    for color in colors:
        t.color(color)
        draw_special(t, size, repeat, num_circles, decrease_amount)
        size -= decrease_amount 

    wn.exitonclick()

draw_picture(100, 10, 10, 10) 