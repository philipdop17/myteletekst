alien_0={'color':'green', 'points':5}
print (alien_0['color'])
print (alien_0 ['points'])

alien_1={'color': 'blue', 'points':15}
print (alien_1['color'])
print (alien_1 ['points'])

new_points=alien_0['points'] + alien_1 ['points']

print ('Total points:' + str(new_points))
print (alien_0)
alien_0 ['x_position']=0
alien_0 ['y_position']=25
print (alien_0)


alien_10={}
alien_10['color']='green'
alien_10 ['points']=30

print (alien_10)
print ('Color of alien_10 is: ' + alien_10['color'])

alien_10['color']='blue'

print ('color of alien_10 changed to: ' + alien_10['color'])

alien_0['speed']='fast'

print (alien_0)

print ('Originail position of alien_0 is ' + str (alien_0['x_position']))

#speed will determine new position

if alien_0['speed']=='slow':
		x_increment=1
elif alien_0['speed']=='medium':
		x_increment = 2
else:
		x_increment=3
		
alien_0['x_position']=alien_0['x_position'] + x_increment

print ('The new position for alien_o is ' + str(alien_0['x_position'] + x_increment))

	
