sentimen = []
with open('tweets.txt', 'r') as file:
    counter = 0
    for line in file :
        # counter+=1
        # if (counter == 21) :
        #     break
        nilai_sentimen = 0
        tweet = line.split(" ")
        with open('lexicon.txt', 'r') as lexicon:
            for lex in lexicon :
                for kata in tweet :
                    # print("check antara " + kata.lower() + " <==> " + lex.split(" ")[0])
                    if kata.lower() == lex.split(" ")[0] :
                        print("DAPET COY")
                        nilai_sentimen += int(lex.split(" ")[1])
        sentimen.append(nilai_sentimen)

print(sentimen)
print("selesai")