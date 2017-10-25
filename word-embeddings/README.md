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

Sebastian Ruder's [blog](http://ruder.io/word-embeddings-1/) is a great introduction to word embeddings, and Chris McCormick's [blog](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/) contains a clear explaination of the archetypal word embedding approach _word2vec_.

### Common approaches to word embeddings

The following are common word embeddings:
* **word2vec**: this uses a shallow neural network to map words to vectors. A version of this algorithm is available in gensim and pre-trained vectors are also [available](https://code.google.com/archive/p/word2vec/) where the vectors have been trained on Google News Group data. There is [evidence](https://arxiv.org/abs/1607.06520) that the pre-trained vectors have learnt gender biases from this News Group data. These biases are likely to be an issue with many word embeddings.
* **GloVe**: this is an alternative to word2vec that is not based on neural networks but instead is constructed from statistics on the co-occurance of words. Information about GloVe can be found [here](https://nlp.stanford.edu/projects/glove/) as can a range of pre-trained vectors. It is not clear whether word2vec or GloVe is more performant on given problems. 
* **fastText**: FastText was created by the same group as word2vec and has been opened source by facebook. More information and pre-trained vectors can be found [here](https://github.com/facebookresearch/fastText). FastText creates word embeddings that take into account the subsets of characters a word. For example, it might learn that having the letters "im" at the start of a word tells you something about the meaning of that word. This also means that fastText can create vectors for words not appearing in the original training data by considering the different subsets of characters within that word.
* **Conceptnet Numberbatch**: this combines information from various embeddings (including commonly used pre-trained word2vec and GloVe vectors) and also ccombines it with knowledge of associations between words captured by the ConceptNet project. More information can be found [here](https://github.com/commonsense/conceptnet-numberbatch) and the authors also argue that their pre-trained embeddings contain fewer biases than those within other commonly used embeddings. 
* **sense2vec**: The aim of sense2vec is to deal with the case where a word has more than one distinct meaning. The idea is to append annotations to each word which denote which meaning is indicated in any given situation. In order to create annotations algorithmically NLP techniques (in particular part-of-speech tagging and named entity detection) are used to detect how a word is being used. Once annotations have been appended to each and every word, these new words can be run through standard word embeddings algorithms such as word2vec and GloVe. See this [blog post](https://explosion.ai/blog/sense2vec-with-spacy) and code their [code repository](https://github.com/explosion/sense2vec) for more details.


The vectors from word embeddings can be used to look for similiar words and this is typically found by calculating the cosine distance between word vectors. Cosine distance only considers the angles between vectors, but the magnitude of the vectors can also have meaning. As shown in [this paper](https://arxiv.org/abs/1508.02297), with word2vec the length of the vector is related to the both the number of times a word occurs and whether the word is always appearing in very similiar contexts.

TensorBoard (online version [here](http://projector.tensorflow.org/)) has a visualisation of the Google News Group word2vec embeddings built and is a good way of understanding what sort of words are flagged as being similiar. You can also read in your own embeddings if they are in the right format.

### Combining embeddings
![equation](https://latex.codecogs.com/svg.latex?x%5Ey)


### Creating document / sentence level embeddings
* **word mover distance**:
* **aggregating word2vec vectors**:
* **doc2vec**:
* **skip thought vectors**:
* **sent2vec**: 

These word embedding techniques are alternatives to performing 
