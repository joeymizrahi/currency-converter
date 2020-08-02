import requests
import json

API_ENDPOINT = "https://api.exchangeratesapi.io/latest?base=USD"


class Converter:
    """
    Currency converter class to allow conversion btw one currency to another
    """

    def __init__(self):
        """
        constructor that builds class
        """
        self.rates = {}
        self.__connect()

    def __connect(self):
        """
        Connects to the API and defines dictionary of rates
        """
        res = requests.get(API_ENDPOINT)
        self.rates = res.json()["rates"]

    def convert(self, from_currency, to_currency, ammount):
        """
        Does the conversion

        Arguments:
            from_currency {[string]} -- [the currency to convert from]
            to_currency {[string]} -- [the currency to convert to]
            ammount {[int or float]} -- [the ammount to convert]

        Raises:
            ValueError: [When the from currency or to currency arent in the rates dictionary]
            ValueError: [When the ammount given is not a number]

        Returns:
            [float] -- [the conversion ratio]
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"The only known rates are:{self.rates.keys()}")

        if not isinstance(ammount, (int, float)):
            raise ValueError("Please give me a number for the ammount")

        if from_currency == to_currency:
            return ammount
        if from_currency == "USD":
            return self.rates[to_currency] * ammount
        else:
            # transfer to base rate
            ammount = ammount / self.rates[from_currency]
            return self.rates[to_currency] * ammount
