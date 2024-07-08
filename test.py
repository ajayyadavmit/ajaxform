class University(object):
    name = "tribhuwan"
    headquater = "kirtipur"

    def __init__(self, roll, salary) -> None:
        self.roll = roll
        self.salary = salary

    @classmethod
    def name_university(cls, name, location):
        cls.name = name
        cls.headquater = location
        return None

    @staticmethod
    def age_valid(age):
        if age > 16:
            return True
        else:
            return False


u1 = University(56, 456000)
print(type(u1.age_valid(15)))
print(University.name, University.headquater)
University.name_university("Yadav", "janakpur")
print(University.name, University.headquater)


def value_add(x):
    def three(y, z):
        return x+y+z
    return three


m = value_add(5)
print(value_add(6), type(value_add))
print(m(4, 6))


def decoration(fns):
    print("Before FNS Call")

    def wrapper(*args):
        fns(*args)
        print("After fns")
        return fns
    return wrapper


# @decoration
def two_add(m, n):
    return m+n


two_add = decoration(two_add(4, 2))
print(two_add)

l = [4, 56, 4]
print(type(l))


def abc():
    yield "akna"
    yield "dkdk"


print(type(abc), abc(), abc(), dir(abc))
m = abc()
print(type(m), dir(m))
print(dir(l))

print([2*i for i in l])
d = {'name': "ajay", "loc": "ktm", "age": 45}

print({x: x**2 for x in range(1, 6)})
age = 54

print([[4, 3, 4, 5, 6] if age > 16 else "Less"])
print({x for x in "aabbavcddda"})

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = (list(filter(lambda x: x % 2 == 0, numbers)))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


def new():
    ''' this is documentation'''
    a = 45
    b = 3234
    return a


print(University.__dict__)


def gen():
    yield "abc"
    yield 5
    yield 8
    return "hi"


g = gen()
print(next(g))
print(next(g))


def a(x): return x*x


print(a(5))

print(list([lambda x: x*x for x in [4, 5, 6]]))

l1 = [lambda x: x*x for x in [4, 5, 6]]

# Create a list of lambda functions
lambdas = [lambda x=x: x*x for x in [4, 5, 6]]

# Call each lambda function and print the result
print([f(8) for f in l1])


print([f() for f in  [lambda x=x: x*x for x in [4, 5, 6]]])


# Create a list of lambda functions for both x + y and x - y
lambdas = [(lambda x=x, y=y: x + y, lambda x=x, y=y: x - y) for x in [4, 5, 6] for y in [9, 11, 44]]

# Evaluate and print the results
results = [(f1(), f2()) for f1, f2 in lambdas]
print(results)

c = (lambda a=4, b=6 :(( a+b), (a-b)))()
print(c)


def gen():
    yield "abc"
    yield 5
    yield 8
    return "hi"


g = gen()
print(next(g))
print(next(g))
print(next(g))

print(next(g))


