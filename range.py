for value in range(1, 6):
    print(value)

number = list(range(1, 9))
print(number)

number_2 = list(range(1, 11, 2))
print(number_2)

squares = []
for value in range(1, 8):
	squares.append(value ** 2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

square = [value * 2 for value in range(1, 5)]
print(square)
