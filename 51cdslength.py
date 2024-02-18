#51cdslength.py by Khalid Saif

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:    #use of continue for skipping!
	for line in fp:
		if line[0] == '#': continue	#skip
		words = line.split()
		if words[2] != 'CDS': continue	#skip
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)
'''

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'#same as before
with gzip.open(path, 'rt') as fp:								 # but with nestingno continue
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] == 'CDS':
				beg = int(words[3])
				end = int(words[4])
				print(end - beg + 1)
'''