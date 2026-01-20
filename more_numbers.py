for c in range(1,11):
	cube_c=(c**3)
	print(cube_c)
cube_list=[cub**3 for cub in range(1,11)]
print (cube_list)

names=['deb','tro','spl','assdf','ploo','wert']
print (names[0:2])
print (names[-3:])
print ('Worst players:')
for pl in (names[-2:]):
	print (pl.title())
		
team=(names[:])
print (team)
team.append('gpl')
names.append('okkk')
print(team)
print (names)


fav=('pota','meta','plou')
print (fav)
print(fav[0])

