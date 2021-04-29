
tp, fp, fn, tn = [int(x) for x in input().split()]

accuracy=(tp+tn)/(tp+fp+fn+tn)
accuracy=round(accuracy,4)
print(accuracy)

precision=tp/(tp+fp)
precision=round(precision,4)
print(precision)

recall=tp/(tp+fn)
recall=round(recall,4)
print(recall)

f1=(2*precision*recall)/(precision+recall)
f1=round(f1,4)
print(f1)