from enum import Enum


class ResponseMessage(str, Enum):
    INVALID_INPUT_FORMAT = 'Invalid input format'
    SUCCESS = 'success'
    ERROR = 'error'
    DB_QUERY_ERROR = 'db query failed'
    NOT_FOUND = 'not found'
    TRANSACTION_FAILED = 'transaction failed'
    ACCOUNT_ID_NOT_FOUND = 'Account Id not found'
    ZILA_HANDLE_EXIST = 'zilaHandle already taken'
    ACCOUNT_ALREADY_EXIST = 'account already exist'
    ACCOUNT_DOESNOT_EXIST = 'account does not exist'
    POST_DOESNOT_EXIST = 'post does not exist'
    BOTH_ACCOUNT_AND_FOLLOWER_SHOULD_EXIST = 'both account and follower should exist'
    ERC20_ALREADY_EXIST = 'ERC20 already exist'
    ERC20_DOES_NOT_EXIST = 'ERC20 does not exist'
    INVALID_BLOCKCHAIN = 'Invalid blockchain'
    INVALID_AUTHENTICATION = 'Authentication Token Is Invalid'
    MISSING_TOKEN = 'Authentication Token Is Missing'
    ERROR_MEAL = 'Meal type is not valid in this time'
    ORDER_UPDATE_ERROR = 'Your order can not update at this time'
    PACKET_LIMIT_ERROR = "message"
