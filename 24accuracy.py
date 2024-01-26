# 24accuracy.py by Khalid Saif Co-authored with Ethan Djou


def accuracy_f1(tp, fp, tn, fn):				#accuracy and F1 score
	accuracy  = (tp + tn)/ (tp + fp + tn + fn)
	precision = tp / (tp + fp)
	recall	  = tp / (tp + fn)
	f1_score  = 2 * (precision * recall) / (precision + recall)
	assert(tp + fp + tn + fn > 0)
	assert(precision + recall > 0)
	assert(tp + fp > 0)
	return accuracy, f1_score

# Testing the formula
print(accuracy_f1(2, 55, 35, 62))
print(accuracy_f1(13, 89, 87, 2))
print(accuracy_f1(5, 33, 78, 99))
print(accuracy_f1(5, -5, 3, 4))					#check denominator equal zero error 