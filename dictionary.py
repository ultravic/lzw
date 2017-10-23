def init():
    global dictionary
    global dictionarySize
    dictionarySize = 256;
    dictionary = dict((index, chr(index)) for index in xrange(dictionarySize))
