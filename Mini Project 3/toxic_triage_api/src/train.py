import torch
from model import ToxicClassifier
import config
from data_loader import create_data_loader
from transformers import DistilBertTokenizer
from torch.cuda.amp import GradScaler, autocast
from tqdm import tqdm
import pandas as pd


scaler=GradScaler()

model = ToxicClassifier(config.MODEL_NAME).to(config.DEVICE)
tokenizer = DistilBertTokenizer.from_pretrained(config.MODEL_NAME)
loss_fn = torch.nn.BCEWithLogitsLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=config.LEARNING_RATE)

def train_epoch(model, dataloader, optimizer, criterion, device, scaler):
    model.train()
    total_loss = 0
    progress_bar = tqdm(dataloader, desc="Training", leave=False)
    for batch in progress_bar:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        optimizer.zero_grad()
        with autocast():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = criterion(outputs, labels)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    return avg_loss

if __name__ == "__main__":
    data = pd.read_csv('../data/train.csv').head(1000)
    dataloader = create_data_loader(data, tokenizer, max_len=config.MAX_LEN, batch_size=config.TRAIN_BATCH_SIZE)
    avg_loss = train_epoch(model, dataloader, optimizer, loss_fn, config.DEVICE, scaler)
    print(f"Average training loss: {avg_loss:.4f}")
    torch.save(model.state_dict(), "toxic_model_weights.pth")

