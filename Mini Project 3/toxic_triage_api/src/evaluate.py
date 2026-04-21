import torch
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score, f1_score
import config
from model import ToxicClassifier
from data_loader import create_data_loader
from transformers import DistilBertTokenizer
from tqdm import tqdm

tokenizer = DistilBertTokenizer.from_pretrained(config.MODEL_NAME)
test_data = pd.read_csv(config.TRAIN_DATA_PATH)
test_loader = create_data_loader(test_data, tokenizer, config.MAX_LEN, config.VALID_BATCH_SIZE)

model = ToxicClassifier(config.MODEL_NAME)
model.load_state_dict(torch.load('/content/drive/MyDrive/toxic_triage_api/src/toxic_model_weights.pth'))
model.to(config.DEVICE)
model.eval()

probabilities_list = []
labels_list = []

with torch.inference_mode():
    for batch in tqdm(test_loader, desc="Evaluating"):
        input_ids = batch['input_ids'].to(config.DEVICE)
        attention_mask = batch['attention_mask'].to(config.DEVICE)
        labels = batch['labels'].to(config.DEVICE)

        logits = model(input_ids=input_ids, attention_mask=attention_mask)
        probability = torch.sigmoid(logits).cpu().numpy()
        true_labels = labels.cpu().numpy()

        probabilities_list.append(probability)
        labels_list.append(true_labels)

        
    
final_probabilities = np.vstack(probabilities_list)
final_labels = np.vstack(labels_list)

roc_auc = roc_auc_score(final_labels, final_probabilities, average='macro')
propabilities = (final_probabilities > 0.5).astype(int)
f1 = f1_score(final_labels, propabilities, average='macro')

print(f"ROC AUC Score: {roc_auc:.4f}")
print(f"F1 Score: {f1:.4f}")