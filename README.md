# Digital Asset Signal Service (DASS)

## Description


## Inputs
* Time Frame setting (1h by default)
* Moving Average period setting (200 SMA by default)
* email address of signal recipient

## Pairs
1. BTC/USD
1. ETH/USD
1. ADA/USD
1. ETH/BTC
1. ADA/BTC
1. ADA/ETH

## Relative Strength Comparison Logic
|     | USD  | BTC  |  ETH | ADA  |
| --- | ---- | ---- | ---- | ---- |
| USD |  x   |  1   |  1   |   1  |
| BTC |  -1  |  x   |  -1  |   1  |
| ETH |  -1  |  1   |  x   |   1  |
| ADA |  -1  |  -1  |  -1  |  x   |
|     |  -3  |  1   |  -1  |  3   |

## Rankings Example
1. ADA (+3)
1. BTC (+1)
1. ETH (-1)
1. USD (-3)
