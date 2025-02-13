# Perceptron Convergence Simulation

## Overview
This repository contains a Python script that simulates the convergence probability of a perceptron learning algorithm. The script examines how often a perceptron successfully classifies a given dataset for different values of the problem size (N) and the ratio of data points to feature dimensions (alpha).

## Features
- Implements a simple perceptron learning rule.
- Simulates multiple perceptron learning systems.
- Computes the probability of perceptron convergence.
- Measures performance for different values of N and alpha.

## Requirements
The script requires the following Python libraries:
- `numpy`
- `matplotlib`
- `time`

## Usage
Run the script using Python 3:
```sh
python perceptron_convergence.py
```
The script will output the convergence probabilities for different values of N and alpha, along with the time taken for each experiment.

## Explanation
The script follows these steps:
1. Initializes a weight vector `w` randomly.
2. Generates a dataset of `p = alpha * N` points in an N-dimensional space.
3. Iteratively updates the perceptron weight vector based on misclassified points.
4. Repeats the process for multiple systems and computes the convergence probability.
5. Outputs the probability of convergence for different values of `N` and `alpha`.

## Example Output
```
100 [1.0, 0.98, 0.95, 0.85, 0.72]
Elapsed Time: 5.32s
500 [1.0, 0.99, 0.97, 0.89, 0.75]
Elapsed Time: 12.45s
1000 [1.0, 0.995, 0.98, 0.91, 0.78]
Elapsed Time: 25.87s
```



