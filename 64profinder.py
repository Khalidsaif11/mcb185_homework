#64profinder.py by Khalid Saif (function below from Abhi Sharma)

import sys
import mcb185
import gzip
import dogma


input_fasta = sys.argv[1]
protein_min_length = int(sys.argv[2])


def find_orfs(dna_sequence, mini):						#orf=open reading frame
	translated_sequences = []
	for orf in dogma.translate(dna_sequence).split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= mini:
				translated_sequences.append(protein)
	return translated_sequences



for defline, seq in mcb185.read_fasta(input_fasta):
	words = defline.split()
	name = words[0]
	reverse = dogma.revcomp(seq)
	identifier = 0
	for frame in range(3):
		for protein in find_orfs(seq[frame:], protein_min_length):
			identifier += 1
			print(f'>{name}-proto-{identifier}')
			print(protein)
		for revprotein in find_orfs(reverse[frame:], protein_min_length):
			identifier += 1
			print(f'>{name}-proto-{identifier}')
			print(revprotein)