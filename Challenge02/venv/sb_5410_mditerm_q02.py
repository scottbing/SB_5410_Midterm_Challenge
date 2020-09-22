import string
import re

def process_file(fname, enc):
    #open file for 'r'eading
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()   #read file
        dat = perform_re(dat)
    return(dat.split())  #return read data
#end process_file(fname, enc):

def read_file(fname, enc, words):
    scores = []
    titles = []
    with open(fname) as fp:
        scores = []
        line = fp.readline()
        cnt = 1
        while line:
            line = perform_re(line)  # clean data
            print("Line {}: {}".format(cnt, line.strip()))
            titles.append(line)
            score = 0
            tokens = line.split()
            for t in tokens:
                if words[clean_word(t)] == 1:
                    score += 1
                    #print("unique score: ", score)
            line = fp.readline()
            cnt += 1
            #print("score for line", score)
            scores.append(score)
            #print("scores: ", scores)
        print("\nThis is the sentence with the most unique words: ",
              titles[scores.index(max(scores))])
#end process_file(fname, enc):

def write_results(fname, data, enc):
    #open file for 'w'riting
    with open(fname, 'w', encoding = enc) as file:
        file.write(data)
#end def write_results(fname, data, enc):

def write_lines(fname, data, enc):
    #open file for 'w'riting
    with open(fname, 'w', encoding = enc) as file:
        file.write(data)
#end def write_results(fname, data, enc):

def words_to_dict(all_words, dictionary):
    for w in all_words: #for each word
        w = clean_word((w))
        if w in dictionary:  #if the word was counted before
            dictionary[w] += 1  #increment te count
        else:
            dictionary[w] = 1   #begin count for a new word
#end def word_to_dict(all_words, dictionary):

def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")
    return word.lower() #return the word as lowercase
#end def clean_word(word):

def perform_re(text):
    #text = re.sub(r'(CHAPTER) ([IVXLC]+.)', '\\1\\2', text)
    text = re.sub(r'\d+\.(.+)', '\\1', text)
    text = re.sub("\([A-Z0-9.'\s]+\)", "", text)
    return text

def main():
    # first pass - esablish dictionary of unique words
    unique_words = {}   #dictionary for word counts
    words = process_file("songs.txt", "utf-8")
    words_to_dict(words, unique_words)

    # put data back into lines and score the titles
    read_file("songs.txt", "utf-8", unique_words)

    # print results
    print("Found {0} total words.".format(len(words)))
    print("Found {0} unique words.".format(len(unique_words.keys())))

    print("Raw TTR: ", len(unique_words.keys()) / len(words))
    print("Pct TTR: ", str(round((len(unique_words.keys()) / len(words))*100)) + "%")

    #join the words in the list with new line char
    write_results("perline.txt", "\n".join(words), "utf-8")
#end of main():

if __name__ == "__main__":
    main()