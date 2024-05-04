import functools
import requests
from cachetools import cached, TTLCache

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id : str) -> None:
        self.app_id = app_id
    
    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=90))
    def latest(self) -> dict:
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()
    
    def convert(self, currency_amount : int, from_currency : str, to_currency : str) -> int:
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return currency_amount * to_rate
        else:
            in_usd = currency_amount / rates[from_currency]
            return in_usd * to_rate

    