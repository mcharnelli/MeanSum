"""
Class to create SummDataset instances.

In part here in a separate file to avoid circular imports
"""

from meansum.data_loaders.amazon_dataset import AmazonDataset
from meansum.data_loaders.yelp_dataset import YelpDataset


class SummDatasetFactory:
    def __init__(self):
        pass

    @staticmethod
    def get(name):
        if name == 'amazon':
            return AmazonDataset()
        elif name == 'yelp':
            return YelpDataset()
