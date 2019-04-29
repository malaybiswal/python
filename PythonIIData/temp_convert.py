"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results. 
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

def fahrenheit_to_centigrade(*xtmp):
	print(type(xtmp), xtmp)
	for x in xtmp:
		if(isinstance(x,(int,float))):
			#print(x)
			nutmp=float((5.0/9.0)*(x - 32))
			print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(x, nutmp))
		else:
			print('Only int,float allowed, but you entered',x)
    

#temp = 72.0
fahrenheit_to_centigrade('str',12,24,56,True,False)
    

