"""Fit the optimised logistic classifer to the babyCARDS corpus."""

from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def fit_logistic_classifier(data):
    '''
    Takes training "data" and fits a LogisticRegression classifier.

    Args:
        data (list): A list of lists holding the paragraph text (index 0) 
                     and the claim (index 1).
    
    Returns:
        dict: A dictionary with the following keys:
              "clf" (LogisticRegression): the fitted logistic classifer
              "label_encoder" (LabelEncoder): encoder used for labels.
              "vectorizer" (TfidfVectorizer): Fitted TF-IDF vectorizer.           
    '''
    # Encode labels
    claims = [row[1] for row in data]
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(claims)

    # Vectorize
    text = [row[0] for row in data]

# Setup the Tf-Idf vectorizer
    vectorizer = TfidfVectorizer(stop_words='english',
                                 min_df=2,
                                 strip_accents='unicode',
                                 ngram_range=(1, 2), 
                                 lowercase=False, 
                                 sublinear_tf=1)

    X = vectorizer.fit_transform(text)

    # Fit final logistic classifier
    clf_logit = LogisticRegression(C=3.3,
                                solver='liblinear',
                                multi_class='ovr',
                                max_iter=200,
                                class_weight='balanced')

    # Fit final logit model
    clf_logit.fit(X, y)

    return {'clf': clf_logit, 'label_encoder': le, 'vectorizer': vectorizer}