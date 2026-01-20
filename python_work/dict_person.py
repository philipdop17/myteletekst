person_a={
	'first_name':'karen',
	'last_name': 'dop',
	'age': '46',
	'city':'chicago',
	}
print (person_a ['first_name'].title() + "  " +
    person_a ['last_name'].title() +
    "\n" +  person_a ['age']+
    person_a ['city'].title()
    )
    
fav_num={
	'JIm': '7',
	'jen': '9',
	'jon': '16',
	'jeff': '99',
	}

print ("Jim's favorite number is: " + fav_num['JIm']+
	"\n" + "jen's favorite number is: " + fav_num['jen']+
	"\n" + "jon's favorite number is: " + fav_num['jon']+
	"\n" + "jeff's favorite number is: " + fav_num['jeff']
	)

learned_words={
	'print':'show output in a screen',
	'dict':' a list with key pairs',
	'list':' a holder with elements ',
	}

print ( "What is learned is: ",
	"\n" + "print means: " + learned_words['print'] +
	"\n" + "dictionary means: " + learned_words['dict'] +
	"\n" + "list means: " + learned_words['list'] 
	)
	
for k, v in learned_words.items():
	print (k,v)
for a, b in learned_words.items():
	print ("learned: " + a.title())
	print ("what it is: " + b.title())
	
	


		
