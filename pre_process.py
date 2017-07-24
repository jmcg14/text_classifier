import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer



def process_dir(dir):
    for x in dir:
        process_file(x)

def process_file(infile):
    stopwords = nltk.corpus.stopwords.words('english')
    wnl = WordNetLemmatizer()
    outdir ='/home/josh/Documents/COSC/projects/ML/datasets/bbc_processed/'
    outfile = outdir + str(infile.split('/')[-2]) + '-processed' + '/' + str(infile.split('/')[-1])

    with open(infile, 'r') as infile, open(outfile, 'w+') as outfile:
        #text = nltk.word_tokenize(infile.read().decode('utf8', 'ignore'))
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(infile.read().decode('utf8', 'ignore'))
        text_lower = [x.lower() for x in text]
        text_filtered = [word for word in text_lower if word not in stopwords]
        lemma_list = [wnl.lemmatize(x) for x in text_filtered]
        print outfile
        for x in lemma_list:
            outfile.write(x.encode('utf8') + ' ')
