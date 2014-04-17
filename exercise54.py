# This is where Exercise 5.4 goes
# Name: Cait

a = int(input('Enter 1st side length to check if real triangle: '))
b = int(input('Enter 2nd side length to check if real triangle: '))
c = int(input('Enter 3rd side length to check if real triangle: '))

def is_triangle(a, b, c):
	if a > b + c:
		print 'No'
	elif b > a + c:
		print 'No'
	elif c > a + b:
		print 'No'
	else:
		print 'Yes'	

is_triangle(a, b, c)		