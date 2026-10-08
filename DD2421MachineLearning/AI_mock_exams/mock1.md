# DD2421 Machine Learning - Practice Exam & Answer Key

## Section A: General Machine Learning & Regression

### Questions

**A-1: Terminology Matching**
Match each term (1-4) to its most accurate description (A-D):
1. Occam's Razor
2. RANSAC
3. Curse of Dimensionality
4. K-fold cross-validation

A. A method that randomly selects a sample of points to initiate a subset and maximizes the number of inliers within a threshold distance.

B. The phenomenon where easy problems in low-dimensional spaces become difficult because the distance between points increases.

C. A technique used to estimate prediction error for model selection by partitioning data into training and validation folds.

D. The principle stating that when faced with multiple explanations for the same phenomenon, the simplest explanation is preferred.

**A-2: Bias-Variance Tradeoff & Regularization**
In Ridge Regression, the objective is to minimize $RSS + \lambda \sum_{i=1}^{D} w_i^2$. 
1. Explain what happens to the model's bias and variance as the value of the shrinkage penalty $\lambda$ increases.

2. How does the Lasso regression penalty differ from Ridge, and what specific property does this difference create in the resulting model?

**A-3: Decision Trees**
1. Write the formula for Gini impurity.

2. What does a lower Gini impurity indicate about a specific node split in a decision tree?

3. Name two specific methods to prevent a decision tree from overfitting.

---

## Section B: Probabilistic Reasoning & Inference

### Questions

**B-1: Maximum Likelihood Estimation (MLE)**
Assume a random variable $Y$ follows a Bernoulli distribution with parameter $\lambda$. You are given a dataset $\mathcal{D}$ of $N$ observations, where $n$ observations are $y=1$ and $N-n$ observations are $y=0$. 

1. Write down the likelihood function $p(\mathcal{D}\vert{}\lambda)$.

2. Derive the Maximum Likelihood Estimate for $\lambda$ by maximizing the log-likelihood. Show your mathematical steps.

**B-2: Maximum A Posteriori (MAP) vs. MLE**
1. Starting from Bayes' theorem, derive the expression for $\theta_{MAP}$.
2. In the context of probabilistic linear regression, explain how applying a D-dimensional zero-mean spherical Gaussian prior to the weights $\mathbf{w}$ transforms the MAP estimation into Ridge Regression. 

**B-3: K-Means vs. Expectation-Maximization (EM)**
1. In the EM algorithm for a Gaussian Mixture Model, briefly explain what is calculated during the E-step and the M-step.
2. State two specific ways in which the EM algorithm is more flexible than standard K-Means clustering.

---

## Section C: SVM & Artificial Neural Networks

### Questions

**C-1: Support Vector Machines (SVM)**
1. In a linearly separable SVM, the margin width between positive and negative targets is given by a specific formula depending on the weight vector $\vec{w}$. What is this mathematical formula, and what must the SVM minimize to maximize this margin?
2. What is the purpose of introducing "slack" variables ($\alpha_i \leq C$) into the SVM optimization problem? 

**C-2: Artificial Neural Networks**
1. Explain why a single artificial neuron cannot represent the XOR boolean function. What architectural change is required to solve this?
2. When training a neural network using backpropagation and gradient descent, you split your data into a 70% training set and a 30% validation set. What is the exact stopping criterion you should use to prevent overfitting/overtraining? 

---
---

## Answer Key

### Section A Answers
**A-1:** 1-D[cite: 8], 2-A[cite: 2], 3-B[cite: 2], 4-C[cite: 2].

**A-2:** 
1. As $\lambda$ increases, the model becomes more biased but has lower variance[cite: 2]. 
2. Lasso replaces the squared shrinkage penalty with an L1 norm penalty ($\sum \vert{}w_i\vert{}$)[cite: 2]. This allows some coefficients to become exactly zero, creating a sparse model and performing automatic variable selection[cite: 2].

**A-3