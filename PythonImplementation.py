import math

def SortedInsertion(A, a):
	for i in range(len(A)):
		if(a < A[i]):
			B = A[0:i]+[a]+A[i:]
			return B
	A.appned(a)

def LogSort(A):
	B = dict()
	for a in A:
		try:
			B[int(math.log(a, 10))] = SortedInsertion(B[int(math.log(a, 10))], a)
		except KeyError:
			B[int(math.log(a, 10))] = [a]

	buckets = list(B.keys())
	buckets.sort()
	C = []
	for b in buckets:
		C += B[b]
	return C
