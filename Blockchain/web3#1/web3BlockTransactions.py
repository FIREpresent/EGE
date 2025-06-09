from web3 import Web3, HTTPProvider

def get_transactions(block_number, w3):
    _transactions = w3.eth.get_block(block_identifier=block_number, full_transactions=True)['transactions']
    return _transactions

def transactions_display(transactions):
    index = 1
    for transaction in transactions:
        print(f'Transaction №{index}:')
        for (key, value) in transaction.items():
            print(f'        {key}: {value}')
        index += 1
        print()

def main():
    w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
    block_number = int(input())
    transactions = get_transactions(block_number, w3)
    transactions_display(transactions)

if __name__ == '__main__':
    main()