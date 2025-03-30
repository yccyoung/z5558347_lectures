# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

# print("Welcome to T1 2025, Chengchen Yang, z5558347!")

# import yfinance as df
# df.download("QAN.AX", '2020-01-01', None).to_csv('2.csv')
# Define a few lists...
