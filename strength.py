import yfinance 

usd_score = 0
btc_score = 0
eth_score = 0
ada_score = 0

time_frame = '1h'
moving_average_value = 200

def is_stronger(pair):
    # True if the first currency is stronger than the second one
    # E.g. True if BTC/USD price is above the moving average
    current_pair = yfinance.download(pair, interval=time_frame, period='1mo').Close
    current_pair = current_pair.sort_index(ascending=False) # latest dates first
    current_pair = current_pair[1:] # the first data point is not a close
    current_pair = current_pair[:moving_average_value] # remove extra data
    price = current_pair[0] # close price is first one
    ma_value = current_pair.sum()/moving_average_value
    is_stronger = price > ma_value
    return is_stronger

if __name__ == "__main__":
    print("Ranking the top cypto currencies ...")
    # btc-usd
    if is_stronger('btc-usd'):
        btc_score = btc_score + 1
        usd_score = usd_score - 1
    else:
        btc_score = btc_score - 1
        usd_score = usd_score + 1
    # eth-usd
    if is_stronger('eth-usd'):
        eth_score = eth_score + 1
        usd_score = usd_score - 1
    else:
        eth_score = eth_score - 1
        usd_score = usd_score + 1
    # ada-usd
    if is_stronger('ada-usd'):
        ada_score = ada_score + 1
        usd_score = usd_score - 1
    else:
        ada_score = ada_score - 1
        usd_score = usd_score + 1
    # eth-btc
    if is_stronger('eth-btc'):
        eth_score = eth_score + 1
        btc_score = btc_score - 1
    else:
        eth_score = eth_score - 1
        btc_score = btc_score + 1
    # ada-btc
    if is_stronger('ada-btc'):
        ada_score = ada_score + 1
        btc_score = btc_score - 1
    else:
        ada_score = ada_score - 1
        btc_score = btc_score + 1
    # ada-eth
    if is_stronger('ada-eth'):
        ada_score = ada_score + 1
        eth_score = eth_score - 1
    else:
        ada_score = ada_score - 1
        eth_score = eth_score + 1

    print("USD: " + str(usd_score))
    print(f"BTC: {btc_score}")
    print(f"ETH: {eth_score}")
    print(f"ADA: {ada_score}")