# t-SNE Preprocessing Comparison

Preprocessing data for t-SNE using PCA versus a convolutional autoencoder.

My interpretation is that PCA performs better as a pre-processing step in this case than t-SNE. This is based on the way the 2d embedding looks, but also by the k-nearest neighbors classification for different values of k. PCA provides ~96% accuracy for the 1-nearest neighbor while the convolutional autoencoder is closer to ~92% (and decreases faster).

## Notes on t-SNE implementations

This notebook uses [bhtsne](https://github.com/lvdmaaten/bhtsne) by the Laurens van der Maaten, via the Python wrapper, which is the fastest and most bug-free implementation I've found of t-SNE.

* The sklearn t-SNE implementation has [lots of issues](https://github.com/scikit-learn/scikit-learn/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+tsne) including poor performance and bad default values.
* The package installed by `pip install tsne` does not return t-SNE correctly [for three dimensions](https://github.com/danielfrg/tsne/issues/11).

Unfortunately this means I've compiled it for my system only (OSX 10.11). For other systems you will need to recompile the binary following the instructions in Laurens' repo.