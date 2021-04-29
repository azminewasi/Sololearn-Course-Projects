
Problem
Machine Learning - Split to Achieve Gain


Calculate Information Gain.

Task
Given a dataset and a split of the dataset, calculate the information gain using the gini impurity.

The first line of the input is a list of the target values in the initial dataset. The second line is the target values of the left split and the third line is the target values of the right split.

Round your result to 5 decimal places. You can use round(x, 5).

Input Format
Three lines of 1's and 0's separated by spaces

Output Format
Float (rounded to 5 decimal places)

Sample Input
1 0 1 0 1 0
1 1 1
0 0 0

Sample Output
0.5
Explanation
The initial set has 3 positive cases and 3 negative cases. Thus the gini impurity is 2*0.5*0.5=0.5.
The left set has 3 positive cases and 0 negative cases. Thus the gini impurity is 2*1*0=0.
The right set has 0 positive cases and 3 negative cases. Thus the gini impurity is 2*0*1=0.
The information gain is 0.5-0-0=0.5