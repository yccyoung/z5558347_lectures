import pandas as pd
import numpy as np


aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = pd.Series({key:value for key, value in aud_usd_lst})
eur_aud_series = pd.Series({key:value for key, value in eur_aud_lst})
df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD': eur_aud_series})
