from request import check_request_time
from wallet_transaction import check_whether_validated_or_rejected


def scheduler_operation():
    try:
        time_limit = 2 * 24 * 3600
        check_whether_validated_or_rejected(time_limit)
        check_request_time()
    except:
        print("Schedular Error")