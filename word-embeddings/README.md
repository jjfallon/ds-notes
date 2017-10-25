# Word Embeddings

This folder contains various notes and notebooks exploring word embeddings techniques.

## Folder
As well as these notes, this folder contains:
* **word2vec-from-scratch.ipynb**: building my own neural network to create a word2vec skip-gram model in order to understand how it works under the hood.
* **doc2vec-basics.ipynb**: toy example of using the doc2vec implementation within gensim as an aide memoir.

## Notes
In short word embeddings map individual words to a vector. The aim is to construct an embedding such that similiar words are mapped to similiar vectors. 
Normally *similarity* is defined in terms of *semantic similarity*, words which are similiar in meaning rather than necessarily looking similiar. Most 
methods deduce semantic similarity by looking at whether words often appear with the same words around them.


### Common word embeddings
* **word2vec**:
* **glove**:
* **fasttext**: 
* **Conceptnet Numberbatch**:
* **sense2vec** 

Alternative, LSA, ..., ...,

Length of a word2vec vector ....

### Combining embeddings
[!equation](https://latex.codecogs.com/svg.latex?x%5Ey)


### Creating document / sentence level embeddings
* **word mover distance**:
* **aggregating word2vec vectors**:
* **doc2vec**:
* **skip thought vectors**:
* **sent2vec**: 
