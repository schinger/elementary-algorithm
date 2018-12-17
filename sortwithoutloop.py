#sort only by recursion, without loop.
def recurseSort(list):
	def insertOne(list,a):
		if a>=list[len(list)-1]:
			list.append(a)
			return list
		if a<list[0]:
			list.insert(0,a)
			return list
		if len(list)>1:
			return [list[0]]+insertOne(list[1:],a)
	n=len(list)
	if n==1:
		return list
	else:
		list[0:n-1]=recurseSort(list[0:n-1])
		list=insertOne(list[0:n-1],list[n-1])
		return list
