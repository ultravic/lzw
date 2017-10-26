# Name: Victor Picussa
# GRR: 20163068

# Import files wih the lzw functions and sys for input
import compressor
import decompressor
import sys

if len(sys.argv) < 3:
    print("\nTo execute this test you need to enter the following comand:")
    print("\t$ python lzw.py [input] [output]\n")
else:
    # Use compressor function with the first argument to compress a file
    compressed = compressor.compress(sys.argv[1])
    # Use decompressor function with the second argument to decompress a file
    decompressed = decompressor.decompress(compressed, sys.argv[2])
