#module = a file containing code you want to include in your program.
#use "import" to include a module (build-in or your own)
#useful to break up a large program reusable separate files

#print(help("modules"))

#print(help("math"))

import math

#import math as m

#module.function
print(math.pi)

#from math import pi

# >>> now no need of module name <<<
# >>> but have some problems <<<
#print (pi)

from math import e

a, b, c, d, e = 1, 2, 3, 4, 5

print (e ** a)
print (e ** b)
print (e ** c)
print (e ** d)
print (e ** e)  # here is the problem!!


