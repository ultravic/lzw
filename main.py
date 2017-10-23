# import compressor
# import decompressor
import dictionary

# How to use:
dictionary.init();
# compressed = compressor.compress(['A', 'B', 'C'])
# print (compressed)
# decompressed = decompressor.decompress(compressed)
# print (decompressed)
dictionary.dictionarySize += 1
dictionary.dictionary[dictionary.dictionarySize] = 'ACX'
print(dictionary.dictionary)
