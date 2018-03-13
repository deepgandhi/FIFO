import csv

aaa=[]
bbb=[]
p=list(csv.reader(open("p.csv","r"),delimiter=","))
s=list(csv.reader(open("s.csv","r"),delimiter=","))
l=list(csv.reader(open("l.csv","r"), delimiter=","))
out=open("out.csv","w")
for i in range(len(p)):
	aaa.append([])
	aaa[i].append(p[i][0])
	aaa[i].append(p[i][1])
	aaa[i].append(int(p[i][2]))
	aaa[i].append(float(p[i][3]))
for i  in range(len(s)):
	bbb.append([])
	bbb[i].append(s[i][0])
	bbb[i].append(s[i][1])
	bbb[i].append(int(s[i][2]))
	bbb[i].append(float(s[i][3]))


def profit(l1,l2):
	aa=[]
	bb=[]
	for i in range(len(l1)):
		aa.append(int(l1[i][2]))
	for i in range(len(l2)):
		bb.append(int(l2[i][2]))
	a=0
	b=0
	i=0
	while (i<len(bb)):
		if aa[a]<bb[b]:
			sales=int(int(aa[a])*float(l2[b][3]))
			purchase=int(int(aa[a])*float(l1[a][3]))
			out.write(l1[a][0]+","+l1[a][1]+","+str(aa[a])+","+str(purchase)+","+l2[b][1]+","+str(aa[a])+","+str(sales)+","+str(sales-purchase)+"\n")
			bb[b]-=aa[a]
			a+=1
		else:
			purchase=int(int(bb[b])*float(l1[a][3]))
			sales=int(int(bb[b])*float(l2[b][3]))
			out.write(l1[a][0]+","+l1[a][1]+","+str(bb[b])+","+str(purchase)+","+l2[b][1]+","+str(bb[b])+","+str(sales)+","+str(sales-purchase)+"\n")
			aa[a]-=bb[b]
			b+=1
			i+=1
			
for a in range(len(l)):
	list1=[]
	list2=[]
	for b in range(len(p)):
		if p[b][0]==l[a][0]:
			list1.append(p[b])
	for c in range(len(s)):
		if s[c][0]==l[a][0]:
			list2.append(s[c])
	profit(list1,list2)
out.close()
			
	
