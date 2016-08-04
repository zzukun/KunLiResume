#coding=utf8
from matplotlib import pyplot as plt

plt.figure( figsize=(12,8) )

# JAVA      21592
# Python  8869
# Cshape 1579
# Matlab  1783    sum 3362

Njava = 21592
Npython = 8869
Ncshape = 1579
Nmatlab = 1783


labels = [u'JAVA', u'Python' , u'C Shape' , u'Matlab']
sizes =   [ Njava , Npython , Ncshape , Nmatlab]
colors = [ '#C4E1FF' , '#84C1FF' , '#2894FF' , '#0066CC']
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
# plt.title('Program Language used in 2013-2016')

plt.text(-0.64, -0.33, str(Njava) + ' lines' , fontsize=11 )
plt.text(0.5, 0, str(Npython) + ' lines' , fontsize=11 )
plt.text(0.24, 0.63, str(Ncshape) + ' lines' , fontsize=11 )
plt.text(0, 0.7 , str(Nmatlab) + ' lines' , fontsize=11 )
plt.show()
