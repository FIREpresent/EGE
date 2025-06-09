from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
transaction_hash = input()
print(w3.eth.get_transaction(transaction_hash),
      w3.eth.get_transaction_receipt(transaction_hash),
      sep='\n')