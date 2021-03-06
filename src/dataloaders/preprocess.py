"""
Module that contains any functions relating to data preprocessing and data loading.
"""
from sklearn.model_selection import StratifiedShuffleSplit


def get_indices_split(data, col, val_prop=0.3):
    """Creates the indices for Train/Val split on given dataset.
    Performs stratified split based on specified feature. 
    (with random seed set).

    Args:
        data (pd.DataFrame):
        col (str): The feature/label to stratify on.
        val_prop (float): Proportion to go to validation set.

    Returns:
        (train_indices, val_indices),
        i.e. tuple of two arrays of indices.
    """
    split = StratifiedShuffleSplit(n_splits=1, test_size=val_prop, random_state=42)

    train_indices, val_indices = next(split.split(data, data[col]))

    return train_indices, val_indices
