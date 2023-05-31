#module1 - create a blockchain

#part 1 - building a blockchain
import datetime  #
import hashlib  #this lib is used for hash the blocks
import json #used for dumps functions from this library to encode the blocks before we use them
from flask import Flask, jsonify  #jasonily used to return the mgs and postman when we interact with our blockchain


class blockchain:
	#we will initialize all the components of the blockchain
	
	def __init__(self):
			self.chain = []  #a list containg several blocks
			self.create_block(proof = 1,prev_hash = '0') #this is a first block (genesis) so prev value is 0
			
	def create_block(self,proof,prev_hash):
				block = {'index':len(self.chain)+1,
									'timestamp': str(datetime.datetime.now()),
										'proof' : proof,
										'prev_hash' : prev_hash
										#'data' : 
								}
				self.chain.append(block)
				return block
def proof_of_work(self,prev_proof):
		new_proof = 1 #to solve the problem we are going to increment this
		check_proof = False
		while check_proof is False:
				hash_operation = hashlib.sha256(str(new_proof**2 + prev_proof**2).encode()).hexdigest()
				#we will check the first 4 char os the hash function is 0's
				#if they are 4 0's the miners win and check_proof will be set to true
				if hash_operation[:4] == '0000':
							check_proof = True
				else:
						#check_proof = False
						new_proof += 1
		return new_proof    
def hash(self,block):
		encoded_block = json.dumps(block,sort_keys = True).encode()
		return hashlib.sha256(encoded_block).hexdigest()

def is_chain_valid(self,chain):
		prev_block = chain[0]
		block_index = 1
		while block_index < len(chain):
				block = chain[block_index]
				if block['prev_hash'] != self.hash(prev_block):
					return False
				prev_proof = prev_block['proof']
				proof = block['proof']
				hash_operation = hashlib.sha256(str(proof**2 + prev_proof**2).encode()).hexdigest()
				if hash_operation[:4] != '0000':
        				return False
				prev_block = block
				block_index += 1
        				   
#part 2 - mining our blockchain

#creating a web app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
blockchain = blockchain()
#mining a new block
@app.route('/mine_block',methods = ['Get'])
def mine_block():
    #it has to mine a block 
    #it has to solve proof of work problem
    prev_block = blockchain.get_prev_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof,prev_hash)
    response = {'message':'Congrates you mined a block',
                'index': block['index'],
                'timestamp ': block['timestamp'],
                'proof' : block['proof'],
                'prev_hash' : block['prev_hash']}
    return jasonify(response) ,200  #this is a http status code 200-ok

@app.route('/get_chain',methods = ['Get'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length' : len(blockchain.chain)}
    return jasonify(response) , 200

app.run(host = '0.0.0.0',port = 5000)