import asyncio
import threading
from af import filter_callback, filter_cancellable

numbers = list(range(1, 21))

def is_even(n):
return n % 2 == 0

print(”Callback”)
done = threading.Event()
filter_callback(numbers, is_even, lambda r: (print(r), done.set()))
done.wait()

print(”Cancellable”)
async def demo():
cancel = asyncio.Event()
asyncio.get_event_loop().call_later(0.01, cancel.set)
result = await filter_cancellable(list(range(1, 10001)), is_even, cancel)
print(f”got {len(result)} items before cancel”)

asyncio.run(demo())