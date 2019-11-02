
#==========================================
#A)
#Purpose: Takes in a file name as a string representing the name of the file, and returns
# a list of the first word in every sentence in that file in order.  
# Input Parameter(s): fname-a string representing the name of the file.
# Return Value(s): lst_of_first_word-A list of the first word in every sentence in that file in order.  
#==========================================
def first_words(fname):
    open_file=open(fname)
    sentence_list=open_file.readlines()
    open_file.close()
    lst_of_first_word=[]
    count=0
    for item in sentence_list:
        sentence=item.split(' ')
        lst_of_first_word.append(sentence[0])
    return lst_of_first_word
#==========================================
# Purpose: Takes in a file name as a string representing the name of the file, and returns
# a dictionary where the keys are each distinct word in the file and the value for any given key is a list of every word that follows that key
# anywhere in the file.  
# Input Parameter(s): fname-a string representing the name of the file.
# Return Value(s):next_word_dict-a dictionary where the keys are each distinct word in the file and the value for any given key is a list of every word that follows that key
# anywhere in the file.  
#==========================================
def next_words(fname):
    open_file=open(fname)
    word_list=open_file.read().split(' ')
    open_file.close()
    word_list_period=[]
    distinct_lst=[]
    for word_index in range(len(word_list)):
        if word_list[word_index][0]=='.':
            token=word_list[word_index].split('\n')
            for i in range(len(token)):     
                word_list_period.append(token[i])
        else:
            word_list_period.append(word_list[word_index])
    for word_index in range(len(word_list_period)):
        if word_list_period[word_index]!='.':
            if word_list_period[word_index] not in distinct_lst:
                distinct_lst.append(word_list_period[word_index])
    next_word_dict={}
    for unique_word in distinct_lst:
        next_word_dict[unique_word]=[]
        for word_index in range(len(word_list_period)-1):
            if word_list_period[word_index]==unique_word:
                next_word_dict[unique_word].append(word_list_period[word_index+1])
    return next_word_dict
#==========================================
# Purpose: Takes in a file name as a string representing the name of the file, and prints ten sentences with a randomly chosen first word(which is then used as a key in the dictionary
#produced by next_words).  The next word should be chosen at random from the list that is the value for that key.  
# Input Parameter(s): fname-a string representing the name of the file.
# Return Value(s): Nothing 
#==========================================
import random
def fanfic(fname):
    first_w_list=first_words(fname)
    next_w_dict=next_words(fname)
    for number in range(10):
        first_w=random.choice(first_w_list)
        sentence=first_w
        next_w=random.choice(next_w_dict[first_w])
        while next_w!='.':
            sentence=sentence+' '+next_w
            next_w=random.choice(next_w_dict[next_w])
        sentence=sentence+' '+next_w
        print (sentence)
#B)
#Purpose: Takes in a nested fictionary representing a directory and returns the total memory in bytes being used by the files.  
# Input Parameter(s): dictionary:a nested dictionary representing a directory. 
# Return Value(s): The total memory in bytes used by the files 
#==========================================
def total_txt_size(dictionary):
    if dictionary=={}:
        return 0
    else:
        first_key=list(dictionary.keys())[0]
        first_value=dictionary[first_key]
        dictionary.pop(first_key)
        if type(first_value) is int:
            return first_value+total_txt_size(dictionary)
        else:
            return total_txt_size(first_value)+total_txt_size(dictionary)
