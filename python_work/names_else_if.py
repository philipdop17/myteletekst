names=['ERIC','karen','truby','admin','darla']

if names:
	for name in names:
			if name=='admin':
				print ('Hello, ' + name.title())
			else:
				print ('What izzup ' + name.title() + '!?')

else:
	print ('We need some people!!!')

new_users=['jim', 'Karen', 'Trouble', 'truby', 'eric']

names_2=[]
for name in names:
	name=name.lower()
	names_2.append(name)
print (names_2)
print (new_users)
for new_user in new_users:
	if new_user.lower() in names_2:
		print ('Please use different name, ' + new_user)
	else:
		print (' Welcome, ' + new_user)
