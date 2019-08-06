from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from random import randint
from termcolor import colored
from open_file import open_file_function
from copy_lines import copy_lines
import io
import codecs
import sys

def extro_intro_switch(lineList):

    reload(sys)
    sys.setdefaultencoding("utf-8")

    i = 0
    outF_intro = open("myOutFile_intro.txt", "a")
    outF_extro = open("myOutFile_extro.txt", "a")
    del lineList[:4] #delete the first 4 lines of the topic text

    for i in lineList:
        input = i #each line is the input

        #Tokenize the sentence
        tokens = word_tokenize(input)

        #save info needed for the topic
        tok_0 = tokens[0]
        tok_1 = tokens[1]
        last_tok = tokens[-2:]

        #delete the info needed for the topic in order to analyze the sentence
        del tokens[0]
        del tokens[0]
        del tokens[-1]
        del tokens[-1]

        #detokenize the sentence
        sent_2 = TreebankWordDetokenizer().detokenize(tokens)

        tok_0_det= TreebankWordDetokenizer().detokenize(tok_0)
        tok_1_det= TreebankWordDetokenizer().detokenize(tok_1)
        last_tok_det = TreebankWordDetokenizer().detokenize(last_tok)

        #delete the space between the characters
        tok_0_det = tok_0_det.replace(" ", "")
        tok_1_det = tok_1_det.replace(" ", "")
        last_tok_det = last_tok_det.replace(" ", "")

        #convert to list
        l = list(sent_2)

        try:
            l.append(l[1]) #to avoid list IndexError


            if tokens[0] == "Posso" and tokens[1] == "chiederti" and tokens[2] == "di" and tokens[3] == "nuovo":
                l[:24] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)
                print colored("extro sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Posso" and tokens[1] == "chiederti":
                l[:25] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)
                print colored("extro sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "So" and tokens[1] == "che":
                l[:6] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)

                l2 = list(complete_sent)
                del (l2[-3])
                complete_sent2 = "".join(l2)

                print colored("extro sentence: ", "blue")
                print(complete_sent2)
                outF_extro.write(complete_sent2)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Sei" and tokens[1] == "molto" and tokens[2] == "paziente":
                l[:20] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)

                l2 = list(complete_sent)
                del (l2[-3])
                complete_sent2 = "".join(l2)

                print colored("extro sentence: ", "blue")
                print(complete_sent2)
                outF_extro.write(complete_sent2)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[-1] == "paziente" and tokens[-2] == "davvero" and tokens[-3] == "sei":
                l[-23:] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Per" and tokens[1] == "favore" and tokens[2] == "," and tokens[3] == "parlami":
                l[:11] =[]
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Dai," + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Per" and tokens[1] == "favore" and tokens[2] == "," and tokens[3] == "dimmi":
                l[:11] =[]
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Dai," + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Per" and tokens[1] == "favore" and tokens[2] == "," and tokens[3] == "dimmi":
                l[:11] =[]
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Dai," + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Lo" and tokens[1] == "vedo":
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det + tok_1_det + "Lo vedo amico mio" + last_tok_det
                print(input)
                print colored('extro-sentence: ', 'red')
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Dovresti":
                l[:8] =[]
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Forse dovresti" + sent_new + last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")


            elif tokens[0] == "E'" and tokens[1]== "molto" and tokens[2]== "interessante":
                l[:27] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "E' molto interessante" + sent_new + last_tok_det
                print colored('extro-sentence: ', 'red')
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif tokens[0] == "Va" and tokens[1] == "bene" and tokens[3] == ",":
                l[:8] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Va bene amico," + sent_new + last_tok_det
                print colored('extro-sentence: ', 'blue')
                print complete_sent
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")


            elif l[-1] is "?" and tokens[0] != "Posso":
                complete_sent = tok_0_det + tok_1_det + "Posso farti una domanda?" + sent_2 + last_tok_det
                print colored('intro-sentence: ', 'red')
                print complete_sent
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

        
            elif tokens[0]== "Mi" and tokens[1] == "puoi" and tokens[2] == "dire":
                l[:12] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "Potresti dirmi" + sent_new + last_tok_det
                print colored('intro-sentence: ', 'red')
                print complete_sent
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")


            else:
                print colored ("Not classifiable: ", 'green')
                print input
                print("_____________________________")
        except IndexError:
            pass
        continue

        outF_extro.close()
        ourF_intro.close()
