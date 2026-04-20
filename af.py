import threading
import asyncio
 
 
def filter_callback(arr, check, callback):
    def work():
        result = []
        for item in arr:
            if check(item):
                result.append(item)
        callback(result)
    t = threading.Thread(target=work)
    t.start()
    return t
