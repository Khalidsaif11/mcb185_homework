#83kozak.py by Khalid Saif

import re
import sys
import gzip


file = sys.argv[1]

#def extract_protein_sequence(file):
sequences = []
with gzip.open(file, 'rt') as fp:
	for lines in fp:
		line = lines.split('\n')
		for lin in line:
			if '/translation="' in lin:
				seq = ""
				seq += lin.split('/translation="')[1]
				print(seq)