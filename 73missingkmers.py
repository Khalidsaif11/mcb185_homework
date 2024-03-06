#73missingkmers.py by Khalid Saif

import sys
import mcb185
import itertools
import dogma

#seq = 'ACGTATATGTCACGTAG' #14


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	reverse_seq = dogma.revcomp(seq)
	for k in range(1, len(seq)):
		print(k)
		kcount = {}
		missing_kmers_found = False
		
		for i in range(len(seq) - k + 1):	#positive strand
			kmer = seq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		#for a, n in kcount.items(): print(a, n)
		
		for i in range(len(reverse_seq) - k + 1): #neg strand
			kmer = reverse_seq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
			
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount:
				print(kmer, k, 0)
				missing_kmers_found = True
		if missing_kmers_found:
			break