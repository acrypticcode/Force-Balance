'''
This program calculates the force vector that will balance any number of input forces entered by the user
No error-checking of user inputs is performed by this program
'''
import math

#asks user how many forces they would like to input
number_of_forces = int(input('Enter the number of forces '))
#x,y, and z represent the running total of the sum of the input vectors' x, y, and z components
#the vector <x,y,z> gives the sum of all vectors entered by the user
x=y=z=0

for i in range (number_of_forces):
    #for each input force, the program asks whether the user will enter the force in in polar or cartesian form
    entry_method = int(input(f'\nEnter 1 if you wish to enter force #{i+1} in polar form, or enter 2 for cartesian form '))
    if entry_method==1:
        #if the user chooses polar form, the program collects the magnitude and direction angles of the
        #force, then converts the force to carsesian form and adds its components to the running total
        magnitude = int(input(f'Enter the magnitude of force #{i+1} in newtons '))
        alpha = int(input(f'Enter angle alpha in degrees for force #{i+1} '))*math.pi/180
        beta = int(input(f'Enter angle beta in degrees for force #{i+1} '))*math.pi/180
        gamma = int(input(f'Enter angle gamma in degrees for force #{i+1} '))*math.pi/180
        x += magnitude * math.cos(alpha)
        y += magnitude * math.cos(beta)
        z += magnitude * math.cos(gamma)
    else:
        #if the user chooses cartesian form, the program collects the components of the force and then adds them to the running total
        x += int(input(f'Enter the x component of force #{i+1} in newtons '))
        y += int(input(f'Enter the y component of force #{i+1} in newtons '))
        z += int(input(f'Enter the z component of force #{i+1} in newtons '))
        
#finds the vector, in polar form, that is opposite to vector <x,y,z>
magnitude = math.sqrt(x**2 + y**2 + z**2)
alpha = math.acos(-x/magnitude)*180/math.pi
beta = math.acos(-y/magnitude)*180/math.pi
gamma = math.acos(-z/magnitude)*180/math.pi

#outputs the solution to the user
input(f'\nThe vector that will balance the input forces has magnitude {magnitude:.5}N and alpha, beta, and gamma angles of {alpha:.5}, {beta:.5}, and {gamma:.5}, respectively'+
      '\nPress the Enter key to exit the program')
