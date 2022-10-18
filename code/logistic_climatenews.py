"""Fit the optimised logistic classifer to the babyCARDS corpus."""

from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from operator import itemgetter

def fit_logistic_classifier(data, C=1, penalty='l2'): 
# C=1 and penalty="l2" are the sklearn.linear_model.LogisticRegression default values
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
    vectorizer = TfidfVectorizer(stop_words=None,
                                 min_df=2,
                                 strip_accents='unicode',
                                 ngram_range=(1, 2), 
                                 lowercase=True, 
                                 sublinear_tf=1)

    X = vectorizer.fit_transform(text)

    # Fit final logistic classifier
    clf_logit = LogisticRegression(C=C,
                                   penalty=penalty,
                                   solver='liblinear',
                                   max_iter=200,
                                   class_weight='balanced')

    # Fit final logit model
    clf_logit.fit(X, y)

    return {'clf': clf_logit, 'label_encoder': le, 'vectorizer': vectorizer}


def show_most_informative_features(model, text=None, n=50):
    """
    Computes the n most informative features of a TFidf classifier model. 
    If text is given, then will compute the most informative features for classifying that text.
    Note that this function will only work on linear models with coefs_
    """
    # Extract the vectorizer and the classifier from the pipeline
    vectorizer = model['vectorizer']
    classifier = model['clf']

    # Check to make sure that we can perform this computation
    if not hasattr(classifier, 'coef_'):
        raise TypeError(
            "Cannot compute most informative features on {} model.".format(
                classifier.__class__.__name__
            )
        )

    if text is not None:
        # Compute the coefficients for the text
        tvec = vectorizer.transform([text]).toarray()
    else:
        # Otherwise simply use the coefficients
        tvec = classifier.coef_

    # Zip the feature names with the coefs and sort
    coefs = sorted(
        zip(tvec[0], vectorizer.get_feature_names_out()),
        key=itemgetter(0), reverse=True
    )

    topn  = zip(coefs[:n], coefs[:-(n+1):-1])

    # Create the output string to return
    output = []

    # If text, add the predicted value to the output.
    if text is not None:
        output.append("\"{}\"".format(text))
        output.append("Classified as: {}".format(classifier.predict(tvec)))
        output.append("")

    # Create two columns with most negative and most positive features.
    for (cp, fnp), (cn, fnn) in topn:
        output.append(
            "{:0.4f}{: >15}    {:0.4f}{: >15}".format(cp, fnp, cn, fnn)
        )

    return "\n".join(output)
# Adapted from https://gist.github.com/bbengfort/044682e76def583a12e6c09209c664a1