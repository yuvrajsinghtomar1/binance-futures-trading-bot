# Binance Futures Testnet Trading Bot

## Features

- MARKET orders
- LIMIT orders
- BUY/SELL support
- CLI interface
- Logging
- Exception handling
- Input validation

## Setup

1. Clone repository

2. Install dependencies

pip install -r requirements.txt

3. Create .env file

BINANCE_API_KEY=...
BINANCE_API_SECRET=...

4. Run examples

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 95000

## Assumptions

- Binance Futures Testnet account is active.
- API credentials have futures permissions.