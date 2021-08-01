import nltk
import re
from nltk.stem import WordNetLemmatizer


def tokenize_twitter(sentences):
    """
    Tokenize sentences into tokens (words)

    Args:
        sentences: List of strings

    Returns:
        List of lists of tokens
    """
    print("Starting Cleaning Process")
    tokenized_sentences = []
    for sentence in sentences:

        # Convert to lowercase letters
        sentence = cleanhtml(sentence)
        sentence = sentence.lower()
        sentence = _replace_urls(sentence)
        sentence = remove_email(sentence)
        sentence = misc(sentence)
        sentence = re.sub(r'[^a-zA-Z]', ' ', sentence)

        tokenized = nltk.word_tokenize(sentence)

        # append the list of words to the list of lists
        tokenized_sentences.append(tokenized)

    return tokenized_sentences

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def _replace_urls(data):
    # Removing URLs with a regular expression
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    data = url_pattern.sub(r'', data)
    return data

def remove_email(data):
    # Remove Emails
    data = re.sub('\S*@\S*\s?', '', data)
    return data

def misc(data):
    # Remove new line characters
    data = re.sub('\s+', ' ', data)
    # Remove distracting single quotes
    data = re.sub("\'", "", data)
    return data


lemmatizer = WordNetLemmatizer()

def lemma(sentences):
    print("Starting Lemmatization and Tokenizing Process")
    final = []
    for sentence in sentences:
        output = [w.lower() for w in sentence]
        lemmatized_output = [lemmatizer.lemmatize(w) for w in output]
        final.append(lemmatized_output)

    return final


def littleCleaning(sentences):
    print("Starting cleaning Process")
    ret_list = []
    for sentence in sentences:
      for words in sentence:
        if len(words) == 1 and (words == 'a' or words == 'i'):
          pass
        elif len(words) > 1:
          pass
        else:
          sentence.remove(words)

      word_list = " ".join(sentence).strip(" ")
      ret_list.append(word_list)
    return ret_list


def normalization_pipeline(sentences):
    print("Starting Normalization Process")
    sentences = tokenize_twitter(sentences)
    sentences = lemma(sentences)
    sentences = littleCleaning(sentences)
    print("Normalization Process Finished")
    return sentences