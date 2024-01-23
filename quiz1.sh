Khalid Saif Khalidsaif11			#co authered with Natael

#Task 3

gunzip dictionary.gz | grep a | grep -E "^[mcuotfa]{4,}$"
gunzip dictionary.gz | grep b | grep -E "^[trnliab]{4,}$"
gunzip dictionary.gz | grep c | grep -E "^[amdinoac]{4,}$"
gunzip dictionary.gz | grep z | grep -E "^[naigroz]{4,}$"

#task 4

gunzip -c jaspar2024_core.transfac.gz | grep tax | cut -d ":" -f 2 | sort