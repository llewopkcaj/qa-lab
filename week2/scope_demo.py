"""scope_demo.py — Demonstrates local vs global variables,
why mutating globals is bad, and why returning values is better."""

x = 11
def false(y):
    x = 10  # local x
    return x + y
print("False example:", false(5))  # 15
print("Global x after false():", x)  # still 11

x = 10

def bad_increment():
    global x
    x += 1   # mutates global x
    return x

print("Bad increment:", bad_increment())  # 11
print("Global x after bad increment:", x) # 11

def good_increment(value):
    return value + 1

x = 10
print("Good increment:", good_increment(x))  # 11
print("Global x after good increment:", x)   # still 10
# Demonstrating variable scope and mutation 

