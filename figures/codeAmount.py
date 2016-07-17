#coding=utf8
from matplotlib import pyplot as plt

plt.figure( figsize=(12,8) )

labels = [u'JAVA', u'Python' , u'C Shape']
lines = [111, 4553, 12344]
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

plt.text(-0.67, -0.27, '1024 lines' , fontsize=11)
plt.text(0.1, 0.48, '155 lines' , fontsize=11)
plt.text(0.5, -0.1, '345 lines' , fontsize=11)
plt.show()
