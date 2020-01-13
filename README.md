# Convert

Online currency converter providing a Web API endpoint 💱.

Written in Python 3 using [Flask](https://flask.palletsprojects.com/).

## Usage

### Requirements

TBD

### Run

TBD

### Available endpoints

The application offers an HTTP `GET` `/convert` endpoint which converts the given amount in the given destination currency from the given source currency.

Parameters:
- `amount`: the amount to convert (e.g. `12.35`)
- `src_currency`: ISO currency code for the source currency to convert (e.g. EUR, USD, GBP)
- `dest_currency`: ISO currency code for the destination currency to convert (e.g. EUR, USD, GBP)
- `reference_date`: reference date for the exchange rate, in YYYY-MM-DD format

### Examples

TBD

## Application structure

The application is structured as follows:

- A conversion package which does the dirty work and could be used from external applications
- A rate provider, which is used from the conversion package as dependency
- The HTTP route is provided by Flask, which wraps everything

## Available rate providers

TBD
