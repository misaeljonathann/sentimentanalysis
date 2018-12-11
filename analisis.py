# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem

sentimen = []

with open('tweets_cleaned.txt', 'r') as file:
    counter = 0

    for line in file :
        line = stemmer.stem(line)
        print(line)
        nilai_sentimen = 0
        tweet = line.split(" ")
        with open('lexicon.txt', 'r') as lexicon:
            for lex in lexicon :
                for kata in tweet :
                    if kata.lower() == lex.split(" ")[0] :
                        nilai_sentimen += int(lex.split(" ")[1])
        sentimen.append(nilai_sentimen)

print(sentimen)
print("selesai")