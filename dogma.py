#library for central dogma by Khalid Saif

def transcribe(dna):						#replaces T with U in TXN
	return dna.replace('T', 'U')


def revcomp(dna):							#reverse complement
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else          : rc.append('N')
	return ''.join(rc)						#joins list ot make string


'''
def translate(dna):							#translation
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'TTT' or codon == 'TTC':
			aas.append('F')
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT':
			aas.append('L')
		elif codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
			aas.append('L')
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA':
			aas.append('S')
		elif codon == 'TCG' or codon == 'AGT' or codon == 'AGC':
			aas.append('S')
		elif codon == 'TAT' or codon == 'TAC':
			aas.append('Y')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			aas.append('*')
		elif codon == 'TGT' or codon == 'TGC':
			aas.append('C')
		elif codon == 'TGG':
			aas.append('W')
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
			aas.append('P')
		elif codon == 'CAT' or codon == 'CAC':
			aas.append('H')
		elif codon == 'CAA' or codon == 'CAG':
			aas.append('Q')
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA':
			aas.append('R')
		elif codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
			aas.append('R')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
			aas.append('I')
		elif codon == 'ATG':
			aas.append('M')
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
			aas.append('T')
		elif codon == 'AAT' or codon == 'AAC':
			aas.append('N')
		elif codon == 'AAA' or codon == 'AAG':
			aas.append('K')
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
			aas.append('V')
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
			aas.append('A')
		elif codon == 'GAT' or codon == 'GAC':
			aas.append('D')
		elif codon == 'GAA' or codon == 'GAG':
			aas.append('E')
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
			aas.append('G')
		else:
			aas.append('X')
	return ''.join(aas)
'''
'''
def translate(dna):							#another way!
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)

											#another way cononical
w = 3 #window size
s = 3 #step size
for i in range(0, len(seq) -w +1, s):		#len(seq) -w +1 prevent runoff
	subseq = seq[i:i+w]
'''
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):						#translate function
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)


kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}

def hydropathy(seq):				#hydropathy function
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)


def gc_comp(seq):					#gc comp function
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):					#gc skew function
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)