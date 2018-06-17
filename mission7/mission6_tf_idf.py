import os
import math
from xlsx_reader import read_words_from_col
from word_split_retr import word_split

def main():
    words = read_words_from_col('./词表/words.xlsx')
    stopwords = read_words_from_col('./词表/stopwords.xlsx')
    ld = os.listdir('./分词文本')
    total = len(ld)
    cnt = 0
    occurs = {}
    stack = {}
    for i in ld:
        cnt = cnt + 1
        # if cnt > 2:
        #     break
        print('\r', end='')
        print('sp: {}/{} ====> {}'.format(cnt, total + 1, i)[0:80], end='')
        path = os.path.join('./分词文本', i)
        if os.path.isfile(path) and path.endswith('.txt'):
            with open(path, encoding='utf8') as f:
                o = {}
                src = f.read()
                res = word_split(src, words, stopwords)
                for j in res:
                    if j in o:
                        o[j] = o[j] + 1
                    else:
                        o[j] = 1
                        if j in stack:
                            stack[j] = stack[j] + 1
                        else:
                            stack[j] = 1
                occurs[i] = o

    print('')
    out_dir = './tfidf_output'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    cnt = 0
    libsize = len(occurs)
    for i in occurs:
        cnt = cnt + 1
        tfidf = {}
        print('\r', end='')
        print('tfidf: {}/{} ====> {}'.format(cnt, libsize + 1, i)[0:80], end='')
        for j in occurs[i]:
            tf = occurs[i][j]
            cnt = stack[j]
            idf = math.log(libsize/cnt+1)
            tfidf[j] = tf * idf
        s = sorted(tfidf, key=tfidf.get, reverse=True)
        out_file = os.path.join(out_dir, i)
        with open(out_file, 'w', encoding='utf8') as out:
            out.write('\n'.join(s))
    print('\ndone! file output in {}'.format(out_dir))

if __name__ == '__main__':
    main()
