import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json
from json import dumps, loads
from pandas import json_normalize


# In[295]:


def get_exchange_prices(asset, size, exchange=None, base_asset=None, quote_asset=None, sort_by=None):
    
    """
    This function makes a request to an external API CryptingUp, fetches data for a given cryptocurrency asset in the available exchanges, 
    and filters the results based on specified parameters. The function returns the filtered data in the form of a Pandas DataFrame.
    
    It takes six parameters:

    asset :(str) The asset for which to retrieve market data.
    size: (int) The number of markets to retrieve.
    exchange: (optional) The exchange ID to filter the results by. There are 7 available exchanges: 'BINANCE', 'HUOBIGLOBAL', 'COINBASE', 'KRAKEN', 'BITFINEX', 'POLONIEX', 'BITTREX'.
    base_asset: (optional) The base asset to filter the results by.
    quote_asset: (optional) The quote asset to filter the results by.
    sort_by: (optional) A string indicating how to sort the results. Examples: 'exchange_id','base_asset','quote_asset','price','volume_24h',etc.
    If any of the optional parameters are specified, the function filters the results accordingly before returning a Pandas DataFrame containing the filtered data.  
    
    Returns:
    Pandas DataFrame: A DataFrame containing the filtered and sorted cryptocurrency data.
    
    Example:
    df=get_exchange_price('USDT', 1000, exchange='BINANCE', quote_asset= 'USDT', sort_by='volume_24h')
    
    """
    
    #All available exchanges id
    all_exchanges_id = ['BINANCE', 'HUOBIGLOBAL', 'COINBASE', 'KRAKEN', 'BITFINEX', 'POLONIEX', 'BITTREX']
    
    # Ensure that the asset argument is a non-empty string
    if not isinstance(asset, str) or not asset:
        raise ValueError('Asset must be a non-empty string')
        
    # Ensure that the size argument is a positive integer
    if not isinstance(size, int) or size <= 0:
        raise ValueError('Size must be a positive integer')

    # Make API request and process data
    assets = requests.get('https://cryptingup.com/api/assets/' + asset + '/markets?size=' + str(size))
    data_assets = assets.json()
    data_assets_df = json_normalize(data_assets['markets'])
        
    # Filter results based on specified parameters
    if exchange is not None:
        data_assets_df = data_assets_df[data_assets_df.exchange_id == exchange]
        if exchange not in all_exchanges_id:
            raise ValueError('Exchange not found')
    if base_asset is not None:
        data_assets_df = data_assets_df[data_assets_df.base_asset == base_asset]
    if quote_asset is not None:
        data_assets_df = data_assets_df[data_assets_df.quote_asset == quote_asset]
            
    # Sort the results if a sort field is specified
    if sort_by is not None:
        data_assets_df = data_assets_df.sort_values(sort_by)
    
    # Output when the filtered dataframe is empty
    if data_assets_df.empty:
        return 'No data available'
    
    return data_assets_df