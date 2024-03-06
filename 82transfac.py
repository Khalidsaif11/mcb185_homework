#82transfac.py by Khalid Saif

import re
import json
import gzip


pwm_records = []	#list to store dicts for each record

with gzip.open('transfac.gz', 'rt') as fp:
	current_record = {}						#dict to store current record
	for line in fp:
		lines = line.rstrip('\n')			#rm newline space
		if not lines:
			continue

		if lines.startswith('ID'):
			if current_record:				#start of new record
				pwm_records.append(current_record)
			current_record = {'id': lines.split()[1], 'pwm': []}

		elif lines.startswith('PO'):
			header = lines.split()[1:]

		elif lines.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
			values = []
			for val in lines.split()[1:]:
				values.append(float(val))
			pwm_dict = {}					#to match values with their bases
			for i in range(len(header)):
				pwm_dict[header[i]] = values[i]
			current_record['pwm'].append(pwm_dict)

if current_record:							#append last record
	pwm_records.append(current_record)

json_output = json.dumps(pwm_records, indent=2)
print(json_output)