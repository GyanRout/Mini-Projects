import torch

TRAIN_DATA_PATH = '../data/train.csv'
TEST_DATA_PATH = '../data/test.csv'

MODEL_NAME = 'distilbert-base-uncased'
MAX_LEN = 256
TRAIN_BATCH_SIZE = 16
VALID_BATCH_SIZE = 16
EPOCHS = 3
LEARNING_RATE = 2e-5

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')