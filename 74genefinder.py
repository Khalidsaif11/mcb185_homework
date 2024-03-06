#74genefinder.py by Khalid Saif


import sys
import mcb185
import dogma



start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']
minorf = int(sys.argv[2])

def find_orfs(seq, frame, strand):
	orfs = []
	i = 0
	while i < len(seq):
		codon = seq[i:i+3]
		if codon != start_codon:
			i += 3
			continue
			
		start = i					#record start position of ORF
		
		for j in range(i, len(seq) - 2, 3):
			codon = seq[j:j+3]		#move to nxt codon in seq
			if codon in stop_codons:
				stop = j + 2			#record position of stop codon
				if (stop - start) >= minorf:
					if strand == '+':
						orfs.append((start + 1 + frame, stop + 3 + frame -2, strand))
					else:
						orfs.append((len(seq) - stop, len(seq) - start, strand))
				i = j
				break
		i += 3		#move to next codon triplets
	return orfs

def format_output(defline, start, end, strand):
		return f'{defline}\tRefSeq\tregion\t{start}\t{end}\t.\t{strand}'
				
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for frame in range(3):
		print(f'frame\t{frame}')
		print()
		identifier = defline.split()[0]
		orfs_pos_strand = find_orfs(seq[frame:], frame, '+')
		orfs_neg_strand = find_orfs(dogma.revcomp(seq)[frame:], frame, '-')
		
		for start, end, strand in orfs_pos_strand:		#pos strand coordinates from list
			print(format_output(identifier, start, end, strand))
		for start, end, strand in orfs_neg_strand:		#neg strand coordinates from list
			print(format_output(identifier, start, end, strand))