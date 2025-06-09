from web3 import Web3, HTTPProvider

def get_nonce(w3, from_):
    return w3.eth.get_transaction_count(from_)

def make_transaction(from_, to_, value_, chainId_, maxFeePerGas_, nonce_, type_, gas_, maxPriorityFeePerGas_, private_key_, w3):
    transaction = {
        'from': from_,
        'to': to_,
        'value': value_,
        'chainId': chainId_,
        'gas': gas_,
        'maxFeePerGas': maxFeePerGas_,
        'maxPriorityFeePerGas': maxPriorityFeePerGas_,
        'nonce': nonce_,
        'type': type_,
    }

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key_)

    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def main():

    w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))
    my_address = '0x3ccca1bC97E609B236511974794fa260B9cA4af1'
    _type = '0x2'
    private_key = open('utils/key.txt', 'r').readline()

    nonce = get_nonce(w3, my_address)

    person_address = input('Person address: ')
    value = int(input('Value: '))
    maxFeePerGas = w3.eth.gas_price + 300_000
    maxPriorityFeePerGas = 2_000_000
    gas = 21000

    chainId = 11155111
    if w3.is_address(person_address):
        print(make_transaction(my_address,
                         person_address,
                         value,
                         chainId,
                         maxFeePerGas,
                         nonce,
                         _type,
                         gas,
                         maxPriorityFeePerGas,
                         private_key,
                         w3))
    else:
        print('Error')

if __name__ == '__main__':
    main()

