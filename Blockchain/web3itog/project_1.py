from web3 import Web3, HTTPProvider
from threading import Thread
import time

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY'))

# Конфигурация пользователя
address = "..."
private_key = open('utils/key.txt', 'r').readline()

# Флаг для вывода событий
print_event = True

# Настройки контракта
MARKETPLACE_ADDRESS = '0xbfe926450d924d4aa20e46044bab6fffce355245'
true = True
false = False
ABI = [
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"BuyItem","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Cancel","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"price","type":"uint256"}],"name":"FinishAuction","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"price","type":"uint256"}],"name":"ListItem","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"minPrice","type":"uint256"}],"name":"ListItemOnAuction","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"price","type":"uint256"}],"name":"MakeBid","type":"event"},
    {"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"buyItem","outputs":[],"stateMutability":"payable","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"cancel","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"finishAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"list","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"listAuction","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"currentPrice","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint24","name":"bidCount","type":"uint24"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"lastCustomer","type":"address"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"listAuctionId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"listId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"name":"listItem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"minPrice","type":"uint256"}],"name":"listItemOnAuction","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"makeBid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"}]

ERC721_ABI = [
    {"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"approved","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"operator","type":"address"},{"indexed":false,"name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},
    {"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
    {"constant":false,"inputs":[{"name":"operator","type":"address"},{"name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
    {"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
    {"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":true,"inputs":[{"name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":true,"inputs":[{"name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
    {"constant":false,"inputs":[{"name":"to","type":"address"}],"name":"mint","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"}
]

Marketplace = w3.eth.contract(address=MARKETPLACE_ADDRESS, abi=ABI)


# ===============   Обработчики событий   ================
def log_loop_list_item(event_filter, handler, poll_interval):
    while True:
        if print_event:
            for event in event_filter.get_new_entries():
                handler(event)  # Правильная передача события
        time.sleep(poll_interval)


def log_loop_buy_item(event, poll_interval):
    print(f"\nКуплен лот #{event['args']['id']}")
    time.sleep(poll_interval)

def log_loop_cancel(event, poll_interval):
    print(f"\nЛот #{event['args']['id']} снят с продажи")
    time.sleep(poll_interval)


def log_loop_list_item_on_auction(event, poll_interval):
    print(f"\nНовый аукцион #{event['args']['id']}")
    print(f"Минимальная цена: {event['args']['minPrice']} Wei")
    time.sleep(poll_interval)


def log_loop_make_bid(event, poll_interval):
    print(f"\nНовая ставка #{event['args']['id']}")
    print(f"Текущая цена: {event['args']['price']} Wei")
    time.sleep(poll_interval)


def log_loop_finish_auction(event, poll_interval):
    print(f"\nАукцион завершен #{event['args']['id']}")
    print(f"Финальная цена: {event['args']['price']} Wei")
    time.sleep(poll_interval)


# ================    Вспомогательные функции    ==================
def send_transaction(transaction):
    try:
        signed = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        print(f"\nТранзакция отправлена: {tx_hash.hex()}")

        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status:
            print("Транзакция успешно выполнена")
        else:
            print("Ошибка выполнения транзакции")

    except Exception as e:
        print(f"Ошибка: {e}")

def event_tracking_setup():
    global print_event
    print("1. Выводить сообщения о новых событиях")
    print("2. НЕ выводить сообщения о новых событиях")
    choice = int(input("\nВведите номер пункта меню, который выбрали: "))
    if choice == 1:
        print_event = True
    elif choice == 2:
        print_event = False
    menu()


#  =======  Функции, для взаимодействия с контрактом бесплатные - НАЧАЛО  ====
def call_list_id():
    print(f"\nТекущий listId: {Marketplace.functions.listId().call()}")


def call_list_auction_id():
    print(f"\nТекущий listAuctionId: {Marketplace.functions.listAuctionId().call()}")


def call_list():
    id = int(input("Введите ID лота: "))
    item = Marketplace.functions.list(id).call()
    print(f"\nЛот #{id}:")
    print(f"Токен ID: {item[0]}")
    print(f"Цена: {item[1]} Wei")
    print(f"Контракт токена: {item[2]}")
    print(f"Владелец: {item[3]}")


def call_list_auction():
    id = int(input("Введите ID аукциона: "))
    auction = Marketplace.functions.listAuction(id).call()
    print(f"\nАукцион #{id}:")
    print(f"Токен ID: {auction[0]}")
    print(f"Текущая цена: {auction[1]} Wei")
    print(f"Дата начала: {auction[2]}")
    print(f"Ставок: {auction[3]}")
    print(f"Контракт токена: {auction[4]}")
    print(f"Владелец: {auction[5]}")
    print(f"Последний участник: {auction[6]}")
    #  =======  Функции, для взаимодействия с контрактом бесплатные - КОНЕЦ  ======

#  ====    Функции, для взаимодействия с контрактом платные - НАЧАЛО    ====
def call_list_item():
    token_address = input("Адрес контракта токена: ")
    token_id = int(input("ID токена: "))
    price = int(input("Цена в Wei: "))

    tx = Marketplace.functions.listItem(
        token_address,
        token_id,
        price
    ).build_transaction({
        'from': address,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2
    })
    send_transaction(tx)


def call_buy_item():
    item_id = int(input("ID лота: "))
    try:
        item = Marketplace.functions.list(item_id).call()
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    tx = Marketplace.functions.buyItem(item_id).build_transaction({
        'from': address,
        'value': item[1],
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2
    })
    send_transaction(tx)

def call_cancel():
    item_id = int(input("Введите ID лота для отмены: "))

    try:
        item = Marketplace.functions.list(item_id).call()
        token = item[2]
        is_operator = token.functions.isApprovedForAll(item[3], address).call()
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    token_contract = w3.eth.contract(address=item[2], abi=ERC721_ABI)
    is_operator = token_contract.functions.isApprovedForAll(...).call()

    if item[3].lower() != address.lower() and not is_operator:
        print("Нет прав для отмены лота!")
        return

    transaction = Marketplace.functions.cancel(item_id).build_transaction({
        'from': address,
        'chainId': 11155111,
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2,
        'nonce': w3.eth.get_transaction_count(address)
    })

    send_transaction(transaction)

def call_list_item_on_auction():
    token_address = input("Адрес контракта токена: ")
    token_id = int(input("ID токена: "))
    min_price = int(input("Цена в Wei: "))

    tx = Marketplace.functions.listItemOnAuction(
        token_address,
        token_id,
        min_price
    ).build_transaction({
        'from': address,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2
    })
    send_transaction(tx)


def call_make_bid():
    item_id = int(input("ID аукциона: "))
    try:
        auction = Marketplace.functions.listAuction(item_id).call()
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    bid_amount = int(input(f"Введите ставку (минимум {auction[1] + 1} Wei): "))
    if bid_amount <= auction[1]:
        print("Ставка должна быть выше текущей цены!")
        return

    balance = w3.eth.get_balance(address)
    if balance < bid_amount:
        print(f"Недостаточно средств. Баланс: {balance} Wei")
        return

    tx = Marketplace.functions.makeBid(item_id).build_transaction({
        'from': address,
        'value': bid_amount,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2
    })
    send_transaction(tx)

def call_finish_auction():
    item_id = int(input("ID аукциона: "))
    try:
        auction = Marketplace.functions.listAuction(item_id).call()
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    current_time = w3.eth.get_block('latest')['timestamp']
    if current_time < auction[2] + 600:
        print("Аукцион еще не завершился!")
        return

    tx = Marketplace.functions.finishAuction(item_id).build_transaction({
        'from': address,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2
    })
    send_transaction(tx)


# ===========      Меню      ============
def menu():
    while True:
        print("\n" + "=" * 30)
        print("1. Узнать listId")
        print("2. Узнать listAuctionId")
        print("3. Информация о лоте")
        print("4. Информация об аукционе")
        print("5. Выставить лот")
        print("6. Купить лот")
        print("7. Снять лот")
        print("8. Создать аукцион")
        print("9. Сделать ставку")
        print("10. Завершить аукцион")
        print("11. Настройки событий")
        print("12. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            call_list_id()
        elif choice == '2':
            call_list_auction_id()
        elif choice == '3':
            call_list()
        elif choice == '4':
            call_list_auction()
        elif choice == '5':
            call_list_item()
        elif choice == '6':
            call_buy_item()
        elif choice == '7':
            call_cancel()
        elif choice == '8':
            call_list_item_on_auction()
        elif choice == '9':
            call_make_bid()
        elif choice == '10':
            call_finish_auction()
        elif choice == '11':
            event_tracking_setup()
        elif choice == '12':
            exit()


def main():
    POLL_INTERVAL = 10
    events = [
        (Marketplace.events.ListItem, log_loop_list_item),
        (Marketplace.events.BuyItem, log_loop_buy_item),
        (Marketplace.events.Cancel, log_loop_cancel),
        (Marketplace.events.ListItemOnAuction, log_loop_list_item_on_auction),
        (Marketplace.events.MakeBid, log_loop_make_bid),
        (Marketplace.events.FinishAuction, log_loop_finish_auction)
    ]

    for event, handler in events:
        Thread(
            target=handler,
            args=(event.createFilter(fromBlock='latest'), handler, POLL_INTERVAL),
            daemon=True
        ).start()
    menu()

if __name__ == '__main__':
    main()