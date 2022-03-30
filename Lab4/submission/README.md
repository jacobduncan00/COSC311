# Run the spam classifier, what is the confusion matrix? What is the precision and recall? What are the spammmiest words and hammiest words?

-- Confusion Matrix
Counter({(False, False): 668, (True, True): 85, (True, False): 54, (False, True): 18})

-- Precision & Recall
Precision = 85 / 85 + 18 = .8252 = 82.52%
Recall = 85 / 85 + 54 = .6115 = 61.15%

-- Hammiest and Spammiest Words
spammiest_words ['fortune', 'assistance', 'attn', 'account', 'sale', 'zzzz', 'systemworks', 'money', 'rates', 'adv']
hammiest_words ['spambayes', '2', 'users', 'razor', 'zzzzteana', 'sadev', 'ouch', 'apt', 'bliss', 'selling']

# Modify the classifier to accept an optional min_count threshold and ignore tokens that don’t appear at least that many times. Rerun the modified classifier and answer the same questions above.

-- Confusion Matrix
Counter({(False, False): 587, (True, True): 101, (False, True): 99, (True, False): 38})

-- Precision & Recall
Precision = 101 / 101 + 38 = .7266 = 72.66%
Recall = 101 / 101 + 99 = .505 = 50.5%

-- Hammiest and Spammiest Words
spammiest_words ['reps', 'assistance', 'attn', 'sale', 'account', 'zzzz', 'money', 'systemworks', 'adv', 'rates']
hammiest_words ['spambayes', '2', 'users', 'razor', 'zzzzteana', 'sadev', 'ouch', 'apt', 'bliss', 'wedded']
