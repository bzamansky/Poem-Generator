import nltk, re, nltk.data, curses, random, shelve
from curses.ascii import isdigit
from nltk.corpus import cmudict

words = open("words.text").readlines()
words = [x.strip().lower() for x in words]
words = list(set(words))
words.sort()
d = cmudict.dict()
sylls = {'0':[]}

nouns = {}
verbs = {}
adjectives = {}
adverbs = {}

regexp = "[A-Za-z]+"
apos = ".*'.*"
exp = re.compile(regexp)
exp2 = re.compile(apos)


def nysl(word):
    try:
        return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
    except:
        return "word is not in cmudict"




def makeSyllablesDict():
    sylls = shelve.open("syl")
    for a in words:
        key = str(nysl(a)[0])
        if exp.match(a) and not exp2.match(a):
            if key in sylls:
                l = sylls[key]
                l.append(a)
                sylls[key] = l
            else:
                sylls[key] = [a]
        #print a +" " + str(nysl(a)[0])  
   # print sylls
    return sylls

def getDict():
    syl = shelve.open("syl")
    return syl


#make a line of 10 syllables
def makeLine(x = 10):
    line = ""
    while x > 0:
        #get num of syllables
        if x > 8:
            num = random.randint(1,8)
        else:
            num = random.randint(1,x)
        #get random index
        y = random.randint(0,len(sylls[str(num)]))
        line+= sylls[str(num)][y]
        line+= " "
        x = x - num
    return line

def makeHaiku():
    s = ""
    s = s + makeLine(5) + '\n'
    s = s + makeLine(7) + '\n'
    s = s + makeLine(5)
    return s

def makeAdverbs():
    syl = shelve.open("syl")
    adverbs = shelve.open("adverbs")
    x = {}
    for item in syl:
        l = nltk.pos_tag(syl[item])
        x[item] = l
    #print x
    
    for item in x:
        adverbs[item] = []
        for word in x[item]:
            print word
            if word[1] == "ADV" or word[1] == "RB":
                l = adverbs[item]
                l.append(word)
                adverbs[item] = l
    return adverbs
        
def getNouns():
    nouns = shelve.open("nouns")
    return nouns

def getVerbs():
    verbs = shelve.open("verbs")
    return verbs

def getAdjectives():
    adjectives = shelve.open("adjectives")
    return adjectives

def getAdverbs():
    adverbs = shelve.open("adverbs")
    return adverbs

sylls = getDict()

#fours = sylls['4']
#parts = nltk.pos_tag(fours)

#nouns = getNouns()
#verbs = getVerbs()
#adjectives = getAdjectives()
#adverbs =getAdverbs()

#print makeHaiku()
