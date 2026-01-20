bikes=['trek','mountain','hillbill','modernnoo']
#biw=bike_I_want
biw='trek'
for bike in bikes:
	if biw==bike:
		print ("yes, we have a " + biw.title())
	else:
		print ("go away")

number=16
if number >=15:
	print ('\nYes')
	
n=12
f=12
n==f

my_bike='fixie'
if my_bike not in bikes:
	print ('You are special!')
	
if biw in bikes:
	print (biw.title() + ' is available')
if biw not in bikes:
	print (biw.title() + ' is not available')
	
biw='clump'
btw='mountain'	
if biw in bikes:
	print ('\nYes, ' + biw.title() + ' is available')
if biw not in bikes:
	print ('\nNo, ' + biw.title() + ' is not available')	
	
if biw in bikes and btw in bikes:
	print ('Which one is it going to be?')
if biw in bikes or btw in bikes:
	print ('\n We have a hit! You are the owner of a new')
	if biw in bikes:
		print (biw + '!')
	if btw in bikes:
		print (btw + '!')

btw='humps'
if biw not in bikes and btw not in bikes:
	print ('\nWe need to order either the ' + biw.title() + ' or ' + btw.title() + '.')
