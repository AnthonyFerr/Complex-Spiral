import cartesius.main as cartesius
import cartesius.elements as elements
import cartesius.charts as charts
import sys

points = []

class complex:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def add(num1, num2):
    rsum = num1.real + num2.real
    isum = num1.imaginary + num2.imaginary
    print("{}, {}i".format(rsum, isum))
  
  def subtract(num1, num2):
    rminus = num1.real - num2.real
    iminus = num1.imaginary - num2.imaginary
    print(rminus, iminus)

  def multiply(num1, num2):
    iterm = (num1.real * num2.imaginary) + (num1.imaginary * num2.real)
    rterm = (num1.real * num2.real) - (num1.imaginary * num2.imaginary)
    return(rterm, iterm)

c1 = complex(3, 5)
c2 = complex(4, 2)
c1.multiply(c2)


z = complex(2, 3)
factor = complex(6, -15)
z.multiply(factor)

initr = 2
initi = 3

"""
n = 1
for i in range(15):
  product = complex(initr, initi).multiply(complex(n, n))
  print(product)
  n += 1
  initr = product[0]
  initi = product[1]"""

def xplane():
    global initr
    global initi
    global n
    coordinate_system = cartesius.CoordinateSystem(bounds=(-30000, 30000, -30000, 30000))
    coordinate_system.add(elements.Point((c1.real, c1.imaginary), style='o'))
    coordinate_system.add(elements.Point((c2.real, c2.imaginary), style='o'))
    coordinate_system.add(elements.Point((c1.multiply(c2)), style='o'))
    for i in range(15):
      #product = complex(1, 1).multiply(complex(1, i))
      product = complex(initr, initi).multiply(complex(2, 2))
      print(product)
      initr = product[0]
      initi = product[1]
      coordinate_system.add(elements.Point((product), style='x', label=("XXXXX{}, {}XXXXX ".format(initr, initi)), color="red"))
    return coordinate_system.draw(12000, 8000), coordinate_system.draw(1200, 800, antialiasing=True)
points.append(xplane)

args = sys.argv[1:]

for i, function in enumerate(points):
    images = function()
    print('Processing %s' % function)

    if not isinstance(images, tuple) and not isinstance(images, list):
        images = [images]

    for j, image in enumerate(images):
        image_name = 'graph-{0}-{1}.png'.format(i, j)
        image.save(image_name)
        print('written:', image_name)