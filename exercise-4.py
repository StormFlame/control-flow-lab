print('Enter the lengths of three side of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

sides = [a, b, c]

matching_sides = 0
for side in sides:
    sides.remove(side)
    for s in sides:
        if(s == side):
            matching_sides += 1
    sides.insert(0, side)

type_of_triangle = ''

if matching_sides == 6:
    type_of_triangle = 'equalateral'
elif matching_sides == 2:
    type_of_triangle = 'isosceles'
else:
    type_of_triangle = 'scalene'
    
print(f'A triangle with sides of {a}, {b} & {c} is a {type_of_triangle} triangle')