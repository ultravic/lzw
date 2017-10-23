import dictionary

def decompress(infile):
    from cStringIO import StringIO

    ifile = open(infile, 'r')
    ofile = open(infile + '.lzw', 'w')

    # use StringIO, otherwordise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    word = chr(file.pop(0))
    result.write(word)
    for c in file:
        if c in dictionary:
            entry = dictionary[c]
        elif c == dictionarySize:
            entry = word + word[0]
        else:
            raise ValueError('Bad file c: %s' % c)
        result.write(entry)

        # Add word+entry[0] to the dictionary.
        dictionary[dictionarySize] = word + entry[0]
        dictionarySize += 1

        word = entry

    # Fechar os arquivos e retornar nome do output
    ifile.close()
    ofile.close()

    return ofile.name
