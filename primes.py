import math

def isprime(p):
	for i in range(2,p):
		if p % i == 0:
			return False
	return True


def find_primes(numPrimes):
	ps = []
	i = 2
	while( len(ps) < numPrimes ):
		if isprime(i):
			ps.append(i)
		i = i + 1	
	return ps

class ModifiedSieveOfEratosthenes(object):

	ns = []

	def find_primes_below(self, maxNum):
		i = 2
		self.ns = self.ns + list(range(len(self.ns),maxNum))
		while i < int(math.sqrt(len(self.ns))):
			n = self.ns[i]
			if n == 0:
				i = i + 1
				continue
			for k in range(2*i,maxNum,i):
				self.ns[k] = 0
			i = i + 1
		return list(filter(lambda x: x > 1, self.ns))

def find_primes2(numPrimes):
	s = Sieve()
	n = numPrimes	
	ps = []
	while(len(ps) < numPrimes):
		ps = s.find_primes_below(n)
		n = n*2
	return ps[:numPrimes]

# with Timer('find_primes'):
# 	ps = find_primes(5000)
# print(ps)

def reference_primes():
	with open('primes1.txt','r') as f:
		lines = f.readlines()[1:]
		reference_ps = []
		for line in lines:
			s = filter(lambda x : x, [x.strip() for x in line.split(' ')])
			reference_ps.extend([int(x) for x in s])
	return reference_ps

# print(reference_ps)
#
# with Timer('find_primes2'):
# 	ps = find_primes2(1000000)
# print(ps)
# print(reference_ps[0:1000000] == ps)
