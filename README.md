# babyCARDS: Binary computer-assisted recognition of (climate change) contrarian speech

This repository makes available the code to train binary logistic classifiers to distinguish between climate change **contrarian** (1) versus **convinced** (0) written text. It has been trained on documents by know contrarian and convinced actors. Specifically, three classifiers have been trained, namely

i) **babyCARDS**: a binary logistic classifier on complete documents by various blog-posts, twitter and facebook posts and newspaper articles,

ii) **sentenceCARDS**: a binary logistic classifier trained on the same data as babyCARDS at the sentence level, and

iii) **socialCARDS**: a binary logistic classifier only trained twitter and facebook posts.


```
Performance babyCARDS:


```

```
Performance sentenceCARDS:


```

```
Performance socialCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.88      0.90      0.89    484130
           1       0.91      0.89      0.90    547607

    accuracy                           0.90   1031737
   macro avg       0.90      0.90      0.90   1031737
weighted avg       0.90      0.90      0.90   1031737



Testing data (unseen twitter/facebook handles):

              precision    recall  f1-score   support

           0       0.70      0.90      0.79    166797
           1       0.89      0.67      0.77    200079

    accuracy                           0.78    366876
   macro avg       0.79      0.79      0.78    366876
weighted avg       0.80      0.78      0.78    366876


```
```
Performance tweetyCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.90      0.92      0.91    357773
           1       0.94      0.92      0.93    433777

    accuracy                           0.92    791550
   macro avg       0.92      0.92      0.92    791550
weighted avg       0.92      0.92      0.92    791550



Testing data (unseen twitter handles):

              precision    recall  f1-score   support

           0       0.73      0.85      0.79    142178
           1       0.90      0.81      0.85    231942

    accuracy                           0.83    374120
   macro avg       0.82      0.83      0.82    374120
weighted avg       0.84      0.83      0.83    37412
```
