# Name: Victor Picussa
# GRR: 20163068

import pickle
import sys

def compress(infile):
    # Try open the infile, if doesn't exist, throw a error
    if infile:
        try:
            ifile = open(infile, 'r')
        except IOError:
            print("The file named '%s' doesn't exist or cannot be found" % infile)
        else:
            # Open the output file
            ofile = open(infile + '.lzw', 'wb')

            # Create the base dictionary
            dictionarySize = 256;
            dictionary = dict((chr(index), index) for index in xrange(dictionarySize))

            # LZW algorithm
            letters = ""
            linecp = []
            for word in ifile:
                for character in word:
                    word_character = letters + character
                    if word_character in dictionary:
                        letters = word_character
                    else:
                        linecp.append(dictionary[letters])
                        # While the dictionary size is lower than 16b, values are registered
                        if dictionarySize < 65537:
                            dictionary[word_character] = dictionarySize
                            dictionarySize += 1
                        letters = character
            if letters:
                linecp.append(dictionary[letters])

            # Use pickle to create an object serialized, a byte stream, of the array of codes
            pickle.dump(linecp, ofile, pickle.HIGHEST_PROTOCOL)

            # Close the files
            ifile.close()
            ofile.close()

            print("LZW compression succeded")
            # Return output file name
            return ofile.name
    else:
        print("Compress function request a file name to compress")
        sys.exit(0)
