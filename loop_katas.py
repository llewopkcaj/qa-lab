total = 0
for x in range(1, 101):
    total += x
print(total)
list_ = list(range(0,31,3))
print(list_)
for index, value in enumerate(list_, start=1):
    print(index, ":", value)

el = 10
while el >= 0:
    print(el)
    el -= 1
print("Boom!")

for i in range (1,101):
    if i % 7 == 0:
        print(i)
        break
else:
    print("No multiples found")




