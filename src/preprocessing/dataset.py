# dataset.py
from torch.utils.data import Dataset

class MosaicDataset(Dataset):

    def __init__(self, features: dict):
        self.features = features
        self.keys = list(features.keys())

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, idx):
        key = self.keys[idx]
        df = self.features[key]
        return key, df