
import re
from collections import OrderedDict
import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory



class SentimentAnalyzer:

    def __init__(self):
        self.negasi = [line.replace('\n','') for line in open("Analisis/negatingword.txt").read().splitlines()]
        self.postive_words = [line.replace('\n','') for line in open("Analisis/positive_gabung.txt").read().splitlines()]
        self.negative_words = [line.replace('\n','') for line in open("Analisis/negative_gabung.txt").read().splitlines()]
        # factory = StemmerFactory()
        # self.stemmer = factory.create_stemmer()

    def main(self,sentence) :
        sentences = sentence.split('.')
        total_score = 0
     

        for sentence in sentences:            
            sentence_score = 0
            prev = ""
            terms = sentence.split()
            terms_length = len(terms)

            for term in terms:
                
                term_score = 0
                
                # for pos_term in self.postive_words :
                #     dis = self.minimumEditDistance(pos_term,term)
                #     if dis <= 1 :
                #         term_score = 1
                #         break

                # for neg_term in self.negative_words :
                #     dis = self.minimumEditDistance(neg_term,term)
                #     if dis <= 1 :
                #         term_score = -1
                #         break

                if(term in self.postive_words) :
                    term_score = 1
                elif(term in self.negative_words) :
                    term_score = -1

                if(prev in self.negasi) :
                    term_score *= -1

                sentence_score += term_score
                #print (term,term_score)
                prev = term
            total_score = sentence_score
        return total_score

    def minimumEditDistance(self,s1,s2):
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        distances = range(len(s1) + 1)
        for index2,char2 in enumerate(s2):
            newDistances = [index2+1]
            for index1,char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1+1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]


#UNCOMMAND UNTUK MENGANALISIS SEnTIMEN DARI SEBUAH FILE (yg sudah di clean)

# with open('tweets_cleaned.txt', 'r') as file:
#     i = 0
#     for line in file :
#         # factory = StemmerFactory()
#         # stemmer = factory.create_stemmer()
#         # line = stemmer.stem(line)
#         x = sentimen.main(line)
#         if x > 0 :
#             res["positif"] += 1
#         elif x < 0 :
#             res["negatif"] += 1
#         else :
#             res["netral"] +=1 
#         scores.append(x);
#         i += 1
#         if(i <= 100000) :
#             print(i)
#             x = sentimen.main(line)
#             if x > 0 :
#                 res["positif"] += 1
#             elif x < 0 :
#                 res["negatif"] += 1
#             else :
#                 res["netral"] +=1 
#             scores.append(x);
#  print(scores)
# print(res)
#  with open('result_jkw.txt', 'a') as f:
#     f.write("\n====================RESULT==========================\n")
#     f.write(str(scores))
#     f.write(str(res))