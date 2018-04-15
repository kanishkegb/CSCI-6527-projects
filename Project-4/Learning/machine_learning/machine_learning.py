import pandas as pd
import pdb

# pdb.set_trace()

melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.describe())
