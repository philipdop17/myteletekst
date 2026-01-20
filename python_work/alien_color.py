alien_color= 'green'
if alien_color == 'green':
	print ('You earned 5 points')
if alien_color != 'green':
	print ('no points')
alien_color = 'red'

if alien_color == 'green':
	print(' 5 points')
else:
	print(' 10 points')

if alien_color == 'green':
	print ('10 points')
	
elif alien_color == 'yellow':
	print ('10 points')

else:
	print ('15 points')

age=1


if age<2:
	print ('You are a baby')
elif age<4:
	print ('You are a toddler')
elif age<13:
	print ('You are a kid')
elif age<20:
	print ('You are a teenager')
elif age<65:
	print ('You are an adult')
else:
	print('You are an elder')
	
fav_fruit=['orange', 'apple', 'banana']
a = 'banana'
if a in fav_fruit:
	print ('You really like ' + a + 's!!!')

if 'orange' in fav_fruit:
	print ('You really like oranges!!!')
if 'pear' in fav_fruit:
	    print ('You really like oranges!!!')
	else:
		print ('You have no taste')
