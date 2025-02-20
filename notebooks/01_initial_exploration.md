# Initial Data Exploration
This notebook will be used for processing my thoughts, as I explore, clean up, and enrich the ArchivesSpace agent data.

## Setup
```python
import pandas as pd
import json
import requests
from pathlib import Path

Load Configuration

with open('../config.json') as f:
    config = json.load(f)
    
    Load and Examine Data
[Add data loading and examination code here]
