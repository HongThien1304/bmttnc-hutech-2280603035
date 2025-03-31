from blockchain import BlockChain

# Testting the blockchain
my_blockchain = BlockChain()

# Adding transactions with user input
while True:
    sender = input("Nhap nguoi gui (hoac nhan 'exit' de thoat): ")
    if sender.lower() == 'exit':
        break
    receiver = input("Nhap nguoi nhan: ")
    amount = float(input("Nhap so luong: "))
    
    # Add the transaction to the blockchain
    my_blockchain.add_transaction(sender, receiver, amount)

# Mining a new block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Displaying the blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("--------------------------")

# Check if the blockchain is valid
print("Is BlockChain valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
