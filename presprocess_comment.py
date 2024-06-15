from nltk import SnowballStemmer
from nltk.corpus import stopwords
import re
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

def preprocess_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'http\S+|www.\S+', '', sentence, flags=re.IGNORECASE)
    sentence = re.sub(r'[^\w\s]', '', sentence, flags=re.IGNORECASE)
    print(sentence)
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    sentence = ' '.join(filtered_words)
    sentence = ' '.join([stemmer.stem(word) for word in sentence.split()])
    return sentence

# sentence = "hi This is an example sentence with some stop words."
# filtered_sentence = preprocess_sentence(sentence)
# print(filtered_sentence)