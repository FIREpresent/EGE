from web3 import Web3
import threading
import time


def track_transactions(provider_url, stop_flag, address):
    w3 = Web3(Web3.HTTPProvider(provider_url))
    if not w3.is_connected():
        print("Ошибка подключения к сети")
        return

    transaction_filter = w3.eth.filter("pending")
    print(f"Начало отслеживания тразакция с адреса {address}")

    try:
        while stop_flag['running']:
            try:
                new_transactions = w3.eth.get_filter_changes(transaction_filter.filter_id)

                for transaction_hash in new_transactions:
                    transaction = w3.eth.get_transaction(transaction_hash)
                    if transaction['from'] == address or transaction['to'] == address:
                        print(f'Адрес отправителя: {transaction["from"]}')
                        print(f'Адрес получателя: {transaction["to"]}')
                        print(f'Всего переслано эфира: {transaction["value"]}')
                        print('\n')

            except Exception as e:
                print(f"Ошибка: {e}")
                time.sleep(5)
    finally:
        w3.eth.uninstall_filter(transaction_filter.filter_id)

def main():
    PROVIDER_URL = "https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9"
    stop_flag = {'running': True}

    address = input("Введите адрес: ")

    thread = threading.Thread(target=track_transactions, args=(PROVIDER_URL, stop_flag, address))
    thread.start()

    input("Нажмите Enter для остановки...\n")
    stop_flag['running'] = False
    thread.join()
    print("Мониторинг остановлен")

if __name__ == "__main__":
    main()

#0x7B55f2b7798EaF2ac2165f6b5F86d41f674002b7