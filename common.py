def lmap(func, iterable):
    return list(map(func, iterable))

def split_strip(s, sep=' '):
    return [e.strip() for e in s.split(sep)]

def lbin(num, length=0):
    b = bin(num)[2:]
    return '0'*max(length - len(b), 0) + b
