import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, f"{year}-01-01", f"{year}-12-31")


if __name__ == "__main__":
    qan_prc_to_csv(year=2020)
