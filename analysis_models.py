import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np
from scipy.signal import correlate

class MarketPredictor(nn.Module):
    """
    A deep learning model to predict market index's price or volatility using 
    low-frequency macro data and mid-frequency micro data such as commodities 
    spot price, and specific stock price.
    """
    def __init__(self, input_dim, hidden_dim, output_dim):
        """
        Initialize the neural network.
        :param input_dim: The number of input features.
        :param hidden_dim: The size of the hidden layer.
        :param output_dim: The number of output features (1 for price or volatility).
        """
        super(MarketPredictor, self).__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        """
        Forward pass through the network.
        :param x: The input data.
        :return: The predicted output.
        """
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x

class CPIComparison:
    """
    A class to compare the CPILike Index with the CPI index to find the lag between them.
    """
    @staticmethod
    def find_lag(cpilike_index_series, cpi_index_series):
        """
        Finds the lag between the CPILike Index and the CPI index.
        
        :param cpilike_index_series: The CPILike Index series as a numpy array.
        :param cpi_index_series: The CPI index series as a numpy array.
        :return: The lag between the two series.
        """
        correlation = correlate(cpilike_index_series, cpi_index_series, mode="full")
        lag = np.argmax(correlation) - (len(cpilike_index_series) - 1)
        return lag