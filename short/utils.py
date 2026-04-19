import string

ALPHABET = string.digits +string.ascii_lowercase+string.ascii_uppercase

def encode_url(id:int)->str:
    if id == 0:
        return ALPHABET[0]
    arr = []
    base = len(ALPHABET)
    while id:
        id,rem= divmod(id,base)
        arr.append(ALPHABET[rem])

    arr.reverse()
    return ''.join(arr)

def decode(id:str)->int:
    base = len(ALPHABET)
    num= 0
    for i in id:
        num = num*base + ALPHABET.index(i)
    return num



