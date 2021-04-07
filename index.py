import nltk
"""
    corpus = collection of text
    tokenizers = divides text into tokens
        word, sentence, regex tokenizer
    
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = ""
"""
    remove stop words (is, a, an, the, a) = adds no value
"""
stopwords = set(stopwords.words("english"))
words = word_tokenize(text)
"""
    create a frequency table of words = determines which words has the most relevancy
"""

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word]+= 1
    else:
        freqTable[word]=1
"""
    assign score to sentence depending on the words/frequency table
"""

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
        if sentence in sentenceValue:
            sentenceValue[sentence] += freq
        else:
            sentenceValue[sentence]=freq

"""
    assign score to comapre sentences = find average score => okay threshold
"""

sumValues = 0
for sentence in sentenceValue:
    sumValues+= sentenceValue[sentence]
average = int(sumValues / len(sentenceValue))

summary = ""
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " "+ sentence
print(summary)