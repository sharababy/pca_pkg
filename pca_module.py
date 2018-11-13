from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import csv
from numpy import cov
from numpy.linalg import eig
import matplotlib.pyplot as plt

def PCA(filename = "",topk = 0, graph=True):

	if len(filename) == 0:
		print("Error: File not provided!")
		return

	data = []
	label = []
	with open(filename) as datafile:
		reader = csv.reader(datafile,delimiter=",")
		next(reader)
		for row in reader:
			
			# data.append(list(map(float,row[2:])))
			float_row = []
			for value in row[2:]:
				try:
					value = float(value)
					float_row.append(value)

				except ValueError:
					float_row.append(0.0)					
			data.append(float_row)
			label.append(row[1])

	data_mat = np.asarray(data)

	totalDims = data_mat.shape[-1]

	if topk > totalDims or topk < 0:
		print("Invalid value for topk!")
		return

	
	centered_mat = data_mat - np.mean(data_mat.T, axis=1)
	
	values, vectors = eig(cov(centered_mat.T))
	indices = np.argpartition(values, -topk)[-topk:]

	max_variance_vectors = []
	for index in indices:
		max_variance_vectors.append(vectors[index])

	max_variance_vectors = np.asarray(max_variance_vectors)
	projected_mat = max_variance_vectors.dot(centered_mat.T)

	if graph:
		fig = plt.figure()
		fig.suptitle('PCA on '+filename, fontsize=14, fontweight='bold')
		ax = fig.add_subplot(111)
		ax.set_xlabel("PC1")
		ax.set_ylabel("PC2")
		ax.scatter(projected_mat[0],projected_mat[1])
		
		plt.show()

	return projected_mat.T
