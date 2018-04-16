import itertools
for i in itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz1234567890', 4):
	print (''.join(i))
	