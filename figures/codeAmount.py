#coding=utf8
from matplotlib import pyplot as plt

plt.figure( figsize=(6,9) )

labels = [u'Part1', u'Part2' , u'Part3']
sizes =   [ 60 , 30 , 10]
colors = [ 'red' , 'yellowgreen' , 'lightskyblue']

# explode = (0.05 , 0 , 0)

patched, l_text, p_text = plt.pie(sizes,
			labels = labels,
			colors = colors,
			labeldistance = 1.1,
			autopct = '%3.1f%%',
			shadow = False,
			startangle = 90,
			pctdistance = 0.6)

for t in l_text:
	t.set_size = (30)
for t in p_text:
	t.set_size = (20)

plt.axis('equal')
plt.legend()
plt.show()