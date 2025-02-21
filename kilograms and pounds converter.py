weight = input('weight = ' )
unit = input('(K)g or (L)bs = ')
if unit.upper() == 'K':
    converted = float(weight) / 0.45
    print(f'{weight}K is {converted}L')
elif unit.upper() == 'L':
    converted = float(weight) * 0.45
    print(f'{weight}L is {converted}K')
else:
    print('error try again')


