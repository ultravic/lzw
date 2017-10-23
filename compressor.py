import dictionary

def compress(infile):
    ifile = open(infile, 'r')
    ofile = open(infile + '.lzw', 'w')

    word = ""
    for c in file:
        wordc = word + c
        if wordc in dictionary:
            word = wordc
        else:
            dictionary.dictionarySize += 1
            dictionary.dictionary[dictionary.dictionarySize] = word
            word = c

    # Output the code for word.
    if word:
        dictionary.dictionarySize += 1
        dictionary.dictionary[dictionary.dictionarySize] = word
        
    # Fechar os arquivos e retornar nome do output
    ifile.close()
    ofile.close()

    return ofile.name
