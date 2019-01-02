#Importing Library for Chat Bot
import numpy as np
import re
import time

#Importing Data in program

lines = open("movie_lines.txt", encoding= "utf-8", errors = "ignore").read().split('\n')
Conversations = open("movie_conversations.txt", encoding= "utf-8", errors = "ignore").read().split('\n')

#Creating Dictionary that maps each line and its id

id2line = {}
for line in lines:
    _line = line.split(' +++$+++')
    if len(_line) == 5:
        id2line[_line[0]]= _line[4]

#Creating a list of all of the conversations

Conversations_id = []
for conversation in Conversations:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ","")
    Conversations_id.append(_conversation.split(","))

#Getting Seprately questions and answers
questions = []
answers = []
for conversation in Conversations_id:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])

#Doing a first cleaning of text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm","i am", text)
    text = re.sub(r"\'s","is", text)
    text = re.sub(r"he's","he is", text)
    text = re.sub(r"she's","she is", text)
    text = re.sub(r"that's","that is", text)
    text = re.sub(r"what's","what is", text)
    text = re.sub(r"where's","where is", text)
    text = re.sub(r"\'ll","will", text)
    text = re.sub(r"\'ve","have", text)
    text = re.sub(r"\'re","are", text)
    text = re.sub(r"\'d","would", text)
    text = re.sub(r"won't","will not", text)
    text = re.sub(r"can't","can not", text)
    text = re.sub(r"|{}\[]@;/':?.<>=~", "", text)
    return text

#Cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))

#Cleaning the answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
#Creating a dictionary that maps each word to its number of occurences
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1 
#Creating a two dictionaries that map the questions words and the answers word to unique integer
threashold = 20
questionword2hint = {}
word_number = 0 
for word, count in word2count.items():
    if count >= threashold:
        questionword2hint[word] = word_number
        word_number += 1 