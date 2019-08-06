from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from random import randint
from termcolor import colored
from open_file import open_file_function
from copy_lines import copy_lines

def extro_intro_switch(lineList):

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

            if tokens[0] == "I" and tokens[1] == "want" or tokens[1] == "need":
                l[:6] = [] #delete I want/need
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det + tok_1_det + "I would like to have" + sent_new + last_tok_det
                print(input)
                print colored("intro need-sentence: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "see":
                complete_sent = tok_0_det + tok_1_det + "I see my friend" + last_tok_det
                print(input)
                print colored('extro-sentence: ', 'red')
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] =="I" and tokens[1]=="would" and tokens[2] == "like" and tokens[3] == "to" and tokens[4] == "have":
                l[:20] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det+tok_1_det+"I want " + sent_new+last_tok_det
                print(input)
                print colored("extro need-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "come"  and tokens[1] == "on" and tokens[2] == "tell" and tokens[3] == "me":
                l[:15] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det+tok_1_det+ "I would like to know " + sent_new+last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "People" and tokens[1] =="tell" and tokens[2] == "me"  and tokens[3] == "that":
                l[:20] = []
                l[-1:] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det+tok_1_det+"I know that " + sent_new+last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "It" and tokens[1] == "'s" and tokens[2] =="good" and tokens[3] == "to" and tokens[4] == "have":
                l[:9] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det+tok_1_det+"I like " + sent_new+last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[-1] == "nice" and tokens[-2] == "be" and tokens[-3] == "would" and tokens[-4]=="It":
                l[-16:] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det+ sent_new + "It could be nice" + last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "think" and tokens[2] == "that":
                l[:13] = []
                sent_new = "".join(l)
                print(input)
                print colored("extro-sentence: ", "blue")
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "know" and tokens[2] == "that":
                l[:12] = []
                sent_new = "".join(l)
                print(input)
                print colored("extro-sentence: ", "blue")
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "am" and tokens[2] == "aware" and tokens[3] == "that":
                l[:15] = [ ] #delete I am aware that
                sent_new = "".join(l)
                print(input)
                print colored("extro-sentence: ", "blue")
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "would" and tokens[2] == "like" and tokens[3] == "to" and tokens[4] == "know":
                l[:20] =[]
                sent_new = "".join(l)
                complete_sent= tok_0_det + tok_1_det + "come on, tell me "+ sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Please" and tokens[1]== "," and tokens[2] == "tell" and tokens[3] == "me":
                l[:15] = []
                sent_new = "".join(l)
                complete_sent= tok_0_det + tok_1_det + "come on, tell me "+ sent_new + last_tok_det
                print(input)

                l2 = list(complete_sent)
                del (l2[-3])
                complete_sent2 = "".join(l2)

                print colored("extro-sentence: ", "blue")
                print(complete_sent2)
                outF_extro.write(complete_sent2)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "understand" and tokens[2] == ",":
                l[:14] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "OK " + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "understand" and tokens[2] == "that":
                l[:12] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + "It's clear " + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "You" and tokens[1] == "are" and tokens[2] == "very" and tokens[3] == "patient":
                l[:22] = []
                sent_new = "".join(l)
                print(input)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det

                l2 = list(complete_sent)
                del (l2[-3])
                complete_sent2 = "".join(l2)

                print colored("extro-sentence: ", "blue")
                print complete_sent2
                outF_extro.write(complete_sent2)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[-1] == "patient" and tokens[-2] == "very" and tokens[-3] == "are" and tokens[-4] == "you":
                l[-23:] = []
                sent_new = "".join(l)
                complete_sent = tok_0_det + tok_1_det + sent_new + last_tok_det
                print(input)
                print colored("extro-sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")



            elif tokens[0] == "I" and tokens[1] == "like" or tokens[1] == "love":
                number = randint(1,2) #generate a random number to choose between two different adj
                l[:6] = []
                last_element = l[-1] #save the last element
                if number == 1:
                    if last_element == "s":
                        sent_new = "".join(l)
                        complete_sent = tok_0_det + tok_1_det + sent_new + " are really good" + last_tok_det
                        print(input)
                        print colored("extro-sentence: ", "blue")
                        print(complete_sent)
                        outF_extro.write(complete_sent)
                        outF_extro.write("\n")
                        print("_____________________________")
                    else:
                        sent_new = "".join(l)
                        complete_sent = tok_0_det + tok_1_det + sent_new + " is really good" + last_tok_det
                        print(input)
                        print colored("extro-sentence: ", "blue")
                        print(complete_sent)
                        outF_extro.write(complete_sent)
                        outF_extro.write("\n")
                        print("_____________________________")
                if number == 2:
                    if last_element == "s":
                        sent_new = "".join(l)
                        complete_sent = tok_0_det + tok_1_det + sent_new + " are really nice" + last_tok_det
                        print(input)
                        print colored("extro-sentence: ", "blue")
                        print(complete_sent)
                        outF_extro.write(complete_sent)
                        outF_extro.write("\n")
                        print("_____________________________")
                    else:
                        sent_new = "".join(l)
                        complete_sent = tok_0_det + tok_1_det + sent_new + " is really nice" + last_tok_det
                        print(input)
                        print colored("extro-sentence: ", "blue")
                        print(complete_sent)
                        outF_extro.write(complete_sent)
                        outF_extro.write("\n")
                        print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "will" and tokens[2] == "try" and tokens[3] == "to":
                l[:13] = [ ] #delete I will try to
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det + tok_1_det + "I will" + sent_new + last_tok_det
                print(input)
                print colored("intro-future sentence: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "I" and tokens[1] == "will" and tokens[3]!= "try" :
                l[:6] = [ ] #delete I will
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det+ tok_1_det + "I will try to" + sent_new + last_tok_det
                print(input)
                print colored("extro-future sentence: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif l[-1] is "?" and tokens[0] != "Can" and tokens[0] != "Could": #check if the sentence is a question
                complete_sent = tok_0_det+tok_1_det + "Can I ask you a question? " + sent_2 + last_tok_det
                print(input)
                print colored("intro-question: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Do": #check if the sentence is a question
                complete_sent = tok_0_det+tok_1_det+ "Can I ask you a question? " + sent_2 + last_tok_det
                print(input)
                print colored("intro-question: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif l[-1] == "?": #check if the sentence is a question
                complete_sent =tok_0_det+tok_1_det+ "Can I ask you a question? " + sent_2 + last_tok_det
                print(input)
                print colored("intro-question: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Can" and tokens[1]== "I" and tokens[2] == "ask" and tokens[3] == "you" and tokens[4] == "a" and tokens[5] ==  "question":
                l[:25] = [] #delete the elements (can I ...)
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det+tok_1_det+sent_new+ last_tok_det
                print(input)
                print colored("extro-question: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Please" and tokens[1] == "," and tokens[2]!= "tell" :
                complete_sent = tok_0_det+tok_1_det+ "Could you " + sent_2 + "?" + last_tok_det
                print(input)
                print colored("intro-request", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "Could" or tokens[0] == "could" and tokens[1] == "you":
                l[:9]=[] #delete could you
                l.pop() #extract the last element
                sent_new = "".join(l) #convert to string
                if tokens[2] != "please":
                    complete_sent= tok_0_det + tok_1_det + "Please" + sent_new + last_tok_det
                else:
                    complete_sent= tok_0_det+tok_1_det+sent_new+last_tok_det
                print(input)
                print colored("extro-request: ", "blue")
                print(complete_sent)
                outF_extro.write(complete_sent)
                outF_extro.write("\n")
                print("_____________________________")

            elif tokens[0]== "Can" and tokens[1] == "we" and tokens[2] == "talk" and tokens[3] == "about":
                l[:3] = []
                l.pop() #extract the last element
                sent_new = "".join(l) #convert to string
                complete_sent =tok_0_det+tok_1_det+ "It could be nice if" + sent_new + ". If you like the idea" + last_tok_det
                print(input)
                print colored("intro-suggestion: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0]== "Why" or tokens[0]== "why" and tokens[1]=="don't" and tokens[2]=="we":
                l[:9]=[] #delete why don't we
                l.pop() #extract the last element
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det+tok_1_det+"It could be nice if" + sent_new + ". If you like the idea" + last_tok_det
                print(input)
                print colored("intro-suggestion: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0] == "You" and tokens[1] == "should":
                l[:10]=[] #delete you should
                sent_new = "".join(l) #convert to string
                complete_sent = tok_0_det+tok_1_det+ "Maybe it's better if you " + sent_new + last_tok_det
                print(input)

                l = list(complete_sent)
                l[-1:] = []
                complete_sent = "".join(l)

                print colored("intro-suggestion: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0]== "How" or tokens[0] == "how" and tokens[1]== "about":
                l[:9]=[] #delete how about
                sent_new = "".join(l) #convert to string
                complete_sent=tok_0_det+tok_1_det+"May I suggest" + sent_new +"?" + last_tok_det
                print(input)
                print colored("intro-suggestion: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[0]=="Let" and tokens[1]=="'s" and tokens[2]=="talk":
                l[:10]=[] #delete may I suggest
                sent_new = "".join(l) #convert to string
                complete_sent=tok_0_det+tok_1_det+"May we talk" + sent_new + "?"+last_tok_det
                print(input)
                print colored("intro-suggestion: ", "red")
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")


            elif tokens[1] == "is" or tokens[1] == "are":
                tokens[1]=[] #delete the elements from the first to "if"
                tokens_2 = [x for x in tokens if x]
                sent_new = TreebankWordDetokenizer().detokenize(tokens_2) #detokenize the sentence
                complete_sent =tok_0_det+tok_1_det+ "I find " + sent_new + last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
                outF_intro.write(complete_sent)
                outF_intro.write("\n")
                print("_____________________________")

            elif tokens[2] == "is" or tokens[2] == "are":
                tokens[2]=[] #delete the elements from the first to "if"
                tokens_2 = [x for x in tokens if x]
                sent_new = TreebankWordDetokenizer().detokenize(tokens_2) #detokenize the sentence
                complete_sent = tok_0_det+tok_1_det+"I find " + sent_new+last_tok_det
                print(input)
                print colored('intro-sentence: ', 'red')
                print(complete_sent)
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
