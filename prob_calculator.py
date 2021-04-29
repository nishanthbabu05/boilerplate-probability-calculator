import copy
import random


# Consider using the modules imported above.

class Hat:
  def __init__(self, **h):
    self.k = copy.deepcopy(h)

    self.contents = []
    for l, v in h.items():
      for i in range(1, v + 1):
        self.contents.append(l)

  def draw(self, n):

    w=copy.deepcopy(self.contents)
    z=copy.deepcopy(self.contents)
    if (n < len(w)):
      x = []
      c = n
      while (c > 0):
        
        l=random.choice(w)
        x.append(l)
        w.remove(l)
        self.contents.remove(l)

        c -= 1

      return x
    else:
      self.contents=copy.deepcopy(z)
      return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  q = copy.deepcopy(hat.contents)
  n = num_experiments
  m = 0
  c = []
  for k, v in expected_balls.items():
    for i in range(1, v + 1):
      c.append(k)

  while (n > 0):
    ct = 0
    t = hat.draw(num_balls_drawn)
    hat.contents=copy.deepcopy(q)

    for ii in c:

      if t.count(ii)>=c.count(ii):
        ct += 1

    if (ct == len(c)):
      m += 1


    n -= 1

  return m / num_experiments
