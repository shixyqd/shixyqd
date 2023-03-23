# get_exchange_prices

This function makes a request to an external API CryptingUp, fetches data for a given cryptocurrency asset in the available exchanges, 
    and filters the results based on specified parameters. The function returns the filtered data in the form of a Pandas DataFrame. 

## Installation

```bash
$ pip install get_exchange_prices
```

## Usage

- It takes six parameters:

    asset: (str) The asset for which to retrieve market data.<br>
    size: (int) The number of markets to retrieve.<br>
    exchange: (optional) The exchange ID to filter the results by. There are 7 available exchanges: 'BINANCE', 'HUOBIGLOBAL', 'COINBASE', 'KRAKEN', 'BITFINEX', 'POLONIEX', 'BITTREX'.<br>
    base_asset: (optional) The base asset to filter the results by.<br>
    quote_asset: (optional) The quote asset to filter the results by.<br>
    sort_by: (optional) A string indicating how to sort the results. Examples: 'exchange_id','base_asset','quote_asset','price','volume_24h',etc.<br>
    If any of the optional parameters are specified, the function filters the results accordingly before returning a Pandas DataFrame containing the filtered data.  <br>
    
    Returns:<br>
    Pandas DataFrame: A DataFrame containing the filtered and sorted cryptocurrency data.<br>
    
    Example:<br>
    df=get_exchange_price('USDT', 1000, exchange='BINANCE', quote_asset= 'USDT', sort_by='volume_24h')

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`get_exchange_prices` was created by Xinyi Shi. It is licensed under the terms of the MIT license.

## Credits

`get_exchange_prices` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
