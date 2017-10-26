# Name: Victor Picussa
# GRR: 20163068

import pickle
import sys

def decompress(infile, outfile):
    # Try open the infile, if doesn't exist, throw a error
    if infile and outfile:
        try:
            ifile = open(infile, 'rb')
        except IOError:
            print("The file named '%s' doesn't exist or cannot be found" % infile)
        else:
            # Open the outfile to decompress infile
            ofile = open(outfile, 'w')

            # Create the base dictionary
            dictionarySize = 256;
            dictionary = dict((index, chr(index)) for index in xrange(dictionarySize))

            # Load the pickle object to de-serialize it
            filecp = pickle.load(ifile)

            # Pop the first character from the array, if
            word = chr(filecp.pop(0))

            # LZW algorithm
            linedcp = [word]
            for character in filecp:
                if character in dictionary:
                    letters = dictionary[character]
                elif character == dictionarySize:
                    letters = word + word[0]
                else:
                    raise ValueError("Compression currupted: character %d unidentifiable" % character)
                linedcp.append(letters)
                dictionary[dictionarySize] = word + letters[0]
                dictionarySize += 1
                word = letters

            # For each item in the array, write it in the output file
            for item in linedcp:
                ofile.write(item)

            # Close the files
            ifile.close()
            ofile.close()

            print("LZW decompression succeded")
            # Return output file name
            return ofile.name
    else:
        print("Decompress function request a file name to decompress and a output")
        sys.exit(0)
