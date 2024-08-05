from blockchian_plugin import login_user, get_chain
from wallet_transaction import add_validation


def test_login():
    private_key = "MHQCAQEEIN+35WwsePG01XMdgTqjJxXpzdh96bnanHMUwiSA6ZsooAcGBSuBBAAKoUQDQgAE4LFVuhHnR0gy7I5T10WMQVaKNAX6TWkdZHwoCLsDuXiOzWlR/x2UAlPI50ty+IHh+k67TrKw+thd9rMPJcjRwg=="
    res = login_user(private_key)
    print(res)

def test_transaction():
    private_key = "MHQCAQEEIAUD9NeEfUjJLe1adNGlIkpaoVS3jEL+KrluWbw+rZAgoAcGBSuBBAAKoUQDQgAEDqu3u6CSYfD2yWK+d5x8zqLDRDU5IFTxkGhEw7hcO+nVzFFeR5srF7Z7tABIa9ibv3GElVr/312IB3LWvvt6Zw=="
    reciever_public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE5TeoeEpCC+V0BXdjaUnRtd0phNdbSO/TrzCk4g1rSDrTdB0oOLVY0vUWGlllgi68hnwbPDSrbroTPRz8wcqZdw=="
    transferer_public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEDqu3u6CSYfD2yWK+d5x8zqLDRDU5IFTxkGhEw7hcO+nVzFFeR5srF7Z7tABIa9ibv3GElVr/312IB3LWvvt6Zw=="
    request_id = "668cd51afad294919c4e6f12"
    amount = 20
    res =  add_validation(private_key, reciever_public_key, amount, transferer_public_key, request_id=request_id)
    print(res)

def get_chain_():
    res = get_chain("MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwhYr+Ggz0xDTS1Q4SYdoSwgHxdz22OPBETsJUcS6eCi4eG9NDva0xDzDLlNThS0JicPf05CyKVdXfjDZ153wKw==")
    print(res)

# get_chain_()
test_login()