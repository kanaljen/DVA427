## Assignment 1
The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

The passenger information is given in a file (titanic.dat) where:

    VARIABLE DESCRIPTIONS:
        Column
        1. Class real[-1.87,0.965]
        2. Age real[-0.228,4.38]
        3. Sex real[-1.92,0.521]
        4. Survived {-1.0,1.0}

You assignment now is to create an ANN with Backpropagation as a learning algorithm. You need to use 700 cases (one case is one individual) in the validation/test and the rest in the training process.
Steps to do:

Step 1: Read the file and the last 700 cases will be the validation/test data.

Step 2: Create the ANN. You need to use sigmoid as activation function. If output is >= 0.5 then the case survived, If not, the individual died according the ANN. (You need to use this in the validation process and not in the learning process)

To calculate the error in the learning process, use 0.25 and 0.75 as a target value. Use 0.25 when the individual died and use 0.75 when the individual survived according the dataset. Ask the teacher if you have doubts about this.

Your report has to cover the key parts as follow:
1. Give the structure of your ANN.
2. Give all the weights of the trained ANN.
3. Give the equations that you used to update the weights explaining all the parameters on
them.
4. Give the percentage of correctness of the total validation data set (the last 700 cases) and
give the percentage of correctness of the cases in the validation set that survived according
to the expected value.
5. Give the percentage of survive that every individual had according to the ANN output and compare it with the expected value.

Before submitting the report, you should present this assignment first to Miguel Leon. After that, and only if everything is correct, you are able to send the report to Miguel.leonortiz@mdh.se
