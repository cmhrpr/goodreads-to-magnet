# README


## Installing dependencies

### Python

Run the following to install Python dependencies:

```console
pip install -r requirements.txt
```


## Downloading data from Goodreads 

You will need the following:

* Your Goodreads user ID - go to your profile and copy the link 
* A [Gooreads API Key](https://www.goodreads.com/api/keys)

First, authenticate with Goodreads by running the following:

```console
goodreads-to-sqlite auth
```


## Getting book titles from the database

Run the following to import the .env file:

```console
source .env
```

Run the Python script:

```console
python extract-book-titles.py
```

## Getting magnet URLs from booktitles


## End to End
