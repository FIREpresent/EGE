from web3 import Web3, HTTPProvider

def transaction_information(transaction_hash, w3):
    _weis = w3.eth.get_transaction(transaction_hash)['value']
    _from = w3.eth.get_transaction_receipt(transaction_hash)['from']
    _to = w3.eth.get_transaction_receipt(transaction_hash)['to']
    return [_from, _to, _weis]

def request_display(address_sender, address_recipient, weis):
    print(f'From: {address_sender}',
          f'To: {address_recipient}',
          f'Value: {weis} wei',
          sep = '\n')

def main():
    w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
    transaction_hash = input()
    request_display(*transaction_information(transaction_hash, w3))

if __name__ == '__main__':
    main()