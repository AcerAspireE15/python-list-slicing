numbers = [0, 100, 200, 300, 400, 500, 600]
print(numbers[2:5])
print(numbers[2:6])
print(numbers[4:6])
print(numbers[:6])
print(numbers[:3])
print(numbers[2:])
print(numbers[1:6])
print(numbers[1:6:2])
print(numbers[1:6:3])

list = [x**2 for x in range(5)]
print(list)

list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)