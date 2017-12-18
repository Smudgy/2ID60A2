def hi(n):
    print('Hi ' + girls[n] + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Alina', 'You']
for i in range(len(girls)):
    hi(i)
    if i < len(girls) - 1:
        print('Next girl')
