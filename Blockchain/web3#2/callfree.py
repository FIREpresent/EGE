from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))

true = True
false = False

ABI = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"addPupilEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"},{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"editPupilEvent","type":"event"},{"inputs":[{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"name":"addPupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"},{"internalType":"bool","name":"_blackList","type":"bool"}],"name":"deletePupil","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllPupils","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllPupilsAddress","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pupilAddress","type":"address"}],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPupilByAddress","outputs":[{"components":[{"internalType":"address","name":"pupilAddress","type":"address"},{"internalType":"string","name":"group","type":"string"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"yearsOfSchooling","type":"string"}],"internalType":"struct BlockchainCoursePupils.pupil","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pupilsCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]

contract = w3.eth.contract(
    address='0x7252bFCC2d5eA0AcCf384e8834A6A1f6519099E7',
    abi=ABI
)

a = contract.functions.getAllPupilsAddress().call()
b = contract.functions.getAllPupils().call()
print(a)
print(b)