from web3 import Web3, HTTPProvider
from threading import Thread
import time

w3 = Web3(HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/IiF4PVaEBAdIQxdWCPiiq6re7Z926rr9'))

# инфа о пользователе
address = "__ВСТАВЬТЕ__СЮДА__ВАШ__АДРЕСС_"
private_key = open('utils/key.txt', 'r').readline()

# включаем/отключаем вывод информации о новых событиях
print_event = True

# создание истанса контракта
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
Marketplace = w3.eth.contract(address='__ВСТАВЬТЕ__СЮДА__АДРЕС__КОНТРАКТА__МАРКЕТПЛЕЙСА', abi=ABI)


#  ====    Функции, отслеживающие события - НАЧАЛО    ====

def log_loop_list_item(event_filter, poll_interval):
    while True:
        while not print_event:
            time.sleep(poll_interval)
        for event in event_filter.get_new_entries():
            print("\nNew token is for sale!")
            print(f"id item: {event['args']['id']}")
            print(f"token address: {event['args']['tokenAddress']}")
            print(f"token Id: {event['args']['tokenId']}")
            print(f"price: {event['args']['price']}\n")
        time.sleep(poll_interval)

#     ====     ДОПИШИ ФУНКЦИИ     ====
# def log_loop_buy_item(event_filter, poll_interval):
# def log_loop_cancel(event_filter, poll_interval):
# def log_loop_list_item_on_auction(event_filter, poll_interval):
# def log_loop_make_bid(event_filter, poll_interval):
# def log_loop_finish_auction(event_filter, poll_interval):

#  ====    Функции, отслеживающие события - КОНЕЦ   ====


#  ====    Функции, для взаимодействия с контрактом бесплатные - НАЧАЛО    ====

def call_list_id():
    list_id = Marketplace.functions.listId().call()
    print(f"listId: {list_id}")
    menu()

#     ====     ДОПИШИ ФУНКЦИИ     ====
# def call_list_auction_id():
# def call_list():
# def call_list_auction():

#  ====    Функции, для взаимодействия с контрактом бесплатные - КОНЕЦ    ====


#  ====    Функции, для взаимодействия с контрактом платные - НАЧАЛО    ====

def call_list_item():
    token_address = input("Укажите адрес токена: ")
    token_id = int(input("Укажите id токена: "))
    price = int(input("Укажите цену токена: "))
    # Создаём объект транзакции
    transaction = Marketplace.functions.listItem(token_address, token_id, price).build_transaction({
        'from': address,
        'chainId': 11155111,
        'gas': 300000,
        'maxFeePerGas': w3.eth.gas_price * 2,
        'nonce': w3.eth.get_transaction_count(address)
    })
    send_transaction(transaction)

#     ====     ДОПИШИ ФУНКЦИИ     ====
# def call_buy_item():
# def call_cancel():
# def call_list_item_on_auction():
# def call_make_bid():
# def call_finish_auction():

# def send_transaction(transaction):

#  ====    Функции, для взаимодействия с контрактом платные - КОНЕЦ    ====


#  ====    Прочие функции - НАЧАЛО    ====

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


def menu():
    while True:
        print("\nЧто будем делать?")
        print("1. Узнать listId")
        print("2. Узнать listAuctionId")
        print("3. Получить информацию о лоте из словаря list")
        print("4. Получить информацию о лоте из словаря listAuction")
        print("5. Вызвать функцию listItem")
        print("6. Вызвать функцию buyItem")
        print("7. Вызвать функцию cancel")
        print("8. Вызвать функцию listItemOnAuction")
        print("9. Вызвать функцию makeBid")
        print("10. Вызвать функцию finishAuction")
        print("11. Настроить отслеживание событий")
        print("12. Выйти из программы")
        choice = int(input("\nВведите номер пункта меню, который выбрали: "))
        if choice == 1:
            call_list_id()
        elif choice == 2:
            call_list_auction_id()
        elif choice == 3:
            call_list()
        elif choice == 4:
            call_list_auction()
        elif choice == 5:
            call_list_item()
        elif choice == 6:
            call_buy_item()
        elif choice == 7:
            call_cancel()
        elif choice == 8:
            call_list_item_on_auction()
        elif choice == 9:
            call_make_bid()
        elif choice == 10:
            call_finish_auction()
        elif choice == 11:
            event_tracking_setup()
        elif choice == 12:
            exit()


def main():

    # создание фильтров
    event_filter_list_item = Marketplace.events.ListItem.create_filter(fromBlock="latest")

    #     ====     ДОПИШИ ФИЛЬТРЫ     ====

    # создание потоков
    event_thread_list_item = Thread(target=log_loop_list_item, args=(event_filter_list_item, 10), daemon=True)

    #     ====     ДОПИШИ ПОТОКИ     ====

    # запуск потоков
    event_thread_list_item.start()

    #     ====     ЗАПУСТИ ПОТОКИ     ====

    # запуск меню
    menu()

#  ====    Прочие функции - КОНЕЦ    ====


if __name__ == '__main__':
    main()