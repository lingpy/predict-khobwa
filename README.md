# Prediction experiment for missing words in Kho-Bwa language data

## Introduction

This is an experiment on prediction of words that have so far not been observed in field work. The basic idea is: with an existing dataset of cognate words, we can use the correspondence pattern detection algorithm to infer for those words in a given language that does not show a reflex in a given cognate set, how they would sound if they were cognate. Since Tim Bodt, who did field work on the Kho-Bwa languages, in fact dit not elicit all words during his initial field work on eight varieties of Kho-Bwa, we can now use the existing dataset to predict how potential cognates would have sounded, and if Tim Bodt goes back to field work in October, he can try to elicit those words and see how well the prediction algorithm works. 

## Installation and Running the code

To install the source code of this package, you need lingpy, sinopy, and lingrex, three Python libraries.

You can install them with help of PIP, provided you have a fresh Python3 installation on your computer:

```shell
$ pip install -r pip-requirements.txt
```
To run the code, simply type:

```shell
$ python predict.py
```

The output will be written to the file `predictions.tsv`.

## Testing the Predictions During Field Work

To verify the predictions, Tim Bodt will proceed as follows:

1. During fieldwork, he will try to elicit as many of the potentially missing cognate sets as follows, but it is unlikely that he will be able to elicit them all, as the words currently amount to almost 2000, of which 1322 do not have missing data as inferred by the algorithm.
2. All words tested directly will be tracked with their concept, their variety, and their form.
3. Later, we will compare the number of those words that have been correctly proposed by the algorithm and the words where it failed.
4. The results will be reported.

## Testing the Prediction on the Current Data

  accuracy  |   proportion |   density |   fuzziness |   coverage |   purity |   sounds |   missing
----------  | ------------ | --------- | ----------- | ---------- | -------- | -------- | ---------  
    0.6993  |       0.7588 |    0.6278 |      0.7691 |      0.297 |   0.7554 |       63 |    0.0789


doculect   |   accuracy |   purity  |   sounds  |   words
---------- | ---------- | --------  | --------  | -------
Duhumbi    |     0.5671 |   0.7138  |       58  |     367
Jerigaon   |     0.6954 |   0.7711  |       62  |     343
Khispi     |     0.6207 |   0.7178  |       48  |     329
Khoina     |     0.7058 |   0.7349  |       73  |     386
Khoitam    |     0.7588 |   0.7666  |       65  |     374
Rahung     |     0.7801 |   0.7849  |       69  |     387
Rupa       |     0.7281 |   0.7841  |       73  |     406
Shergaon   |     0.7103 |   0.7701  |       56  |     315


## Timeline

* July 30 -- August 3, 2018: Tim Bodt visited the CALC group, and we started working on the data, aligning words, assigning cross-semantic cognate sets, and annotating morphemes.
* August 29, 2018: Johann-Mattis List carried out the prediction experiment using the lingrex software package, on the datafile `bodt-khobwa-cleaned`. This file was semi-automatically modified from the original data to re-compute the alignments and to correct for spurious errors (mainly missing cognate set identifiers).

 

