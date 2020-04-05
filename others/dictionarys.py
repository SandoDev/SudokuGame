memory = {
    '8':[0,8],
    '2':[4,9]
}

memory.update()

print(memory.get('2'))
print(memory['8'])

obj_d = memory

number = 2

for values in memory[str(number)]:
    print(values)


mas = memory.copy()

asdf = {}

mas.update(asdf)

shall = memory.copy()
print(memory.clear())


print(shall)

other = shall.pop('2')

print(other)


print(shall.keys())
print(shall.values())
print(mas.items())
print("masssss::::::::       ",mas)
print(mas.popitem())


#----------------------------

memoria = {'1':[],
'2':[],
'3':[],
'4':[],
'5':[],
'6':[],
'7':[],
'8':[],
'9':[]}

number = 5
columna = 3

memoria[str(number)].append(columna)
memoria[str(number)].append(columna+1)

print(memoria)
