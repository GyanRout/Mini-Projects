import torch.nn as nn
import torch
from transformers import DistilBertModel

class ToxicClassifier(nn.Module):
    def __init__(self, model_name: str)-> None:
        super(ToxicClassifier, self).__init__()
        self.bert = DistilBertModel.from_pretrained(model_name)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(in_features = 768, out_features = 6)

    def forward(self, input_ids: torch.Tensor, attention_mask: int):
        distilbert_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        hidden_state = distilbert_output[0]

        cls_token = hidden_state[:, 0, :]
        output = self.drop(cls_token)
        logits = self.out(output)

        return logits
    
