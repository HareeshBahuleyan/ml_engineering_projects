import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.base import BaseEstimator, TransformerMixin


class TextPreprocessor(BaseEstimator,TransformerMixin):
    def __int__ (self):
        pass
    
    def preprocess_text(self, text):
        """
        All preprocessing steps
        """
        text = self.convert_lower(text)
        text = self.remove_tags(text)
        text = self.remove_special_chars(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_words(text)
        
        return text
    
    def fit(self, X, y=None):
        # nothing to be done as no "fitting" is required here
        return self

    def transform(self, X):
        """
        Args:
            X: list of texts
        Returns:
            list of transformed text
        """
        X_ = list()
        # note: since we loop here, it will be slower than
        # batch apply() - which would have been the approach in pandas
        for text in X:
            X_.append(self.preprocess_text(text))
        return X_
    
    @staticmethod
    def convert_lower(text):
        return text.lower()
    
    @staticmethod
    def remove_tags(text):
        remove = re.compile(r'<.*?>')
        return re.sub(remove, '', text)
    
    @staticmethod
    def remove_special_chars(text):
        text = ''.join([ch for ch in text if ch.isalnum() or ch == ' ' ])
        return text
    
    @staticmethod
    def remove_stopwords(text):
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        return [x for x in words if x not in stop_words]
    
    @staticmethod
    def lemmatize_words(text):
        wordnet = WordNetLemmatizer()
        return " ".join([wordnet.lemmatize(word) for word in text])
