cache = {}

def latest_id():
    global cache
    keys = list(cache.keys())
    n = len(keys) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(keys)
    missing_number = expected_sum - actual_sum
    return missing_number

def add_cache(response_doc , id):
    global cache
    cache[id]['response'] = response_doc
    return

def get_cache(id):
    global cache
    try:
        response = cache[id]['response']
        del cache[id]
        return response
    except:
        return {}

def check_cache(id):
    global cache
    try:
        response = cache[id]['operation_started']
        return response
    except:
        return False

def check_operation(id):
    global cache
    try:
        response = cache[id]['operation_finished']
        return response
    except:
        return False

def set_id():
    global cache
    id = latest_id()
    cache[id] = {
        'operation_started':False,
        'operation_finished': False,
        "response":{}
    }
    return id

def set_start(id):
    global cache
    cache[id]['operation_started'] = True
    return

def set_finished(id):
    global cache
    cache[id]['operation_finished'] = True
    return

