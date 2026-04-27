import torch

DATA_PATH = "data/ratings.csv"
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model Architecture
EMBEDDING_DIM = 32  # The size of our latent vector space

# MovieLens 100k specific boundaries
NUM_USERS = 943
NUM_ITEMS = 1682

# Training Hyperparameters
BATCH_SIZE = 1024  # Recommender batches are usually massive
EPOCHS = 10
LEARNING_RATE = 1e-3