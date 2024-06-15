import json
import socket
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization


def start_client(message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12345
        client_socket.connect((host, port))
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")
        response = json.loads(response)
        return response

def register_user():
    message = str({
        'headers': {
            "method": "add_node"
        },
        "data": {
            'contract_id': "contract",
        }
    })
    return start_client(message=message)

def login_user(private_key):
    message = str({
        'headers': {
            "method": "log_user"
        },
        "data": {
            'contract_id': "contract",
            "parameters": private_key
        }
    })
    return start_client(message=message)

def do_transaction(private_key , reciever_public_key , amount , transferer_public_key):
    transaction = {
        "transferer_public_key": transferer_public_key,
        "reciever_public_key": reciever_public_key,
        "transfer_amount": amount
    }
    # private_key = "MHQCAQEEIHwik8WBxMcA8u4WQQZp/cZVp56xFXM7sNFg8FQPUQC2oAcGBSuBBAAKoUQDQgAEF3jivBHdIX/cXhF0ktrO0WYwkpxT7Sw9nE7B4B1ZXbnpqa3E8/+oIccV1DPTRxaAiufTJ40rphWKUy4NXqqjyA=="
    json_str = json.dumps(transaction)
    transaction_data = json_str.encode('utf-8')
    pem_private_key = f"""
    -----BEGIN EC PRIVATE KEY-----
    {private_key}
    -----END EC PRIVATE KEY-----
            """
    print(pem_private_key)
    private_key = serialization.load_pem_private_key(
        pem_private_key.encode(),
        password=None,
    )
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_pem_str = public_pem.decode("utf-8")
    public_key_lines = public_pem_str.splitlines()
    public_key_base64 = ''.join(public_key_lines[1:-1])
    digest = hashes.Hash(hashes.SHA256())
    digest.update(transaction_data)
    hash_value = digest.finalize()
    signature = private_key.sign(
        hash_value,
        ec.ECDSA(Prehashed(hashes.SHA256()))
    )
    parameter = {
        "signature": signature,
        "public_key": public_key_base64,
        "transaction_data": transaction_data
    }
    message = str({
        'headers': {
            "method":"transfer_tokens"
        },
        "data": {
            'contract_id': "contract",
            "parameters":parameter
        }
    })
    return start_client(message=message)

def select_nodes(public_key):
    message = str({
        'headers': {
            "method": "select_nodes"
        },
        "data": {
            'contract_id': "contract",
            "parameters": {'public_key':public_key}
        }
    })
    return start_client(message=message)

# response = select_nodes(public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEaYNUaOK3oEV834c0xeA6RV7pHq8leVNrYgqWSHhUCABRUGrrCkMHQvnATljRKd5g+nW2REyuq5voTwkV2cKJrw==")
# print(response)