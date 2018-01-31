## Assignment 2
Classification of Irsi data is a well known benchmark problem in machine learning research.
This data set is downloadable from ftp.ics.uci.edu/pub/machine-learning-databases.The
problem in Iris data is to classify three species of iris (setosa, versicolor and virginica) by
four-dimensional attribute vectors consisting of sepal length (x1), sepal width (x2), petal length
(x3) and petal width (x4). There are 50 samples of each class in this data set.
 We now consider a fuzzy classifier with a set of fuzzy rules to classify Iris data. The values
of attributes are normalized before fuzzy processing according to
max( ) min( )
min( ) ' i i
x i
x i
i 

where max(i) and min(i) denote the maximum and minimum values of attribute xi
respectively. Every attribute of the fuzzy classifier is assigned with three linguistic terms
(fuzzy sets): short, middle and long. With normalized attribute values, the membership
functions of these fuzzy sets for all the four attributes are depicted in the figure below
(assume the membership functions for different attributes are identical).

0 0.6 1.0
1.0
short middle long
 Fig. The membership functions of the attributes for Iris problem
 Further we suppose that the following set of fuzzy rules have been defined by experts to
classify iris data. The membership functions used by these rules are those depicted in the
figure above.
r1: If (x1=short ? long) and (x2=middle ? long) and (x3=middle ? long ) and (x4=middle)
 Then iris versicolor
r2: If (x3=short ? middle) and (x4=short) Then iris setosa
r3: If (x2=short ? middle) and (x3=long) and (x4=long) Then iris virginica
r4: If (x1=middle) and (x2=short ? middle) and (x3=short) and (x4=long)
Then iris versicolor
Your assignment now is to implement this fuzzy classifier in a computer program, and
you have to then apply your program to classify all the iris data and examine the classification
accuracy of your fuzzy system.
Your report has to cover the key parts as follows:
1. What is the AND operator in your implementation?
2. What is the OR operator in your implementation? 
3. What is the data flow from inputs to decision given the normalized attribute values as
(0.3, 0.8, 0.2, 0.7)? You have to make fuzzy reasoning with hand at this stage. This is
a preparation stage to help you make sure that you understand the whole fuzzy
reasoning procedure. As long as you truly understand, you will find implementation
with programming easy and enjoyable.
4. What is the accuracy of your implemented fuzzy classifier on the Iris data? 