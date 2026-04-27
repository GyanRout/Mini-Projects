import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
import config
from model import MatrixFactorization
from dataset import MovieLensDataset

dataset = MovieLensDataset(config.DATA_PATH)
dataloader = DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=True)
model = MatrixFactorization(config.NUM_USERS, config.NUM_ITEMS, config.EMBEDDING_DIM).to(config.DEVICE)
criterion = nn.MSELoss()
optimizer = Adam(model.parameters(), lr=config.LEARNING_RATE)

for epoch in range(config.EPOCHS):
    total_loss = 0
    for users, items, ratings in tqdm(dataloader, desc=f"Epoch {epoch+1}"):
        users = users.to(config.DEVICE)
        items = items.to(config.DEVICE)
        ratings = ratings.to(config.DEVICE)

        optimizer.zero_grad()
        predictions = model(users, items)
        loss = criterion(predictions, ratings)
        loss.backward()
        optimizer.step()

        total_loss+=loss.item()
    print(f"Average loss: {total_loss/len(dataloader)}")