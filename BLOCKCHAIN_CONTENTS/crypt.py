# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:55:56 2023

@author: sanju
"""

#pip install requests==2.18.4
#in this code we are going to code (Devolop) a cryptocurrency
from collections.abc import Mapping
import datetime
import hashlib
import json
from flask import Flask,jsonify,request
import requests #will be used to cactch the right node
from uuid import uuid4
from urllib.parse import urlparse

class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = [] #we have to create this transactions before create block
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions':self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block
    #we need to create a function for transaction formant like sender,reciever


    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transactions(self, sender,receiver,amount):
        self.transactions.append({'sender':sender,
                                  'reciever':receiver,
                                  'amount':amount})
        pre_block = self.get_previous_block()
        return pre_block['index'] + 1


    def add_node(self,address):
        #to add node containing that address to our set of address
        parsed_url = urlparse(address)
        #now we are ready to add this node to the network
        self.nodes.add(parse_url.netloc)
        
        
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for nodes in network:
            #we have to find the largest chain
            response = request.get('http://127.0.0.1:5000/get_chain') 
# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()


# Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200


# Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


# Checking if the Blockchain is valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valids = blockchain.is_chain_valid(blockchain.chain)
    if is_valids:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

def add_tracastion():
    json = request.get_json()
    transaction_keys = ['sender','reciever','amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    index = blockchain.add_transactions(json['sender'],json['reciver'],json['amount'])
    response = {'message':f'This transaction will be added to block{index}'}
    return jasonify(response), 201


#part 3 decentralizing our blockchain

#connecting new nodes
@app.route('/connect_node',methods = ['Post'])
def connect_node():
    json = request.get_json()
    json.get('node')

# Running the app
app.run(host='0.0.0.0', port=5000)


#part 2 = mine


#part 3 = decentralizing the blockchain (new)