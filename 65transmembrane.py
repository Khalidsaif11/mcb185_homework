#65transmembrane.py by Khalid Saif

#soft linked ecoliprot.faa.gz

import sys
import mcb185
import gzip

input_fasta = sys.argv[1]		#polypeptide seq


def kd_values(aa):
	if aa == 'A':
		return 1.8
	elif aa == 'R':
		return -4.5
	elif aa == 'N':
		return -3.5
	elif aa == 'D':
		return -3.5
	elif aa == 'C':
		return 2.5
	elif aa == 'Q':
		return -3.5
	elif aa == 'E':
		return -3.5
	elif aa == 'G':
		return -0.4
	elif aa == 'H':
		return -3.2
	elif aa == 'I':
		return 4.5
	elif aa == 'L':
		return 3.8
	elif aa == 'K':
		return -3.9
	elif aa == 'M':
		return 1.9
	elif aa == 'F':
		return 2.8
	elif aa == 'P':
		return -1.6
	elif aa == 'S':
		return -0.8
	elif aa == 'T':
		return -0.7
	elif aa == 'W':
		return -0.9
	elif aa == 'Y':
		return -1.3
	elif aa == 'V':
		return 4.2
	else:
		return 0



def average_kd(sequence, window_size):
	tot_kd_values = []
	for i in range(len(sequence) - window_size + 1):
		window = sequence[i:i + window_size]
		kd_sum = 0
		for aa in window:
			kd_sum += kd_values(aa)
		tot_kd_values.append(kd_sum / window_size)
	return tot_kd_values

def hydrophobic_alphahelix(seq, window, threshold):
	kd_values_list = average_kd(seq, window)
	for i, kd in enumerate(kd_values_list):
		if kd >= threshold and 'P' not in seq[i:i+window]:
			return True
		else: 
			False

for defline, seq in mcb185.read_fasta(input_fasta):
	signal = hydrophobic_alphahelix(seq[:30], 8, 2.5)
	trans = hydrophobic_alphahelix(seq[30:], 11, 2.0)
	if signal and trans:
		print(defline)