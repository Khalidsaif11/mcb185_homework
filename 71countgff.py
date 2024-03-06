#71countgff.py by Khalid Saif

import sys
import gzip



count = {}
with gzip.open(sys.argv[1], 'rt') as fp:			#gives features
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
#for f, n in count.items(): print(f, n)

for k in sorted(count): print(k, count[k])			#sorted


'''													#otherway!
if feature not in count: count[feature] = 1
else:                    count[feature] += 1


python3 71countgff.py ecoli.gff.gz | sort				#sort alphabet
python3 71countgff.py ecoli.gff.gz | sort -n -k 2		#sort numerically column 2
python3 71countgff.py ecoli.gff.gz | sort -nk2


#GCF_000005845.2_ASM584v2_genomic.fna.gz (seq)
#GCF_000005845.2_ASM584v2_genomic.gff.gz (features)
#GCF_000005845.2_ASM584v2_protein.faa.gz (polypeptide)
'''