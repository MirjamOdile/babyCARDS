# babyCARDS: Binary computer-assisted recognition of (climate change) contrarian speech

This repository makes available the code to train binary logistic classifiers to distinguish between climate change **contrarian** (1) and **convinced** (0) written text. It has been trained on a corpus of documents by known contrarian and convinced actors and organisations. 

<br>

Specifically, three classifiers have been trained, namely

i) **babyCARDS**: a binary logistic classifier on complete documents by various blog-posts, twitter and facebook posts and newspaper articles,

ii) **sentenceCARDS**: a binary logistic classifier trained on the same data as babyCARDS at the sentence level, and

iii) **socialCARDS**: a binary logistic classifier only trained twitter and facebook posts.

<br>

Classifier performance was assessed on a **held out testing data set** containing only text from "unseen" sources, i.e. bloggers, twitter users, facebook users and newspaper articles that the classifiers have not been trained on, providing an insight into external validity.

<br>

```
Performance babyCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.87      0.90      0.88    509797
           1       0.91      0.88      0.90    597768

    accuracy                           0.89   1107565
   macro avg       0.89      0.89      0.89   1107565
weighted avg       0.89      0.89      0.89   1107565



Testing data (unseen bloggers, twitter users, facebook users and newspaper articles):

              precision    recall  f1-score   support

           0       0.71      0.90      0.80    180897
           1       0.90      0.70      0.79    221956

    accuracy                           0.79    402853
   macro avg       0.80      0.80      0.79    402853
weighted avg       0.81      0.79      0.79    402853
```
<br>

```
Performance sentenceCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.74      0.76      0.75   1437268
           1       0.84      0.83      0.83   2161986

    accuracy                           0.80   3599254
   macro avg       0.79      0.79      0.79   3599254
weighted avg       0.80      0.80      0.80   3599254



Testing data (unseen bloggers, twitter users, facebook users and newspaper articles):

              precision    recall  f1-score   support

           0       0.69      0.79      0.74    757918
           1       0.84      0.75      0.79   1075225

    accuracy                           0.77   1833143
   macro avg       0.76      0.77      0.76   1833143
weighted avg       0.78      0.77      0.77   1833143
```
<br>

```
Performance socialCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.88      0.90      0.89    484130
           1       0.91      0.89      0.90    547607

    accuracy                           0.90   1031737
   macro avg       0.90      0.90      0.90   1031737
weighted avg       0.90      0.90      0.90   1031737



Testing data (unseen twitter and facebook users):

              precision    recall  f1-score   support

           0       0.70      0.90      0.79    166797
           1       0.89      0.67      0.77    200079

    accuracy                           0.78    366876
   macro avg       0.79      0.79      0.78    366876
weighted avg       0.80      0.78      0.78    366876
```
