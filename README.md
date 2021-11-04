# babyCARDS: Binary computer-assisted recognition of (climate change) contrarian speech

This repository makes available the code to train 

i) a binary logistic classifier on tweets by known contrarian (1) versus convinced (0) twitter users (tweetyCARDS) and 

ii) a binary logistic classifier on documents by various sources (newspapers, twitter, facebook, blog-posts) by known contrarian (1) versus convinced (0) actors (babyCARDS).


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
