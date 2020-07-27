print('This program will ask you for the lengths of 2 legs of a right triangle, and calculate the hypotenuse.')

# input
leg1 = float(input('Length of leg 1:'))
leg2 = float(input('Length of leg 2:'))

# process
hyp = (leg1**2 + leg2**2) ** .5

# output
print('The length of the hypotenuse is:', hyp)