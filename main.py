import pandas  as pd
import numpy as np
data = {
    'Name': ['Ahmed', 'Sara', 'Ali'],
    'Age': [20, 22, 19],
    'City': ['Cairo', 'Alex', 'Giza'],
}

df = pd.DataFrame(data)
print(df)