f=open("Season.csv")
t=open("Test.csv",'w')

for l in f:
	s = l+","+l[0:4]
	t.write(s)


f.close()
t.close()