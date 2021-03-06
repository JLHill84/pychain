from uuid import uuid4

from blockchain import Blockchain
from util.verification import Verification
from wallet import Wallet


class Node:

    def __init__(self):
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        tx_recipient = input('transaction recipient: ')
        tx_amount = float(input('amount: '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        user_input = input('your pick: ')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print('showing block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('choices!')
            print('1: add transaction')
            print('2: mine block')
            print('3: display blocks')
            print('4: validate transactions')
            print('5: create wallet')
            print('6: load wallet')
            print('7: save keys')
            print('q: quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(
                    self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('transaction added')
                else:
                    print('transaction failed :(')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('mining failed. no wallet?')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('all transactions valid')
                else:
                    print('there are invalid transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('input invalid, try again')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('blockchain invalid')
                break
            print('balance of {}: {:6.2f}'.format(
                self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print('user complete')

        print('finished')


if __name__ == '__main__':
    node = Node()
    node.listen_for_input()
