kid_1={'color':'blue', 'age': 13}
kid_2={'color': 'orange', 'age': 12}
kid_3={'color': 'green', 'age' : 9}

kids=[kid_1, kid_2, kid_3]
for kid in kids:
	print (kid)
	
#make an empty list for aliens
aliens=[]

for alien_number in range(30):
	new_alien={'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print (alien)

print ("show number of aliens: " + str(len(aliens)))

for alien in aliens [:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['points'] = 10
		alien['speed']= 'medium'
		
for alien in aliens[:10]:
	print (alien)
	



