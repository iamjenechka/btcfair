# BTCFair - Bitcoin Price and Fee Tracker

BTCFair is a tool designed to track the price of Bitcoin (BTC) and compare it against exchanges to identify any overpricing by individual traders. It also helps users analyze withdrawal fees on different platforms, ensuring that your investments are more transparent and cost-efficient.

## Features

 - Price Tracking: Compare the sale price of Bitcoin (BTC) from various traders with the current rate on major exchanges like Coinbase.
 - Fee Analysis: Track and compare withdrawal fees across different exchanges to help you make informed decisions.
 - Transparent Trading: Understand the markup and fees applied to your transactions, and avoid overpaying.
 - Long-Term Investment Focus: Helps users focus on the long-term value of their BTC holdings while avoiding unnecessary short-term costs.


## Installation

To get started with BTCFair, follow the steps below:

### Prerequisites

   - Python 3.x or later
   - Required dependencies (listed in requirements.txt)

## Steps

1. Clone the repository:

`bash

git clone https://github.com/iamjenechka/btc-fair.git
cd btc-fair
`

2. Install the dependencies:


`bash
pip install -r requirements.txt
`


3. Set up API keys for the exchanges you want to track. You can sign up for the necessary APIs (e.g., Coinbase API) to get your key and place it in the configuration file.

4. Run the script to start tracking:

`python btc_fair.py`


## Usage

- Track Bitcoin Price: The script compares the current Bitcoin prices from selected exchanges (e.g., Coinbase) and calculates the markup from individual traders.

- Compare Withdrawal Fees: The tool also tracks withdrawal fees, showing how much of your funds might be lost during the transaction process.

- Alerts: Optionally, you can set up email or SMS alerts when the price or fees exceed a certain threshold.


## Example Output

`bash 
Trader Price: $58,500
Coinbase Price: $55,000
Price Difference: 6.36% markup

Withdrawal Fees:
Trader: 10% withdrawal fee
Coinbase: 2.5% withdrawal fee
`


## Contributing

Feel free to fork the repository and submit pull requests! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push the branch and create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.