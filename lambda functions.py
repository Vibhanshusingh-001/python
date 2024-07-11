# lambda function expression ki tarah hote h
# ek function ka variable bna diya aur usko as a function use kar liya
# lambda function ka use tab karna hai jab aapko one liner use karna ho(aapka kaam 1 line me ho jaaye)
#ham function ko function pass kar sakte hai
# aap function ko as a argument pass kar sakte h
# anonymous matlab jisaka naam n ho

# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))