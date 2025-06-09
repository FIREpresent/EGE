from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
print(w3.eth.get_block_number())
# num = int(input())
# print(w3.eth.get_block(num))