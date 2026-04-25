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
    
def filter_cancellable(arr, check, cancel_event):
    async def work():
        result = []
        for item in arr:
            if cancel_event.is_set():
                break
            if asyncio.iscoroutinefunction(check):
                ok = await check(item)
            else:
                ok = check(item)
            await asyncio.sleep(0)
            if ok:
                result.append(item)
        return result
    return work()