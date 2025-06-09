from web3 import Web3
import threading
import time


def track_blocks(provider_url, stop_flag):
    w3 = Web3(Web3.HTTPProvider(provider_url))
    if not w3.is_connected():
        print("Ошибка подключения к сети")
        return

    block_filter = w3.eth.filter("latest")
    print("Начало отслеживания блоков")

    try:
        while stop_flag['running']:
            try:
                new_blocks = w3.eth.get_filter_changes(block_filter.filter_id)

                for block_hash in new_blocks:
                    block = w3.eth.get_block(block_hash.hex(), full_transactions=True)

                    total_eth = sum(
                        w3.from_wei(tx.value, 'ether')
                        for tx in block.transactions
                    )

                    print(f"\nБлок: {block.number}")
                    print(f"Хеш: {block.hash.hex()}")
                    print(f"Транзакций: {len(block.transactions)}")
                    print(f"Всего ETH: {total_eth:.6f}")
                    print("-" * 40)

            except Exception as e:
                print(f"Ошибка: {e}")
                time.sleep(5)
    finally:
        w3.eth.uninstall_filter(block_filter.filter_id)

def main():
    PROVIDER_URL = "https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9"
    stop_flag = {'running': True}
    thread = threading.Thread(target=track_blocks, args=(PROVIDER_URL, stop_flag))
    thread.start()

    input("Нажмите Enter для остановки...\n")
    stop_flag['running'] = False
    thread.join()
    print("Мониторинг остановлен")

if __name__ == "__main__":
    main()