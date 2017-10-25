# Word Embeddings

This folder contains various notes and notebooks exploring word embeddings techniques.

## Folder
As well as these notes, this folder contains:
* **word2vec-from-scratch.ipynb**: building my own neural network to create a _word2vec_ skip-gram model in order to understand how it works under the hood.
* **doc2vec-basics.ipynb**: toy example of using the _doc2vec_ implementation within gensim as an aide memoir.

## Notes
In short word embeddings map individual words to a vector. The aim is to construct an embedding such that similiar words are mapped to similiar vectors. 
Normally *similarity* is defined in terms of *semantic similarity*, words which are similiar in meaning rather than necessarily looking similiar. Most 
methods deduce semantic similarity by looking at whether words often appear with the same words around them.

Sebastian Ruder's [blog](http://ruder.io/word-embeddings-1/) is a great introduction to word embeddings, and Chris McCormick's [blog](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/) contains a clear explaination of the archetypal word embedding approach _word2vec_.

### Common approaches to word embeddings

The following are common word embeddings:
* **word2vec**: this uses a shallow neural network to map words to vectors. A version of this algorithm is available in gensim and pre-trained vectors are also [available](https://code.google.com/archive/p/word2vec/) where the vectors have been trained on Google News Group data. There is [evidence](https://arxiv.org/abs/1607.06520) that the pre-trained vectors have learnt gender biases from this News Group data. These biases are likely to be an issue with many word embeddings.
* **GloVe**: this is an alternative to _word2vec_ that is not based on neural networks but instead is constructed from statistics on the co-occurance of words. Information about _GloVe_ can be found [here](https://nlp.stanford.edu/projects/glove/) as can a range of pre-trained vectors. It is not clear whether _word2vec_ or _GloVe_ is more performant on given problems. 
* **fastText**: _FastText_ was created by the same research group as _word2vec_ and has been opened source by facebook. More information and pre-trained vectors can be found [here](https://github.com/facebookresearch/fastText). _FastText_ creates word embeddings that take into account the subsets of characters a word. For example, it might learn that having the letters "im" at the start of a word tells you something about the meaning of that word. This also means that _fastText_ can create vectors for words not appearing in the original training data by considering the different subsets of characters within that word.
* **Conceptnet Numberbatch**: this combines information from various embeddings (including commonly used pre-trained _word2vec_ and _GloVe_ vectors) and also ccombines it with knowledge of associations between words captured by the _ConceptNet_ project. More information can be found [here](https://github.com/commonsense/conceptnet-numberbatch) and the authors also argue that their pre-trained embeddings contain fewer biases than those within other commonly used embeddings. 
* **sense2vec**: The aim of _sense2vec_ is to deal with the case where a word has more than one distinct meaning. The idea is to append annotations to each word which denote which meaning is indicated in any given situation. In order to create annotations algorithmically NLP techniques (in particular part-of-speech tagging and named entity detection) are used to detect how a word is being used. Once annotations have been appended to each and every word, these new words can be run through standard word embeddings algorithms such as _word2vec_ and _GloVe_. See this [blog post](https://explosion.ai/blog/sense2vec-with-spacy) and code their [code repository](https://github.com/explosion/sense2vec) for more details.


The vectors from word embeddings can be used to look for similiar words and this is typically found by calculating the cosine distance between word vectors. Cosine distance only considers the angles between vectors, but the magnitude of the vectors can also have meaning. As shown in [this paper](https://arxiv.org/abs/1508.02297), with _word2vec_ the length of the vector is related to the both the number of times a word occurs and whether the word is always appearing in very similiar contexts.

TensorBoard (online version [here](http://projector.tensorflow.org/)) has a visualisation of the Google News Group _word2vec_ embeddings built and is a good way of understanding what sort of words are flagged as being similiar. You can also read in your own embeddings if they are in the right format.

### Combining embeddings

Papers such as [this](https://pdfs.semanticscholar.org/343d/39534682bb7b2eec14f573360877eb80cd59.pdf) and [this](https://arxiv.org/abs/1604.01692) discuss ways in which different word embeddings can be combined. Methods include:
* Simply concatenating the vectors together for each word.
* Concatenate the vectors and then perform singular value decomposition.
* Concatenate the vectors and then use an autoencoder to reduce the number of dimensions.

As discussed in the Conceptnet Numberbatch [paper](https://arxiv.org/abs/1604.01692) a difficultly is dealing with words that appear in the vocabulary of one embedding but not the other. The way they deal with this is if a word is missing they look at how the vectors of the most similiar words transform between the two embeddings, and the angle between the vector of the word in question and these similiar words in the original space.

Another thing that the Conceptnet Numberbatch embedding does is take into account known associations between words and encodes them into a matrix, this the word embeddings matrix is then multiplied by this associations matrix. To demonstrate the principle (the full approach is more complicated) consider an embedding of dimension three containing just three words where we know _a priori_ that words one and three are basically the same. Multiplying the embeddings matrix by the association matrix shown results in word one and word three having the same vector.
   ![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%201%20%26%200%20%26%20%5Cfrac12%20%5C%5C%200%20%26%201%20%26%200%20%5C%5C%20%5Cfrac12%20%26%200%20%26%201%20%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word1%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5C%5C%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word2%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5C%5C%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word3%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word1%7D&plus;%5Ctextrm%7B%5Cbf%20word3%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5C%5C%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word2%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5C%5C%20%5Ctextrm%7B%20---%7D%20%26%20%5Ctextrm%7B%5Cbf%20word1%7D&plus;%5Ctextrm%7B%5Cbf%20word3%7D%20%26%20%5Ctextrm%7B---%20%7D%20%5Cend%7Bbmatrix%7D)

The associations do not have to be as strong as that shown in this example.

### Creating document / sentence level embeddings


* **aggregating word2vec vectors**:
* **doc2vec**:
* **skip thought vectors**:
* **sent2vec**: 

An alternative approach that still uses word embeddings is to consider **word mover distance**

These word embedding techniques are alternatives to performing techniques such as **Latent Semantic Analysis (LSA)**. LSA is a bag of words approach where the number of times each word in the vocabulary occurs is tabulated. These term frequencies can then be weighted if warranted (such as with TF-IDF) and then singular value decomposition can be performed to reduce the number of dimensions. This would produce a vector for each document, but words with the same meaning would have been treated as separate features. 
