# dataset.py
from torch.utils.data import Dataset


class MosaicDataset(Dataset):
    def __init__(self, data_dict):
        """
        data_dict = {var_name: DataFrame}
        """
        self.data = data_dict
        self.keys = list(data_dict.keys())

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, idx):
        key = self.keys[idx]
        return key, self.data[key]