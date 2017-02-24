# observe
A powerfull dataframe describer with pandas.

## Usage
```python
import numpy as np
import pandas as pd
from observe import observe

df = pd.DataFrame({
    'animal': ['cat', 'dog', 'cat'],
    'age': [2, 12, 5],
    'weight': [5, 10, np.nan],
})

print(observe(df))
'''
{
    'col_stats': {
        'animal': {
            'type': 'categorical',
        },
        'age': {
            'type': 'numerical',
        },
        'weight': {
            'type': 'numerical',
        },
    },
    'meta': {
        'rows': 3,
    }
}
'''
```
