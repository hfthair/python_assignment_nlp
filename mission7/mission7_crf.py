import os


def get_marks_for_word(word):
    if len(word) == 1:
        return ['BE']
    elif len(word) > 1:
        marks = ['M'] * len(word)
        marks[0] = 'B'
        marks[-1] = 'E'
        return marks
    else:
        raise Exception('word len == zero!')

def main():
    #generate train and test file
    print('# generating training file and test file')
    ld = os.listdir('./output')
    total = len(ld)
    cnt = 0
    lines = []
    for i in ld:
        cnt = cnt + 1
        print('\r', end='')
        print('  read {}/{} ====> {}'.format(cnt, total + 1, i)[0:30], end='')
        path = os.path.join('./output', i)
        if os.path.isfile(path) and path.endswith('.txt'):
            with open(path, encoding='utf8') as f:
                src = f.read()
                lines.extend([e.strip() + '。' for e in src.split('。') if e.strip()])
    print('')
    print('  shuffle...')
    import random
    random.shuffle(lines)
    print('  generate file...')
    deli = len(lines) * 9 // 10
    trains = lines[:deli]
    tests = lines[deli:]
    out_dir = './m7out'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    out_train_file = os.path.normcase(os.path.join(out_dir, 'trains.txt'))
    with open(out_train_file, 'w', encoding='utf8') as out:
        for i in trains:
            words = [e.strip() for e in i.split('/') if e.strip()]
            if words:
                for word in words:
                    marks = get_marks_for_word(word)
                    l = map(lambda x, y: x + '\t' + y + '\n', word, marks)
                    s = ''.join(l)
                    out.write(s)
                out.write('\n')
    print('  ok -> ' + out_train_file)

    out_test_file = os.path.normcase(os.path.join(out_dir, 'tests.txt'))
    with open(out_test_file, 'w', encoding='utf8') as out:
        for i in tests:
            words = [e.strip() for e in i.split('/') if e.strip()]
            if words:
                for word in words:
                    marks = get_marks_for_word(word)
                    l = map(lambda x, y: x + '\t' + y + '\n', word, marks)
                    s = ''.join(l)
                    out.write(s)
                out.write('\n')
    print('  ok -> ' + out_test_file)
    print('training file and test file OK!')

    print('# start train...')
    crf_template_path = '.\\crf++tools\\template'
    test_tool_path = '.\\crf++tools\\crf_test.exe'
    train_tool_path = '.\\crf++tools\\crf_learn.exe'
    res = os.system('.\\crf++tools\\crf_learn.exe .\\crf++tools\\template ' + out_train_file + ' model')
    if res == 0:
        print('# start test...')
        crf_output = os.path.normcase(os.path.join(out_dir, 'output.txt'))
        os.system('.\\crf++tools\\crf_test.exe -m model ' + out_test_file + ' > ' + crf_output)
        print('done.')
    else:
        print('error~')






if __name__ == '__main__':
    if True:
        main()
    else:
        i = '习近平/在/讲话中/指出/，/以/胡锦涛/同志/为/总书记/的/党中央/，/团结/带领/全国/各族人民/，/得了/目的/辉煌成就/。'
        words = [e.strip() for e in i.split('/') if e.strip()]
        if words:
            for word in words:
                marks = get_marks_for_word(word)
                l = map(lambda x, y: x + '\t' + y + '\n', word, marks)
                s = ''.join(l)
                print(s)
                # if len(word) == 1:
                #     print(word[0] + '\tBE\n')
                # else:
                #     line = '\tM\n'.join(word)
                #     line = line.replace('M', 'B', 1)
                #     line = line + '\tE\n'
                #     print(line)
