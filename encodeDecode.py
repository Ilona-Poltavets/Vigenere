# Create dictionary of symbols
def form_dict():
    d = {}
    iter = 0
    for i in range(31, 127):
        d[iter] = chr(i)
        iter = iter + 1
    return d

d=form_dict()

# key to dictionary
def encode_val(word):
    list_code = []
    lent = len(word)
    global d

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
                list_code.append(value)
    return list_code


# key-value mappings
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i, key[iter]]
        full = full + 1
        iter = iter + 1
        if (iter >= len_key):
            iter = 0
    return dic


# decode text
def full_encode(valueInput, keyInput):
    value=encode_val(valueInput)
    key=encode_val(keyInput)
    dic = comparator(value, key)
    lis = []
    global d

    for v in dic:
        go = (dic[v][0] + dic[v][1]) % len(d)
        lis.append(go)
    return ''.join(decode_val(lis))


def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    global d

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
                list_code.append(d[value])
    return list_code


# decode text
def full_decode(valueInput, keyInput):
    value = encode_val(valueInput)
    key = encode_val(keyInput)
    dic = comparator(value, key)
    global d
    lis = []

    for v in dic:
        go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
        lis.append(go)
    return ''.join(decode_val(lis))