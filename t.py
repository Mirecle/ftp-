import itertools
for i in itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,./<>?;:\'\"[{]}\\|`~!@#$%^&*()_-+=', 4):
	print (''.join(i))
	