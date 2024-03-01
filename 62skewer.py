#62skewer.py by Khalid Saif Coauthored with Ethan & George & Jordon

import sys
import mcb185



w = int(sys.argv[2])
genome = sys.argv[1]


for defline, sequence in mcb185.read_fasta(genome):
	initial_window = sequence[0:w]
	G_count = initial_window.count('G')
	C_count = initial_window.count('C')
	for i in range(len(sequence) - w):
		drop = sequence[i]
		pick = sequence[i+w]
		if drop == 'G': G_count -= 1
		elif drop == 'C': C_count -= 1
		if pick == 'G': G_count += 1
		elif pick == 'C': C_count += 1
		
		gc_comp = (G_count + C_count) / w
		if G_count + C_count != 0:
			gc_skew = (G_count - C_count) / (G_count + C_count)
		else:
			gc_skew = 0
		print(f'{i}\t{gc_comp:.3f}\t{gc_skew:.3f}')
		
		
'''
for size 10
real    1m36.543s
user    1m0.140s
sys     0m30.046s

for size 1000
real    3m10.204s
user    2m7.593s
sys     0m57.796s

ecoli.fa.gz = ../MCB185/data/GCF_000005845.2_ASM584v2_
		genomic.fna.gz ecoli.fa.gz
gunzip -c ../MCB185/data/GCF_000005845.2_ASM584v2_
		genomic.fna.gz | head > miniecoli.fa
'''