import torch.nn as nn
import config

class MatrixFactorization(nn.Module):
    def __init__(self, num_users: int, num_items: int, embedding_dim: int) -> None:
        super().__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
    
    def forward(self, user_indices, item_indices):
        user_vecs = self.user_embedding(user_indices)
        item_vecs = self.item_embedding(item_indices)

        ele_wise_product = user_vecs * item_vecs
        prediction = ele_wise_product.sum(dim=1)
        return prediction