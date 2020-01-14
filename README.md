# Convert

Online currency converter providing a Web API endpoint 💱.

Written in Python 3 using [Flask](https://flask.palletsprojects.com/).

## Usage

### Requirements

- Docker engine v. >= 19.03.4
- Linux / Unix machine w/GNU make installed

### Commands

To start the application, run:

```bash
make start
```

### Available endpoints

The application offers an HTTP `GET` `/convert` endpoint which converts the given amount in the given destination currency from the given source currency.

Parameters:
- `amount`: the amount to convert (e.g. `12.35`)
- `src_currency`: ISO currency code for the source currency to convert (e.g. EUR, USD, GBP)
- `dest_currency`: ISO currency code for the destination currency to convert (e.g. EUR, USD, GBP)
- `reference_date`: reference date for the exchange rate, in YYYY-MM-DD format

### Examples

The [docs/examples](docs/examples) folder provides REST examples.
They are meant to be used on [VSCode](https://code.visualstudio.com) [REST Client plugin](https://github.com/Huachao/vscode-restclient).

## Application structure

The application is structured as follows:

- A conversion package which does the dirty work and could be used from external applications
- A rate provider, which is used from the conversion package as dependency
- The HTTP route is provided by Flask, which wraps everything

## Available rate providers

- `RandomRateProvider`: returns a random exchange rate, used for development purposes
- `ECBRateProvider`: returns exchange rates from European Central Bank, getting data from the https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml endpoint

## Tests

To run tests you will need a local Python 3.7+ environment.

You can run tests by executing:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
make tests
```