import random
starters = [('I do know', 3), ('Once', 1), ('Never', 1), ('please', 1), ('always', 2), ('sometimes', 3),
            ('Suprising', 3), ('everyone', 3)]
transition = [('where', 2), ('on', 1), ('through', 1), ('by', 1), ('never', 2), ('always', 2), ('sometimes', 3),
              ('in', 1), ('suddenly', 3)]
subject = [('Milk', 1), ('Strawberrys', 3), ('Penguins', 3), ('Pillow', 2), ('Christmas', 2), ('nap', 1),
           ('night', 1), ('car', 1), ('toilet', 2), ('toilet paper', 4), ('weed', 1), ('Darmstadt', 2), ('bunny', 1),
           ('toes', 1), ('window', 2), ('beach', 1), ('snow', 1),
           ('nuthouse', 2), ('church', 1), ('failure', 2), ('God', 1)]
adjectiv = [('Christmas', 2), ('white', 1), ('red nose', 2), ('more', 1), ('less', 1), ('on', 1), ('away', 1),
            ('wise', 1), ('naked', 2), ('romantic', 2),
            ('fail', 1), ('suprisingly', 3)]
storyend = [('go white', 2), ('get drunk', 2), ('get naked', 3)]

articles = [('A', 1), ('The', 1)]
biverbs = [('take', 1), ('make', 1), ('steal', 1), ('ironing', 2), ('smell', 1), ('get naked', 3), ('taste', 1)]
verb = [('struggle', 2), ('take', 1), ('make', 1), ('steal', 1), ('ironing', 2), ('smell', 1), ('do', 1),
        ('get naked', 3), ('taste', 1)]
ref = {
    'a': articles,
    's': starters,
    't': transition,
    'n': subject,
    'e': storyend,
    'v': verb,
    'b': biverbs,
    'd': adjectiv
}

sentences = ['san', 'ane', 'sban', 'nbn', 'dnbn', 'nbdn', 'adnbn', 'anbn', 'anbdn', 'svn', 'vdn', 'vdntn', 'nve', 'vtn']


def getline(val):
    psntc = list(sentences)

    def choosepart(sntc, val):
        if sntc == '':
            return ''
        possb = list(filter(lambda tp: tp[1] < val if len(sntc) > 1 else tp[1] == val, ref[sntc[0]]))
        remainder = None
        word = None
        while remainder is None:
            if word is not None:
                possb = [v for v in possb if v[0] != word]
            if len(possb) == 0:
                return None

            word, sil = random.choice(possb)
            remainder = choosepart(sntc[1:], val - sil)

        return word + " " + remainder

    line = None
    while line is None:
        if len(psntc) == 0:
            return None
        sntc = random.choice(psntc)
        psntc = [s for s in psntc if s != sntc]
        line = choosepart(sntc, val)

    return line


def gethaiku():
    return getline(5) + '\n' + getline(7) + '\n' + getline(5)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generates haikus')
    parser.add_argument('num', type=int, default=1,
                        help='number of haikus to generate')

    args = parser.parse_args()
    for i in range(args.num):
        print(gethaiku())
        print("")
