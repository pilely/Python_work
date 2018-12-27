guests = ['A', 'B', 'C', 'D']
message = "I want to invita " + str(guests)
print(message)
busy = 'A'
guests.remove(busy)
print(busy  + " can not come!")
guests.append('E')
print("New list " + str(guests))
print(guests[0] + " Welcome!")
print(guests[1] + " Welcome!")
print(guests[2] + " Welcome!")
print(guests[3] + " Welcome!")

guests.insert(0, 'F')
guests.insert(3, 'G')
guests.append('H')
print(guests)

poped = guests.pop()
print(poped + " Sorry!")
poped = guests.pop()
print(poped + " Sorry!")
poped = guests.pop()
print(poped + " Sorry!")
poped = guests.pop()
print(poped + " Sorry!")
poped = guests.pop()
print(poped + " Sorry!")

print(guests[0] + " Have fun")
print(guests[1] + " Have fun")

print(guests)
del guests[0]
del guests[0]
print(guests)
print("The list is emptyed!")
