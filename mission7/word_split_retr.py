from collections import deque

def word_split(src, words, blacklist):
    'modify because of maximum recursion depth'
    step = 5
    result = deque()

    def work_with_tail(src):
        'has limit of maximum recursion depth in Python'
        if not src:
            return
        end = len(src)
        it = end - step
        if it < 0:
            it = 0
        for lset in range(it, end):
            w = src[lset:end]
            if w in words or w in blacklist:
                # if w not in blacklist:
                #     result.appendleft(w)
                result.appendleft(w)
                tmp = src[:lset]
                # work_with_tail(tmp)
                # return
                return tmp
        # result.appendleft(src[-1])
        tmp = src[:-1]
        # work_with_tail(tmp)
        return tmp

    # work_with_tail(src)
    tmp = src
    while tmp:
        tmp = work_with_tail(tmp)
    return result


if __name__ == '__main__':
    from xlsx_reader import read_words_from_col
    words = read_words_from_col('./词表/words.xlsx')
    stopwords = read_words_from_col('./词表/stopwords.xlsx', True)
    res = word_split('    习近平在讲话中指出，以胡锦涛同志为总书记的党中央，团结带领全国各族人民，取得了举世瞩目的辉煌成就。为了党和人民事业继往开来，胡锦涛同志，以及吴邦国、温家宝、贾庆林、李长春、贺国强、周永康等同志，带头退出党中央领导岗位，体现了崇高品德和高风亮节。我们向他们致以崇高的敬意。', words, stopwords)
    print(res)
