from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
person_address = input()
if w3.is_address(person_address):
    print(w3.eth.get_balance(person_address))
else:
    print('Error')