PYC = python

FILES = main.py compressor.py decompressor.py dictionary.py

run:
	$(PYC) $(FILES)

purge:
	-rm *.pyc
