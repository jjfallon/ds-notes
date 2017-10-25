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

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;1.0&space;&&space;0.0&space;&&space;0.5\\&space;0.0&space;&&space;1.0&space;&&space;0.0\\&space;0.5&space;&&space;0.0&space;&&space;1.0&space;\end{bmatrix}&space;\begin{bmatrix}&space;\textrm{...&space;word1&space;...}\\&space;\textrm{...&space;word2&space;...}&space;\\&space;\textrm{...&space;word3&space;...}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\textrm{...&space;(word1&space;&plus;&space;word3)&space;...}\\&space;\textrm{...&space;word2&space;...}&space;\\&space;\textrm{...&space;(word1&space;&plus;&space;word3)&space;...}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;1.0&space;&&space;0.0&space;&&space;0.5\\&space;0.0&space;&&space;1.0&space;&&space;0.0\\&space;0.5&space;&&space;0.0&space;&&space;1.0&space;\end{bmatrix}&space;\begin{bmatrix}&space;\textrm{...&space;word1&space;...}\\&space;\textrm{...&space;word2&space;...}&space;\\&space;\textrm{...&space;word3&space;...}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\textrm{...&space;(word1&space;&plus;&space;word3)&space;...}\\&space;\textrm{...&space;word2&space;...}&space;\\&space;\textrm{...&space;(word1&space;&plus;&space;word3)&space;...}&space;\end{bmatrix}" title="\begin{bmatrix} 1.0 & 0.0 & 0.5\\ 0.0 & 1.0 & 0.0\\ 0.5 & 0.0 & 1.0 \end{bmatrix} \begin{bmatrix} \textrm{... word1 ...}\\ \textrm{... word2 ...} \\ \textrm{... word3 ...} \end{bmatrix} = \begin{bmatrix} \textrm{... (word1 + word3) ...}\\ \textrm{... word2 ...} \\ \textrm{... (word1 + word3) ...} \end{bmatrix}" /></a>
### Combining embeddings



### Creating document / sentence level embeddings
* **word mover distance**:
* **aggregating word2vec vectors**:
* **doc2vec**:
* **skip thought vectors**:
* **sent2vec**: 
