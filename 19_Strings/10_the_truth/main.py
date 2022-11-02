text2 = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
        'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
        'fTjnqm tj scfuuf ibou fy/dpnqm ' \
        'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
        'uGmb tj fuufsc ouib oftufe/ ' \
        'bstfTq jt uufscf uibo otf/ef ' \
        'uzSfbebcjmj vout/dp ' \
        'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
        'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
        'Fsspst tipvme wfsof qbtt foumz/tjm ' \
        'omfttV mjdjumzfyq odfe/tjmf ' \
        'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
        'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
        'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
        'xOp tj scfuuf ibou /ofwfs ' \
        'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
        'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
        'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
        'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip '
abc = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ` , (, ,, -, ., /, *, +, ", !'
temp_word = ''
shift = 3
word = ''
switch = 1
switch_on = 1
def words3(shift, wor):
    temp = ''
    new_word = ''
    temp += wor[len(wor) - shift::] + wor[:len(wor) - shift:]
    for i in range(len(temp)):
        for u in range(len(abc)):
            if temp[i].lower() == abc[u].lower():
               new_word += abc[u - 3:u - 2:]
    return new_word

for i in text2:
    if i != " ":
        temp_word += i
    elif i == " ":
        if len(temp_word) == 2:
            word += (words3(shift, temp_word[::switch]))
            temp_word = ''
        if len(temp_word) != 2:
            word += (words3(shift, temp_word)) + " "
        for u in temp_word:
            if u == "/":
                shift += 1
                word += "\n"
                switch_on += 1
                if switch_on %2 == 0:
                    switch = 1
                if switch_on % 2 != 0:
                    switch = -1
        temp_word = ''
print(word)
