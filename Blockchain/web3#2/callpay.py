from web3 import Web3, HTTPProvider

def get_nonce(w3, from_):
    return w3.eth.get_transaction_count(from_)

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))

true = True
false = False

ABI = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"addPupilEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"editPupilEvent","type":"event"},{"inputs":[{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"name":"addPupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"},{"internalType":"bool","name":"_blackList","type":"bool"}],"name":"deletePupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllPupils","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllPupilsAddress","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"}],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pupilsCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]

contract = w3.eth.contract(
    address='0x7252bFCC2d5eA0AcCf384e8834A6A1f6519099E7',
    abi=ABI
)

_type = '0x2'
private_key = open('utils/key.txt', 'r').readline()
my_address = '0x3ccca1bC97E609B236511974794fa260B9cA4af1'
nonce = get_nonce(w3, my_address)
value = int(input('Value: '))
maxFeePerGas = w3.eth.gas_price + 300_000
maxPriorityFeePerGas = 2_000_000
gas = 300_000
chainId = 11155111
group = 's207'
name = 'Mikhail Borisenko'
yearsOfSchooling = '2024-2025'

transaction = contract.functions.addPupil(group, name, yearsOfSchooling).build_transaction({
    'from': my_address,
    'value': value,
    'chainId': chainId,
    'gas': gas,
    'maxFeePerGas': maxFeePerGas,
    'maxPriorityFeePerGas': maxPriorityFeePerGas,
    'nonce': nonce,
    'type': _type,
})

signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_hash)
print(tx_receipt)