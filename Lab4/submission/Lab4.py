from typing import Set
from sklearn.naive_bayes import BernoulliNB
import re

def tokenize(text: str) -> Set[str]:
    text = text.lower()                         # Convert to lowercase,
    all_words = re.findall("[a-z0-9']+", text)  # extract the words, and
    return set(all_words)                       # remove duplicates.

assert tokenize("Data Science is science") == {"data", "science", "is"}

from typing import NamedTuple

class Message(NamedTuple):
    text: str
    is_spam: bool

from typing import List, Tuple, Dict, Iterable
import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self, k: float = 0.5, min_count: int = 0) -> None:
        self.k = k  # smoothing factor
        self.min_count = min_count # min num of tokens we want to accept

        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str, int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0

    def ignore_tokens(self) -> None:
        if self.min_count != 0:
            removeList = []
            for token in self.tokens:
                if self.token_spam_counts[token] + self.token_ham_counts[token] < self.min_count:
                    removeList.append(token)
            for token in removeList:
                self.tokens.remove(token)
                self.token_spam_counts.pop(token)
                self.token_ham_counts.pop(token)
            
    def train(self, messages: Iterable[Message]) -> None:
        for message in messages:
            # Increment message counts
            if message.is_spam:
                self.spam_messages += 1
            else:
                self.ham_messages += 1

            # Increment word counts
            for token in tokenize(message.text): 
                self.tokens.add(token)
                if message.is_spam:
                    self.token_spam_counts[token] += 1
                else:
                    self.token_ham_counts[token] += 1


        self.ignore_tokens()


    def _probabilities(self, token: str) -> Tuple[float, float]:
        """returns P(token | spam) and P(token | not spam)"""
        spam = self.token_spam_counts[token]
        ham = self.token_ham_counts[token]

        p_token_spam = (spam + self.k) / (self.spam_messages + 2 * self.k)
        p_token_ham = (ham + self.k) / (self.ham_messages + 2 * self.k)

        return p_token_spam, p_token_ham

    def predict(self, text: str) -> float:
        text_tokens = tokenize(text)
        log_prob_if_spam = log_prob_if_ham = 0.0

        # Iterate through each word in our vocabulary.
        for token in self.tokens:
            prob_if_spam, prob_if_ham = self._probabilities(token)

            # If *token* appears in the message,
            # add the log probability of seeing it;
            if token in text_tokens:
                log_prob_if_spam += math.log(prob_if_spam)
                log_prob_if_ham += math.log(prob_if_ham)

            # otherwise add the log probability of _not_ seeing it
            # which is log(1 - probability of seeing it)
            else:
                log_prob_if_spam += math.log(1.0 - prob_if_spam)
                log_prob_if_ham += math.log(1.0 - prob_if_ham)

        prob_if_spam = math.exp(log_prob_if_spam)
        prob_if_ham = math.exp(log_prob_if_ham)
        return prob_if_spam / (prob_if_spam + prob_if_ham)


def main():
    import glob, re
    
    # modify the path to wherever you've put the files
    path = '../../data/*/*'
    
    data: List[Message] = []
    
    # glob.glob returns every filename that matches the wildcarded path
    for filename in glob.glob(path):
        is_spam = "ham" not in filename
    
        # There are some garbage characters in the emails, the errors='ignore'
        # skips them instead of raising an exception.
        with open(filename, errors='ignore') as email_file:
            for line in email_file:
                if line.startswith("Subject:"):
                    subject = line.lstrip("Subject: ")
                    data.append(Message(subject, is_spam))
                    break  # done with this file
    
    import random
    from machine_learning import split_data
    
    random.seed(0)      # just so you get the same answers as me
    train_messages, test_messages = split_data(data, 0.75)

    # Providing optional min_count
    model = NaiveBayesClassifier(min_count=5)
    model.train(train_messages)
    
    from collections import Counter
    
    # (word, prediction)
    predictions = [(message, model.predict(message.text))
                   for message in test_messages]
    
    # Assume that spam_probability > 0.5 corresponds to spam prediction
    # and count the combinations of (actual is_spam, predicted is_spam)
    confusion_matrix = Counter((message.is_spam, spam_probability > 0.5)
                               for message, spam_probability in predictions)
    
    print("CONFUSION MATRIX: ", confusion_matrix)
    
    def p_spam_given_token(token: str, model: NaiveBayesClassifier) -> float:
        # We probably shouldn't call private methods, but it's for a good cause.
        prob_if_spam, prob_if_ham = model._probabilities(token)
    
        return prob_if_spam / (prob_if_spam + prob_if_ham)
    
    words = sorted(model.tokens, key=lambda t: p_spam_given_token(t, model))
    
    print("spammiest_words", words[-10:])
    print("hammiest_words", words[:10])
    
if __name__ == "__main__": main()
##################################################################



# Run the spam classifier, what is the confusion matrix? What is the precision and recall? What are the spammmiest words and hammiest words?

# -- Confusion Matrix
# Counter({(False, False): 668, (True, True): 85, (True, False): 54, (False, True): 18})

# -- Precision & Recall
# Precision = 85 / 85 + 18 = .8252 = 82.52%
# Recall = 85 / 85 + 54 = .6115 = 61.15%

# -- Hammiest and Spammiest Words
# spammiest_words ['fortune', 'assistance', 'attn', 'account', 'sale', 'zzzz', 'systemworks', 'money', 'rates', 'adv']
# hammiest_words ['spambayes', '2', 'users', 'razor', 'zzzzteana', 'sadev', 'ouch', 'apt', 'bliss', 'selling']

# # Modify the classifier to accept an optional min_count threshold and ignore tokens that don’t appear at least that many times. Rerun the modified classifier and answer the same questions above.

# -- Confusion Matrix
# Counter({(False, False): 587, (True, True): 101, (False, True): 99, (True, False): 38})

# -- Precision & Recall
# Precision = 101 / 101 + 38 = .7266 = 72.66%
# Recall = 101 / 101 + 99 = .505 = 50.5%

# -- Hammiest and Spammiest Words
# spammiest_words ['reps', 'assistance', 'attn', 'sale', 'account', 'zzzz', 'money', 'systemworks', 'adv', 'rates']
# hammiest_words ['spambayes', '2', 'users', 'razor', 'zzzzteana', 'sadev', 'ouch', 'apt', 'bliss', 'wedded']
