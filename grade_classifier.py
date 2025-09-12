num_num = int(input("Enter a number 0-100"))
if num_num >= 80 and num_num <= 100:
    print("A")
elif num_num >= 60 and num_num < 80:
    print("B")
elif num_num >= 40 and num_num < 60:
    print("C")
elif num_num >= 20 and num_num < 40:
    print("D")  
elif num_num >= 0 and num_num < 20:
    print("F")
else:
    print("Invalid number (out of range)")  