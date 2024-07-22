# Force Balance Project
Author: Curran Flanders

Course: ENGR-211

Completion Date: 09/16/2022

## Introduction and contents
This document is a brief engineering report describing a piece of computer software that was created as a class assignment. 
The report contains a problem statement and sample output from the program.

## Problem statement 
There is a need for a computer program that, when given any number of three-dimensional force vectors, can calculate the 
force vector that is equal and opposite to the sum of the given forces. The user must be allowed to input each force in 
either polar form (a magnitude and three angles) or cartesian form (x, y, and z coordinates).

## Variable list 

•	number_of_forces (int): Contains the total number of forces that the user wishes to enter.

•	entry_method (int): Contains the integer “1” if the user wants to input a force in polar form or “2” if the user instead wants to input the force in cartesian form.

•	magnitude (int): Contains the magnitude of a force vector in polar form.

•	alpha (float): Contains the angle made between a vector in polar form and the x-axis.

•	beta (float): Contains the angle made between a vector in polar form and the y-axis.

•	gamma (float): Contains the angle made between a vector in polar form and the z-axis.

•	x (int or float): Contains a running total of the sum of the x-components of all vectors entered by the user.

•	y (int or float): Contains a running total of the sum of the y-components of all vectors entered by the user.

•	z (int or float): Contains a running total of the sum of the z-components of all vectors entered by the user.

