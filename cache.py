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
    cache[id] = response_doc
    return

def get_cache(id):
    global cache
    try:
        response = cache[id]
        del cache[id]
        return response
    except:
        return {}

def set_id():
    global cache
    id = latest_id()
    cache[id] = {}
    return id

