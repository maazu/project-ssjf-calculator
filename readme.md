# Project SSJF

Maximmum Digits in a number => one hundred billion: 100,00,00,00,000 / 100000000000

## Getting Started

To execute this programme you will need python 3.9 or greater

### Operations

#### Arguments

--testnumber can be any number or location of the the file if the number is too big and needs to be read from a file (only applicable in step2,step3,step4,step5)

--numberone can be any number or location of the the file if the number is too big and needs to be read from a file

--numbertwo can be any number or location of the the file if the number is too big and needs to be read from a file

--displayout will print the result of the computing operation on a screen.

--savefile will save the result of the computed operation in a txt file. This file is saved in results directory and computed result can be found under the calutated operation name directory.

### Add

```
 python3 add.py --numberone 11 --numbertwo ../data/hundred-long/624-char.txt --showoutput True --savefile True
```

### Subtract

```
 python3 subtract.py --numberone 11 --numbertwo ../data/hundred-long/624-char.txt  --showoutput True --savefile True
```

### Division

```
 python3 divide.py --numberone 11 --numbertwo ../data/hundred-long/624-char.txt  --showoutput True --savefile True
```

### exponent

```
 python3 exponent.py --numberone 11 --showoutput True --savefile True
```

### squareroot

```
 python3 exponent.py --numberone 11 --showoutput True --savefile True
```

## Checking the Steps 2

```
python3 step2.py --testnumber 937  --modlimit ../data/modlimits/modlimitTest.txt --showoutput False --savefile False
```

## Checking the Steps 3

```
python3 step2.py --testnumber 937 --showoutput False --savefile False
```

## Checking the Steps 4

```
python3 step4.py --testnumber ../data/hundred-long/624-char.txt --modnumber 36 --showoutput True
```
