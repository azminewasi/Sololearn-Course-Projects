tp, fp, fn, tn = [int(x) for x in input().split()] 
 
total = tp + fp + fn + tn 
 
accuracy = (tp + tn)/total 
 
precision = tp/(tp + fp) 
 
recall = tp/(tp + fn)  
 
#rec=float(recall) 
#pre=float(precision) 
numerator = ( 2 * precision * recall) 
f1score = numerator / (precision + recall) 
 
accuracy = "{:.4g}".format(accuracy) 
precision = "{:.4g}".format(precision) 
recall = "{:.4g}".format(recall) 
f1score = "{:.4g}".format(f1score) 
 
print(accuracy) 
print(precision) 
print(recall) 
print(f1score)