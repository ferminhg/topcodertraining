class SearchZero:

	# complejidad log(n)
	def search(self, L):
		a = 0
		b = len(L) -1
		while 1:
			h = (a + b) // 2
			if L[h] == 0:
				return h
			elif L[h] > 0:
				b = h
			elif L[h] < 0:
				a = h
		return -1


sz = SearchZero()
print(sz.search([-5, -2, -1, 0, 1, 2, 4]))
print(sz.search([-5, -2, -1, 0, 1]))
print(sz.search([-5, 0, 1, 2, 4]))