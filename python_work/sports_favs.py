fav_sports={
	'Viv':['basketball', 'soccer'],
	'Ava': ['basketball'],
	'Sully': ['Soccer', 'Basketball', 'wrestling']
	}

for name, sports in fav_sports.items():
	print ("\t The favorite sports of " + name.title() + " are:")
	for sport in sports:
		print (sport)
		
