# Compressão com LZW
Os arquivos desse projeto implementam o algoritmo LZW para compressão de arquivos.

O arquivo [compressor.py](https://github.com/ultravic/lzw/blob/master/compressor.py) implementa a compressão de um arquivo passado. Verifica
se existe e abre o arquivo, executa o algoritmo LZW com uma tabela limitada a
16 bits. Utilizando da biblioteca pickle cria um objeto byte stream com os códigos
de compressão e retorna o nome do arquivo de saída.

O arquivo [decompressor.py](https://github.com/ultravic/lzw/blob/master/decompressor.py) implementa a decodificação de um arquivo comprimido com
o compress. Abre o arquivo e faz a leitura do objeto byte stream,
executa o LZW e retorna o nome do arquivo de saída.

## Executar testes
Para executar o teste presente em [lzw.py](https://github.com/ultravic/lzw/blob/master/lzw.py), digita-se o seguinte comando:
```
$ python lzw.py [entrada] [saída]
```

## Oberservações:
* Arquivos com tamanho até (+/-) 6Kb retornam um arquivo comprimido
maior que o original. Para arquivos maiores o algoritmo torna-se eficiente.

* A compressão só funciona para arquivos em formato ASCII

* A decodificação de um arquivo compactado só funciona para arquivos que utilizaram
o algoritmo presente em [compress.py](https://github.com/ultravic/lzw/blob/master/compressor.py)

## Autor
* **Victor Picussa**

