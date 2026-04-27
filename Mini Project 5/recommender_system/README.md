# 🎬 Collaborative Filtering Recommender System

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A machine learning project demonstrating how to build a Collaborative Filtering Recommender System using PyTorch. This system predicts the rating a user will give to a movie they haven't seen yet based on historical user-item interactions.

---

## 📖 Table of Contents
- [The Problem](#-the-problem)
- [The Solution: Matrix Factorization](#-the-solution-matrix-factorization)
- [Project Structure](#-project-structure)
- [Getting Started (Setup Guide)](#-getting-started-setup-guide)
- [Code Breakdown](#-code-breakdown)
- [What I Learnt](#-what-i-learnt)

---

## 🚧 The Problem

Imagine a typical movie database like Netflix or IMDB. It might have **100,000 users** and **10,000 movies**. 
If you create a grid (a matrix) where rows are users and columns are movies, you get 1,000,000,000 possible ratings!

However, most users have only watched about 10 movies. This means our user-item matrix is **99.9% empty (sparse)**. 
> *You cannot calculate standard statistics (like mean or correlation) on empty space.*

---

## 💡 The Solution: Matrix Factorization

To solve the sparsity problem, we use **Matrix Factorization**. Instead of trying to fill in a massive empty grid, we decompose the massive sparse matrix into two smaller, dense matrices:

1. **User Embeddings:** A dense representation (vector) of a user's preferences (e.g., how much they like action, romance, or sci-fi).
2. **Item Embeddings:** A dense representation of a movie's traits (e.g., how much action, romance, or sci-fi it contains).

By taking the **Dot Product** of a User Embedding and an Item Embedding (and adding baseline biases), we can accurately predict how much that specific user will like that specific movie!

---

## 📂 Project Structure

```text
recommender_system/
├── data/                   # Generated datasets will be stored here
├── src/
│   ├── __init__.py
│   ├── config.py           # Hyperparameters (embedding size, learning rate)
│   ├── dataset.py          # PyTorch Dataset parsing User-Item-Rating triplets
│   ├── model.py            # PyTorch Neural Network with nn.Embedding
│   └── train.py            # The training loop optimizing Mean Squared Error (MSE)
├── requirements.txt        # Project dependencies
└── setup_data.py           # Script to generate synthetic ratings data