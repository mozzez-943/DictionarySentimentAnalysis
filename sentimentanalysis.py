import csv

def read_positive(file_path):
    positive = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            category, attribute = row
            if category in positive:
                positive[category].append(attribute)
            else:
                positive[category] = [attribute]
    return positive

def read_negative(file_path):
    negative = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            category, attribute = row
            if category in negative:
                negative[category].append(attribute)
            else:
                negative[category] = [attribute]
    return negative

"""
Reading the email.txt file and outputting the sentiment of the email.

We want to convert the email into a list of words and then check if the words
are in the positive or negative dictionary.

If the word is in the positive dictionary, we increment the positive sentiment
score by 1. If the word is in the negative dictionary, we increment the
negative sentiment score by 1.

We will also give an overall sentiment score based on the difference between
the positive and negative sentiment scores.

We will also reflect which key the words belong to in the positive and negative
dictionary.
"""

def sentiment_analysis(email_path, positive, negative):
    positive_score = 0
    negative_score = 0
    with open(email_path, mode='r') as file:
        # read the email and convert to lowercase and split by space
        # remove all the special characters

        email = file.read().lower().split()
        email = [word.strip('.,!?*') for word in email]

        for word in email:
            for key, value in positive.items():
                if word in value:
                    positive_score += 1
                    print(f'+1: {word} is in the {key} category.')
            for key, value in negative.items():
                if word in value:
                    negative_score += 1
                    print(f'-1: {word} is in the {key} category.')
    sentiment_score = positive_score - negative_score
    print(f'Positive score: {positive_score}')
    print(f'Negative score: {negative_score}')
    print(f'Overall sentiment score: {sentiment_score}')

positive = read_positive('positive.csv')
negative = read_negative('negative.csv')
sentiment_analysis('pos_email.txt', positive, negative)