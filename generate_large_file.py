import pandas as pd
import numpy as np

# Number of rows and columns
num_rows = 1000000  # 1 million rows
num_columns = 10  # 10 columns

# Generate random data
data = np.random.rand(num_rows, num_columns)

# Create a DataFrame
columns = [f'col_{i+1}' for i in range(num_columns)]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('large_file.csv', index=False)
