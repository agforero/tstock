#!/usr/bin/env python3

import sys
import yfinance as yf

def main():
    tickerData = yf.Ticker(sys.argv[1])
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')
    print(tickerDf)

if __name__ == "__main__":
    main()