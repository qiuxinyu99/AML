import pandas as pd

dev_df = pd.read_csv("./data/train.csv", low_memory=True)

dev_small_df = dev_df.sample(frac=0.01)  # We sample 1% of the original data to be used for developing model

dev_small_df.to_csv("./data/dev_small.csv")


