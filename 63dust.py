#63dust.py by Khalid Saif

import sys
import gzip
import mcb185
import math


input_fasta = sys.argv[1]
w = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

def shannon(a, c, g, t):
	total = a + c + g + t
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	
	entropy = 0
	if a != 0: entropy = entropy + pa * math.log2(pa)
	if c != 0: entropy = entropy + pc * math.log2(pc)
	if g != 0: entropy = entropy + pg * math.log2(pg)
	if t != 0: entropy = entropy + pt * math.log2(pt)
	return -entropy

def mask(sequence, w, entropy_threshold):
	masked_sequence = list(sequence)
	for i in range(0, len(sequence) - w +1):
		window = sequence[i:i + w]
		A = window.count('A')
		C = window.count('C')
		G = window.count('G')
		T = window.count('T')
		entropy = shannon(A, C, G, T)
		if entropy < entropy_threshold:
			for j in range(w):
				masked_sequence[i+j]= 'N'
	return ''.join(masked_sequence)


for defline, sequence in mcb185.read_fasta(input_fasta):
	print(">", defline, sep='')
	masked_seq = mask(sequence, w, entropy_threshold)
	for i in range(0, len(masked_seq), 60):
		print(masked_seq[i:i + 60])

		
#find word then mask then split

#ecoli.fa.gz = ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz
#python3 63dust.py ecoli.fa.gz 20 1.4 | head


