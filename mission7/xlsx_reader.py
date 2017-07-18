'read xls'
import xlrd


def read_words_from_col(file_path, fix_stopword_err=False):
    'read second col from xls file'
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_index(0)
    words = []
    for i in range(1, sheet.nrows):
        tmp = sheet.cell(i, 1).value
        tmp = tmp.strip()
        if tmp:
            if fix_stopword_err and '\r\n' in tmp:
                hack_lit = tmp.split('\r\n')
                for j in hack_lit:
                    if j and j.replace('\r', '').replace('\n', ''):
                        j = j.replace('\r', '').replace('\n', '').strip()
                        words.append(j)
            else:
                words.append(tmp)
    return words


if __name__ == '__main__':
    reads = read_words_from_col('./词表/words.xlsx')
    print(reads)
