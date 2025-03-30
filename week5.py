import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    df_date = pd.DataFrame(date_info, columns=["row_id", "Date"])
    df_aud_usd = pd.DataFrame(aud_usd_info, columns=["row_id", "AUD/USD"])
    df_eur_aud = pd.DataFrame(eur_aud_info, columns=["row_id", "EUR/AUD"])

    df = df_date.merge(df_aud_usd, on="row_id", how="left") \
                .merge(df_eur_aud, on="row_id", how="left")

    df = df.sort_values(by="Date")

    df = df.drop(columns=["row_id"])

    df = df.loc[:, ["Date", "AUD/USD", "EUR/AUD"]]
    df.index = df["Date"]
    df = df.drop(columns=["Date"])
    df.index.name = None

    return df

# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]


df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)
