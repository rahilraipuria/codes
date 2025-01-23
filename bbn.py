#Bayesian Belief Networks
import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv').dropna()
heartDisease['age'] = pd.cut(heartDisease['age'], bins=[29, 39, 49, 59, 69, 79, 89], labels=[30, 40, 50, 60, 70, 80])

model = BayesianNetwork([
 ('age', 'trestbps'),
 ('age', 'fbs'),
 ('sex', 'trestbps'),
 ('exang', 'trestbps'),
 ('trestbps', 'target'),
 ('fbs', 'target'),
 ('target', 'restecg'),
 ('target', 'thalach'),
 ('target', 'chol')
])

model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
heartDisease_infer = VariableElimination(model)

q = heartDisease_infer.query(variables=['target'], evidence={'age': 30})
print(q)

print("\nProbability distribution for 'target':")
print(q.values)

q = heartDisease_infer.query(variables=['target'], evidence={'age': 70})
print(q)

print("\nProbability distribution for 'target':")
print(q.values)
