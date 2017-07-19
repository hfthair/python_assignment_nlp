import csv
from collections import namedtuple

def try_pick_info(src):
    page = ''
    year = ''
    vol = ''
    t = src.replace(':', ',')
    t = t.replace('.', ',')
    t = t.replace('，', ',')
    t = t.replace('）', ')')
    t = t.replace('（', '(')
    t = t.split(',')
    for i in t:
        i = i.strip()
        if '-' in i and i.replace('-', '1').replace(' ', '1').isdigit():
            page = i
        elif len(i) == 4 and i.isdigit():
            year = i
        elif '(' in i and i.replace('(', '1').replace(')', '1').replace(' ', '1').isdigit():
            vol = i
    xx = map(lambda x: src.find(x), [page, year, vol])
    xx = filter(lambda x: x > 0, xx)
    mm = len(src)
    for i in xx:
        if i < mm:
            mm = i
    other = src[:mm]
    return other, vol, year, page


def main():
    'null'
    Refs = namedtuple('Refs', ['author', 'title', 'other', 'vol', 'year', 'page', 'src'])
    pr = []
    with open('src.txt', 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line = line.replace('\n', '')
            src = line
            i = line.rfind(']')
            if i > 0 and line[i-2] == '[':
                froms = line[i+2:].strip('/ ')
                line = line[:i+2]
                i = line[:-6].rfind('.')
                if i > 0:
                    author = line[:i+1].strip('/ ')
                    title = line[i+1:].strip('/ ')
                    other, vol, year, page = try_pick_info(froms)
                    print(vol, year, page)
                    pr.append(Refs(author, title, other, 'p ' + vol, year, page, src))
                else:
                    raise Exception('222222: ' + src)
            else:
                raise Exception('11111111: ' + src)
    
    with open('o.csv', 'w', encoding='utf8') as f:
        csvw = csv.writer(f)
        csvw.writerows(pr)
        # for i in pr:
        #     t = map(lambda x:x.encode('gbk'), i)
        #     csvw.writerow(t)
            # x = ''.join(i[-2]) + '\n'
            # f.write(x)


if __name__ == '__main__':
    main()






