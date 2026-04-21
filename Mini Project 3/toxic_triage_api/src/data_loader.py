import torch
import pandas as pd
from typing import Dict
from torch.utils.data import Dataset, DataLoader
from transformers import DistilBertTokenizer

class ToxicCommentsDataset(Dataset):
    def __init__(self, dataframe: pd.DataFrame, tokenizer: DistilBertTokenizer, max_len: int) -> None:
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.target_col =['toxic','severe_toxic','obscene','threat','insult','identity_hate']
        self.max_len = max_len
    
    def __len__(self) -> int:
        return len(self.dataframe)

    def __getitem__(self, index: int) -> Dict[str, torch.Tensor]:
        row = self.dataframe.iloc[index]
        comment_text =  str(row['comment_text'])
        targets = row[self.target_col].values.astype(float)

        inputs = self.tokenizer(
            text=comment_text,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'input_ids': inputs['input_ids'].flatten(), #type: ignore
            'attention_mask': inputs['attention_mask'].flatten(), #type: ignore
            'labels': torch.tensor(targets, dtype=torch.float)
        }

def create_data_loader(dataframe: pd.DataFrame, tokenizer: DistilBertTokenizer, max_len: int, batch_size: int) -> DataLoader:
    dataset = ToxicCommentsDataset(dataframe, tokenizer, max_len)
    return DataLoader(dataset, batch_size=batch_size, num_workers=2,shuffle=True)