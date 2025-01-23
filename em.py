import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

X = np.concatenate([np.random.randn(300, 2) + [5, 5], np.random.randn(300, 2) + [0, -5]])
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
labels = gmm.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('GMM Clustering')
plt.show()


print(f"Means: \n{gmm.means_}")
print(f"Covariances: \n{gmm.covariances_}")
print(f"Weights: \n{gmm.weights_}")