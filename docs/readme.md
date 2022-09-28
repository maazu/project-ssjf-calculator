# Project SSJF Documentation

## User Input

User inputs has been integrated in way as the user execute the program, the following argumnets can be supplied by the user:

--testnumber can be any number or location of the the file if the number is too big and needs to be read from a file (only applicable in step2,step3,step4,step5)

--numberone can be any number or location of the the file if the number is too big and needs to be read from a file

--numbertwo can be any number or location of the the file if the number is too big and needs to be read from a file

--showoutput will print the result of the computing operation on a screen.

--savefile will save the result of the computed operation in a txt file. This file is saved in results directory and computed result can be found under the calutated operation name directory.

Optional arguments --showoutput and --savefile are optional arguments

## Computing Mod Limits or Step 2

User inputs either one or a group of numbers called mod limits. For example, user will use a mod limit of 0,3,7.

If we mod the TN and if it returns any of those 3 values, we stop the process and return what we mod by to get those values as the answer.

In the programme the execution of the loop begins from 1, in the following way:

testnumber mod 1 = 0

since calculated mod is available in a list we stop the execution and return 1

else we keep the loop running until we fulfil the condition.

testnumber mod 2 = 1

testnumber mod 3 = 1

...

## Step 2 Execution

--testnumber can be any number or location of the the file if the number is too big and needs to be read from a file (only applicable in step2,step3,step4,step5)

--displayout will print the result of the computing operation on a screen.

--savefile will save the result of the computed operation in a txt file. This file is saved in results directory and computed result can be found under the calutated
operation name directory.

```
python3 step2.py --testnumber 937  --modlimit ../data/modlimits/modlimitTest.txt --displayoutput False --savefile False
```
