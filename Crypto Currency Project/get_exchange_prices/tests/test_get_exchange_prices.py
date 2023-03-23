import pandas as pd
import pytest
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json
from json import dumps, loads
from pandas import json_normalize
from get_exchange_prices import get_exchange_prices

def test_valid_input():
    # Test with valid asset and size
    df = get_exchange_prices.get_exchange_prices('BTC', 100)
    assert isinstance(df, pd.DataFrame)


def test_get_exchange_prices_asset_error():
    with pytest.raises(ValueError) as e:
        get_exchange_prices.get_exchange_prices(123, 1000)
    assert str(e.value) == 'Asset must be a non-empty string'

def test_get_exchange_prices_size_error():
    with pytest.raises(ValueError) as e:
        get_exchange_prices.get_exchange_prices('BTC', -10)
    assert str(e.value) == 'Size must be a positive integer'

def test_get_exchange_prices_exchange_error():
    with pytest.raises(ValueError) as e:
        get_exchange_prices.get_exchange_prices('BTC', 1000, exchange='INVALID_EXCHANGE')
    assert str(e.value) == 'Exchange not found'


# In[ ]:




