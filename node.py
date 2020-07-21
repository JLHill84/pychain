from uuid import uuid4

from blockchain import Blockchain
from verification import Verification


class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'josh'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        tx_recipient = input('recipient name: ')
        tx_amount = float(input('transaction amount: '))
        return (tx_recipient, tx_amount)

    def get_user_choice(self):
        user_input = input('your options: ')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print('printing block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('please choose')
            print('1: add new transaction')
            print('2: mine new block')
            print('3: display blocks')
            print('4: check transaction validity')
            print('q: quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('transaction added')
                else:
                    print('transaction failed')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('all transactions valid')
                else:
                    print('there are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('invalid input, please try again')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('blockchain compromised')
                break
            print(' balance for {}: {:6.2f}'.format(
                self.id, self.blockchain.get_balance()))
        else:
            print('finished')


node = Node()
node.listen_for_input()
