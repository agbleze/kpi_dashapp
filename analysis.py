#%%
import pandas as pd
import numpy as np
from typing import List


# %%
data = pd.read_csv(r'Data/data.csv')

# %%
np.random.randint(50, 90, data.shape[0])

# %%
np.random.choice(['new', 'return'], data.shape[0])
# %%
data.columns
# %%
data['conversion_rate'] = np.random.randint(50, 90, data.shape[0])
# %%

def generate_values(data: pd.DataFrame, columns: List[str], 
                    start_value: int, end_value: int) -> pd.DataFrame:
    if columns:
        if isinstance(columns, list):
            for name in columns:
                data[name] = np.random.randint(start_value, end_value, data.shape[0])
        else:
            data[columns] = np.random.randint(start_value, end_value, data.shape[0])
    else:
        columns= data.columns
        for name in columns:
                data[name] = np.random.randint(start_value, end_value, data.shape[0])
                
    return data
        
# %%
