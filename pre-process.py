import os
import sys
#author - Matthew Cattaneo


def build_vocab(file_path):
    lines = []
    with open(file_path, 'r',encoding ="utf8", errors="ignore") as file:
        for line in file:
            cleaned_line = line.strip()
            lines.append(cleaned_line)
    return lines

def read_text_files(folder_path, vocab):
    os.chdir(folder_path)
    
    clean_sentences = []
    for file_name in os.listdir():
        with open(file_name,'r',encoding ="utf8", errors="ignore") as file:
            content = file.read()
            content = count_and_tokenize(content, vocab)
            clean_sentences.append(content)
            
    return clean_sentences

def word_tokenize(content):
    content = content.lower()
    content = content.replace("<br />", " ")
    
    punc = '''()-[]{};:'"\!,<>.?/@#$%^&*_~'''
    for ele in content:
        if ele in punc:
            content = content.replace(ele, "")

    content = content.split()
    return content


def count_and_tokenize(content, vocab):
    
    content = word_tokenize(content)

    for token in content:
        if token in vocab:
            if vocab[token] is None:
                vocab[token] = 1
            else:
                vocab[token] += 1
    return content

def clean_sentence(content):
    content = content.lower()

#sort vocab by most n frequent words
def sort_vocabulary(dictionary, n):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    top_n = dict(sorted_items[:n])
    return top_n


stop_words = [
'therein', 'do', 'she', 'should', 'hr', 'z', 'pi', 'qv', 'might', 'ax', 'ru', 'y', 'end', "hasn't", 'lately', 'les', 'couldn', 'j', 'p3', 'call', 'new', 'or', 'jr', 'cannot', 'going', 'just', 'meantime', 'co', 'look', 'behind', 'nd', 'dr',
 'very', 'since', 'cx', 'ran', 'seriously', 'ur', 'added', 'part', 'usefulness', 'fify', "what'll", 'cf', 'which', 'specifying', "you're", 'more', 'indicates', 'twice', 'p', 'tb', 'sm', 'unlikely', 'youll', 'uses', 'ju', 'amongst', 'according',
   'cu', 'related', 'sufficiently', 'hu', 'ill', 'b1', 'eo', 'elsewhere', 'become', 'eleven', 'becoming', 'sl', 'anyhow', 'de', 'anyone', 'specify', 'xj', 'youd', 'gets', 'youre', 'thanx', 'yr', 'etc', 'fifth', 'previously', 'od', 'course', 'may',
     'hers', 'tp', 'act', 'latter', 'don', 'there', 'throug', 'h3', "i've", 'mt', 'jj', 'fi', 'fc', "there've", 'volumtype', 'nj', "i'll", 'sa', 'still', 'sent', 'fl', 'too', 'therere', 'bu', 'da', 'pk', 'mu', 'readily', 'upon', 'appear', "what's",
       'aw', 'regarding', 'except', 'sr', 'nn', 'cg', 'es', 'index', 'means', 'ns', 'likely', 'ev', 'take', 'it', 'describe', 'under', 'f2', 'rf', 'various', 'a4', 'does', 'a2', 'bx', 'eighty', 'ng', 'primarily', 'ir', 'whereas', 'xk', 'right', 'c3',
         'because', 'would', 'dy', 'ba', 'done', 'eight', 'pf', 'whereafter', 'lt', 'run', 'substantially', 'dx', 'follows', 'obtained', 'wasn', 'ab', 'gy', 'after', 'nowhere', 'me', 'example', 'three', 'greetings', 
'using', 'what', 'fn', 'ec', 'g', "mustn't", 'getting', "don't", 'section', 'em', 'similar', 'ts', 'be', 'therefore', 'known', '3d', 'rather', 'se', 'regards', 'seven', 'tq', 'outside', 'ue', 'merely', 'ry', 'corresponding',
 'didn', 'happens', 'besides', 'either', 'ff', 'cj', "didn't", 'iq', 'mug', 'pagecount', 'ui', 'the', 'um', 'wont', 'www', "needn't", 'hj', 'from', 'k', 'successfully', 'ending', 'keep', 'won', 'back', 'showns', 'a3', 'dp', 'immediately', 'her',
   'iy', 'rc', 'ke', 'owing', 'apparently', 'not', "shan't", 'especially', 'hundred', 'importance', 'thered', 'et-al', 'seems', 'has', 'shes', 'xn', 'hes', 'while', 'selves', 'aj', 'through', 'js', 'invention', 'formerly', 'wed', 'n2', 'predominantly',
     'anything', 'poorly', 'whim', 'move', 'xs', 'ej', "how's", 't1', 'whose', 'on', 'dt', 'these', 'could', 'following', 'past', 'q', 'youve', 'hi', 'ma', 'ms', 'f', 'appropriate', 'its', 'mo', 'auth', 'that', 'uo', 'nc', 'four', 'ow', 'c1',
       'somewhat', 'tt', 'onto', 'bill', 'thereto', 'si', 'a', 'pas', 'beginning', "a's", 'everything', 'necessary', 'dj', 'needn', 'also', 'oo', 'placed', 'really', 'rt', 'wouldnt', 'cry', 'away', 'theirs', "mightn't", 'furthermore', 'arent',
         's2', 'serious', 'via', 'better', 'necessarily', 'itself', 'significant', 'to', 'him', 'put', 'ive', 'v', 'particular', 'help', 'interest', "haven't", 'ro', 'get', 'similarly', "why's", 't3', 'ref', 'seemed', 'en', 'sn', 'stop', 'resulted',
           'front', 'are', 'whereupon', 'vq', 'pj', 'wouldn', 'ac', 'ln', 'im', 'present', 'tl', 'yours', 'first', 'df', 'ri', 'e3', 'said', 'tn', 'p1', 'thereupon', 'ignored', 'whole', 'however', 'down', 'cq', 'bd', 'some', 'he', 'fa', 'no', 'per',
             'less', 'ft', 'here', 'indicated','m', 'howbeit', 'sd', 'neither', 'even', 'ah', 'i8', 'va', 'allows', 'x1', "he's", 'thereafter', 'haven', 'cant', 'hid', 'ra', '6o', 'theres', "here's", 'ibid', 'mine', 'ee', 'empty', 'lj', 'xo', 'below',
               'between', "who'll", "aren't", 'eu', 'affecting', 'nothing', 'used', 'goes', 'tip', 'again', 'whatever', 'any', 'home', 'indicate', 'i2', 'io', 'thousand', 'sy', 'noted', 'gl', 'nr', 'y2', 'them', 'twenty', "c's", 'by',
                 'gave', 'rl', 'strongly', 'fj', 'bt', 'omitted', 'sj', 'everyone', 'biol', 'yourself', 'i', 'consider', 'shall', 'other', "that's", 'towards', 'whether', 'several', 'ad', 'please', 'unlike', 'a1', 'ih', 'needs', 'hasn', '3b',
                   'recently', 'fy', 'gs', 'ml', 'xt', 'often', 'system', 'p2', 'ef', 'sf', 'vols', 'effect', 'potentially', 'que', 'apart', 'try', 'oh', 'edu', "we're", 'arise', 'world', 'sometime', 'own', 'due', 'together', 'refs', 'oj', 'dk',
                     'gi', 'op', 'yourselves', 'somebody', 'oa', 'whomever', 'off', 'thank', 'respectively', 'il', 'na', 'this', 'now', 'both', 'at', "he'll", 'around', 'non', 'vd', 'et', 'i7', 'noone', 'causes', 'mustn', 'followed', 'against',
                       'dc', 'ut', 'among', "should've", 'ct', 'brief', 'seeing', "it'll", 'showed', 'tends', 'x3', 'considering', 'sp', 'miss', 'they', 'give', 'par', "can't", 'bn', 'mainly', 're', 'usefully', 'theyve', 'bl', '6b', 'hello', 'about',
                         'di', 'abst', 'couldnt', 'largely', 'wheres', 'whither', 'thorough', 'two', 'whereby', 'film','l2', 'thickv', 'have', 'tried', 'beginnings', 'theyd', "you'll", 'gone', 'think', 'sup', 'thou', 'ic', 'herself', 'research-articl',
 'same', 'further', 'see', 'herein', 'everybody', 'information', 'nl', 'and', 'ph', 'reasonably', 'sub', 'ain', 'el', 'we', 'ch', 'had', 'ij', 'million', 'second', 'ce', 'ip', 'made', 'show', '0o', 'such', 'amount', 'anybody', 'changes', 'able', 'zz',
   'fu', 'suggest', 'com', 'pp', 'appreciate', 'pn', 'taken', 'fs', 'only', 'e', 'd2', 'thus', 'each', 'r2', 'side', 'thoroughly', 'vo', 'alone', 'find', 'detail', 'with', 'vt', 'ix', 'tr', 'oc', 'moreover', 'uj', 'containing', 'best', 'date', 'need',
     'vol', 'ex', 'thence', 'though', 'says', 'ne', 'eg', 'like', 'av', 'oq', 'kg', 'yl', 'pe', 'h', 'toward', 'ei', 'xl', 'td', 'hs', 'if', 'tv', 'were', "they'll", 'our', 'associated', 'ups', 'widely', 'above', 'page', 'theyll', 'rh', 'vs', "t's",
       'az', 'one', 'whom', 'otherwise', 'hopefully', 'doing', 'amoungst', 'seen', "that'll", 'x2', 'br', 'sometimes', 'looks', 'qj', 'whats', 'itd', 'next', 'rq', 'anyway', 'ds', 'po', 'rs', 'saw', 'ga', 'given', 'seeming', 'themselves', 'overall',
         "they've", "i'm",'pages', "that've", 'way', 'au', 'allow', 'unless', 'ge', 'novel', 'none', 'welcome', 'n', 'cr', 'whens', 'viz', 'wa', 'ever', 'lo', "isn't", 'tc', 'ay', 'fill', 'forth', 'ie', 'lets', 'ti', 'u201d', "i'd", 'cc', 'ib', 'gj',
           'ten', 'will', 'pc', 'research', 'recent', 'beyond', 'someone', "it's", 'former', 'mn', 'else', 'found', 'concerning', 'can', 'heres', 'ig', 'available', 'cm', 'l', "they'd", 'shown', 'over', 'cs', 'something', 'somewhere', "doesn't", 'nt',
             'ones', 'pu', 'wants', 'results', 'make', 'liked', 'nobody', 'my', 'bi', 'many', 'near', 'sz', 'value', 'lf', 'contain', 'sorry', 'old', 'oi', 'cit', 'somehow', 'aside', 'zero', "we'd", 'although', 'exactly', 'unto', 'briefly', 'ed', 'd',
               'mrs', 'cn', 'latterly', 'ought', 'ok', 'af', 'immediate', 'ord', 'mean', 'provides', 'use', 'whod', 'yj', "they're", 'giving', 'trying', 'wi', 'went', 'anymore', 'weve', 'bs', 'least', 'let', 'always', 'bk', 'come', 'm2', 'thats', 'ae',
                 'hence', 'shan', 'came', 'name', "he'd", 'xf', 'mightn', 'ox', 'up', 'tj', 'wherever', 'never', 'rd', 'ci', 'somethan', 'hardly', 'others', 'whoever', 'within', 'ask', "wouldn't", 'obviously', 'want', 'sixty', 'werent', 'whys', 'ar',
                   'every', 'before', 'ot', 'keeps', 'doesn', 'bottom', 'having', 'th', 'c2', 'ap', 'his', 'dd', 'usually', 'ia', 'six', 'cd', '3a', 'entirely', 'os', "there'll", 'say', 'xv', 'ls', 'almost', 'of', 'soon', 'maybe', 'b2', 'into',
                     'perhaps', 'enough', 'shed', 'tell', 'affects', 'you', 'awfully', 'er', 'affected', 'words', 'insofar', 'full', 'hereby', 'hows', 'le', "ain't", 'st', 'gives', 'quite', 'whenever', 'plus', 'km', 'well', 'sq', 'got', 'yet',
                       'clearly', 'gotten', 'kept', 'how', 'hither', 'isn', "shouldn't", 'third', 'e2', 'last', 'significantly', 'quickly', 'h2', 'r', 'anyways', 'pd', 't', 'bp', '0s', 'qu', 'relatively', 'specifically', 'than', "where's", 'iv',
                         'rm', 'fo', 'la', 'is', 'downwards', 'comes', 'wish', 'your', 'ni', 'fire', 'oz', 'al', 'line', 'out', "you'd", 'tf', 'begin', 'thru', 'b3', 'obtain', 'cp', 'across', 'where', 'most', 'ii', 'b', 'so', 'py', 'ho', 'jt',
                           'hy', 'useful', 'five', "you've", 'accordingly', 'forty', 'nay', 'sincere', 'yt', 'himself', 'fr', 'whence', 'in', 'definitely', 'been', 'ea', 'ey', 'know', 'until', "when's", 'specified', 'og', 'http', 'promptly',
                             "we'll", 'later', 'ninety', 'rj', 'tx', 'us', 'presumably', 'was', "we've", 'hereafter', 'an', 'du', 'hereupon', 'anywhere', 's', 'shouldn', 'shows', 'becomes', 'te', 'those', 'theyre', 'important', 'possibly',
                               'ps', 'twelve', 'cause', 'wonder', 'ag', 'i6', 'bc', 'ours', 'different', 'ao', 'self', 'thereby', 'another', "wasn't", 'certainly', 'inward', 'meanwhile', 'thoughh', 'truly', 'uk', 'inner', 'described',
                                 'particularly', 'but', 'til', 'hh', 'o', 'ss', 'id', 'adj', 'pl', 'wo', 'during', 'far', 'proud', "couldn't", 'inc', 'pt', 'weren', 'well-b', 'lc', 'all', 'possible', 'knows', "it'd", 'everywhere', 'vj',
                                   'pr', 'hed', 'ourselves', 'begins', 'actually', 'hadn', 'u', 'fix', 'much', 'ca', 'thereof', 'currently', "she'll", 'when', 'gr', 'slightly', 'con', 'xx', 'asking', 'taking', 'i3', 'became', "she's",
                                     'approximately', 'lr', 'took', 'aren', 'ol', 'seem', 'c', 'announce', 'secondly', 'throughout', 'ep', 'as', 'zi', 'wasnt', 'om', 'then', 'sc', 'un', 'without', "let's", 'their', 'thin', 'already',
                                       'vu', "weren't", 've', 'sensible', "c'mon", 'who', 'little', 'inasmuch', 'whos', 'go', 'nonetheless', 'rv', 'lb', 'namely', 'll', 'est', 'consequently', 'makes', 'nevertheless', 'okay', 'pq',
                                         'regardless', 'nine', 'did', 'cv', 'indeed', 'ys', 'sec', 'yes', 'certain', 'lest', 'believe', 'wherein', 'movie', 'few', 'ob', 'pm', 'mg', 'mr', 'must', 'unfortunately', 'why', 'am',
                                           'saying', 'along', 'myself', 'tries', 'tm', 't2', 'accordance', 'i4', 'for', "won't", 'nearly', 'contains', 'instead', 'cl', 'thanks', 'cz', 'mill', 'looking', 'dl', 'once', 'rn',
                                             "hadn't", 'being', 'nor', 'ny', 'ou', 'beside', 'normally', 'probably', 'top', 'willing', "there's", 'rr', 'x', 'resulting', 'xi', 'nos', 'bj', 'cy', 'eq', 'iz', 'los', 'ltd',
                                               'despite', 'sure', 'mostly', 'afterwards', 'fifteen', 'ko', 'beforehand', 'hasnt', "she'd", 'w', 'kj',"dont","characters","scenes","watching","years","thing","didnt","lot","cast","young","horror","series","long","times","comedy","music","making","day","played","book","actor","john","shot","simply",
                                               "year","death","performances","wrong","hollywood","couple","sex","dialogue","absolutely","live","budget","style","problem","cinema","boy","white","based","mother","guys","friend","children","guess","lead","writing","works","called","michael","quality","son","kill","flick","eyes","town",
                                               "car","parts","actress","child","genre","stories","thinking","directed","late","blood","close","fight","heard","killed","kid","police","involved","violence","told","james","murder","including","coming", "story","movies,","films","good","watch","character","life","man","scene","doesnt","actors","work","director",
                                               "things","pretty","fact","big","thought","isnt","point","role","feel","girl","woman","place","money","set","screen","worth","watched","dvd","takes","play","beautiful","version","audience","left","night","special","american",
                                               "high","kids","black","fan","star","mind","men","classic","rest","short","dead","production","women","camera","small","video","face","felt","person","lost","piece","case","written","head","title", "picture","fans",
                                               "care","killer","dark", "final","fine", "totally","history","girls", "time", "people", "acting","plot","script","performance","read","job","main","movies","episode","playing","finally","human"]
def remove_stop_words(vocab):
    for word in stop_words:
        if word in vocab:
            del vocab[word]
    
    return vocab
def create_file(output,vocab, example, label):
    
    for sent in example:

        output.write(label)
        output.write(" ")
        for feature in vocab:
            if feature in sent:
                val = "1"
            else:
                val = "0"
            output.write(val)
            output.write(" ")

        output.write("\n")
                

def main():
  #feature_length set to 60 by default, given best results in evaluation
  FEATURE_LENGTH = 60
  #if statement which runs pre-process when all args are given
  if(len(sys.argv) >= 4):  
    terms = build_vocab(sys.argv[1])
    vocab = {term: 0 for term in terms}
    script_folder = os.path.dirname(os.path.abspath(__file__))
    pos_folder = os.path.join(script_folder, sys.argv[2], 'pos')
    neg_folder = os.path.join(script_folder,sys.argv[2], 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)
    vocab = remove_stop_words(vocab)
    vocab = sort_vocabulary(vocab, FEATURE_LENGTH)
  
    output = open(os.path.join(script_folder,'train_data.txt'),"w")

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()

    output = open(os.path.join(script_folder,'test_data.txt'),"w")
    pos_folder = os.path.join(script_folder, sys.argv[3], 'pos')
    neg_folder = os.path.join(script_folder, sys.argv[3], 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()
    #no args given use default values
  elif(len(sys.argv)==1):
    terms = build_vocab("imdb.vocab")
    vocab = {term: 0 for term in terms}
    script_folder = os.path.dirname(os.path.abspath(__file__))
    pos_folder = os.path.join(script_folder, "train", 'pos')
    neg_folder = os.path.join(script_folder, "train", 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)
    vocab = remove_stop_words(vocab)
    vocab = sort_vocabulary(vocab, FEATURE_LENGTH)
  
    output = open(os.path.join(script_folder,'train_data.txt'),"w")

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()

    output = open(os.path.join(script_folder,'test_data.txt'),"w")
    pos_folder = os.path.join(script_folder, "train", 'pos')
    neg_folder = os.path.join(script_folder, "train", 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()
    file = open(os.path.join(script_folder,"vocab.txt"), "w")
    for word in vocab:
      file.write(word)
      file.write(" ")
    file.close()
    #just the train foder is given
  else:
    FEATURE_LENGTH = int(sys.argv[2])
    terms = build_vocab("imdb.vocab")
    vocab = {term: 0 for term in terms}
    script_folder = os.path.dirname(os.path.abspath(__file__))
    pos_folder = os.path.join(script_folder, "train", 'pos')
    neg_folder = os.path.join(script_folder, "train", 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)
    vocab = remove_stop_words(vocab)
    vocab = sort_vocabulary(vocab, FEATURE_LENGTH)
  
    output = open(os.path.join(script_folder,'train_data.txt'),"w")

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()

    output = open(os.path.join(script_folder,'test_data.txt'),"w")
    pos_folder = os.path.join(script_folder, "train", 'pos')
    neg_folder = os.path.join(script_folder, "train", 'neg')
    pos_examples = read_text_files(pos_folder, vocab)
    neg_examples = read_text_files(neg_folder, vocab)

    create_file(output,vocab,pos_examples,"1")
    create_file(output,vocab,neg_examples,"0")
    output.close()
    file = open(os.path.join(script_folder,"vocab.txt"), "w")
    for word in vocab:
      file.write(word)
      file.write(" ")
    file.close()



    

if __name__ == "__main__":
    main()