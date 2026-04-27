import torch
from typing import Tuple
import pandas as pd
from torch.utils.data import Dataset

class MovieLensDataset(Dataset):
    def __init__(self, csv_file: str) -> None:
        df = pd.read_csv(csv_file)
        self.user_ids = torch.tensor(df['user_id'].to_numpy() - 1, dtype=torch.long)
        self.item_ids = torch.tensor(df['item_id'].to_numpy() - 1, dtype=torch.long)
        self.ratings = torch.tensor(df['rating'].to_numpy(), dtype=torch.float)

    def __len__(self) -> int:
        return len(self.ratings)
    
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        return (self.user_ids[idx], self.item_ids[idx], self.ratings[idx])
