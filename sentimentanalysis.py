import csv

"""
### Task 1: Read From the CSV Files and Populate the Dictionaries ###
"""
def read_csv(file_path):
    dictionary = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            category, word = row
            if category in dictionary:
                dictionary[category].append(word)
            else:
                dictionary[category] = [word]
    return dictionary

"""
### Task 2: Complete the Sentiment Analysis ###

Given a txt file, we want to output the overall sentiment of the email.

1. First, we convert the text into a list of words. To ensure that we can match
the words to the positive and negative dictionaries, we convert all the words
to lowercase and remove any special characters (e.g. punctuation).

2. If the word is in the positive dictionary, we increment the positive
sentiment score by 1. Similarly, if the word is in the negative dictionary, we
instead increment the negative sentiment score by 1.

3. Once we have parsed through the email, an overall sentiment score is
generated based on the difference between the positive and negative sentiment
scores.
"""

def sentiment_analysis(email_path, positive, negative):
    positive_score = 0
    negative_score = 0
    with open(email_path, mode='r') as file:
        # step 1: convert the email into a list of words
        email = file.read().lower().split()
        email = [word.strip('.,!?*') for word in email]
        # step 2: check if the word is in the positive or negative dictionary
        for word in email:
            for key, value in positive.items():
                if word in value:
                    positive_score += 1
                    print(f'+1: {word} is in the {key} category.')
            for key, value in negative.items():
                if word in value:
                    negative_score += 1
                    print(f'-1: {word} is in the {key} category.')
    # step 3: calculate the overall sentiment score and output the results
    sentiment_score = positive_score - negative_score
    print(f'Positive score: {positive_score}')
    print(f'Negative score: {negative_score}')
    print(f'Overall sentiment score: {sentiment_score}')

"""
### Task 3: Run the Code! ###
"""
positive = read_csv('positive.csv')
negative = read_csv('negative.csv')
sentiment_analysis('pos_email.txt', positive, negative)