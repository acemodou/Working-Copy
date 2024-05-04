import time 
from libs.openexchange import OpenExchangeClient

APP_ID = "256e927d9a0c4ca0ab61e85cd5887734"
client = OpenExchangeClient(APP_ID)


usd_amount = 1000
for _ in range(3):
    start = time.time()
    dalasis = client.convert(usd_amount, "USD", "GMD")
    end = time.time()
    print(end - start)
print(f"{usd_amount} USD  is {dalasis} GMD")
