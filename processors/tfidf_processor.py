import logging

from sklearn import model_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR

from processors.abstract_processor import Processor
from utils import file_helper

log = logging.getLogger(__name__)


class TfIdfProcessor(Processor):

    def process(self):
        log.info("TfIdfProcessor begun")

        input_tweets = file_helper.read_input_data(self.options.input_file_path)

        y_train = list()
        tweet_text = list()
        for input_tweet in input_tweets:
            tweet_text.append(input_tweet.text)
            y_train.append(input_tweet.intensity)

        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
        x_train = vectorizer.fit_transform(tweet_text)

        scores = \
            model_selection.cross_val_score(
                LinearSVR(), x_train, y_train, cv=10, scoring='r2'
            )
        mean_score = scores.mean()

        log.info("Accuracy: %0.2f (+/- %0.2f)" % (mean_score, scores.std() * 2))

        log.info("TfIdfProcessor ended")
