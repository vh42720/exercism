def distance(strand_a, strand_b):
	# Raise error if strand lengths are different
	if len(strand_a) != len(strand_b):
		raise ValueError('Different length for strands')
	else:
		return sum([a != b for a, b in zip(strand_a, strand_b)])
