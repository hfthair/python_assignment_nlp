import os
from xlsx_reader import read_words_from_col
from word_split_retr import word_split

def main():
    out_dir = './output'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    words = read_words_from_col('./词表/words.xlsx')
    stopwords = read_words_from_col('./词表/stopwords.xlsx', True)
    ld = os.listdir('./分词文本')
    total = len(ld)
    cnt = 0
    for i in ld:
        cnt = cnt + 1
        print('\r', end='')
        print('{}/{} ====> {}'.format(cnt, total + 1, i)[0:80], end='')
        path = os.path.join('./分词文本', i)
        if os.path.isfile(path) and path.endswith('.txt'):
            with open(path, encoding='utf8') as f:
                src = f.read()
                res = word_split(src, words, stopwords)
                out_file = os.path.join(out_dir, i)
                with open(out_file, 'w', encoding='utf8') as out:
                    out.write('/'.join(res))
    print('\ndone. files output in {}'.format(out_dir))

if __name__ == '__main__':
    main()
