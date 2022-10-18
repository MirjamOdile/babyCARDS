'''A set of functions used to preprocess and tokenise the babyCARDS text.'''

import re
from bs4 import BeautifulSoup
import unicodedata
import nltk
from nltk.corpus import stopwords

def strip_html(text):
    '''
    Strips any remaining HTML from a text string.

    Args:
        text (str): Text to strip
    
    Returns:
        str: Stripped text.
    '''
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def remove_between_square_brackets(text):
    '''
    Removes text between square brackets from a string.

    Args:
        text (str): Text to clean
    
    Returns:
        str: Cleaned text.
    '''
    return re.sub('\[[^]]*\]', '', text)


def remove_non_ascii(text):
    '''
    Removes non-ASCII characters from a text string.

    Args:
        text (str): Text with non-ASCII characters
    
    Returns:
        str: Text with non-ASCII characters.
    '''
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def strip_underscores(text):
    '''
    Removes underscores from a text string.

    Args:
        text (str): Text string
    
    Returns:
        str: Text string with underscores.
    '''
    return re.sub(r'_+', ' ', text)


def remove_multiple_spaces(text):
    '''
    Remove multiple spaces from a text string.

    Args:
        text (str): Text string
    
    Returns:
        str: Text string without multiple spaces.
    '''
    return re.sub(r'\s{2,}', ' ', text)

def remove_urls(text):
    '''
    Remove urls from a text string.

    Args:
        text (str): Text string
    
    Returns:
        str: Text string without urls.
    '''
    return re.sub(r'http\S+', ' ', text)

def denoise_text(text):
    '''
    "Denoise" a text string.

    Args:
        text (str): Text string
    
    Returns:
        str: Text string sans noise.
    '''
    text_no_html = strip_html(text)
    text_no_square = remove_between_square_brackets(text_no_html)
    text_no_ascii = remove_non_ascii(text_no_square)
    text_no_under = strip_underscores(text_no_ascii)
    text_no_multiple = remove_multiple_spaces(text_no_under)
    text_no_url = remove_urls(text_no_multiple)
    return text_no_url.strip()

stopwords_list = set(stopwords.words('english'))

def simple_tokenise(document):
    '''
    "Tokenise a text string.

    Args:
        text (str): Text string
    
    Returns:
        str: Tokens string.
    '''
    # remove punctuations
    document = re.sub('[^\w\d\s]', ' ', document)
    
    # lowercase and split it to tokens
    document = document.lower().split()   
    
    # Stemming with PorterStemmer handling Stop Words
    document = [word for word in document if not word in stopwords_list]
    
    # preparing Messages with Remaining Tokens
    document = ' '.join(document)
    
    return document