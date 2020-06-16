# Craigslist Watcher

Keep yourself in the loop about updates to Craigslist listings

## Installation

Requires `scrapy`:
`pip3 install scrapy`

## Usage

Create `conf.json` with the following in the same directory as `watcher.py`:

```json
{
    "user":"myExchangeEmailAddr@some.com",
    "password":"my_password",
    "mailto":"theEmailToSendUpdatesTo@example.com",
    "smtp_server": "my.smtp.server.com",
    "port": 587,
    "urls": ["https://pittsburgh.craigslist.org/search/sss?query=klr%20650&sort=rel",
             "https://philadelphia.craigslist.org/search/sss?query=klr%20650&sort=rel"]
}
```

Edit the following lines of `conf.json` by changing start_urls to the URL of your Craigslist search (i.e. go to Craigslist, search 'klr 650' and put whatever is in the address bar in here as string literals):

```json
    "urls": ["https://pittsburgh.craigslist.org/search/sss?query=klr%20650&sort=rel",
             "https://philadelphia.craigslist.org/search/sss?query=klr%20650&sort=rel"]
```

And then run the whole thing with:

`python3 watcher.py ~/path_to_conf.json ~/path_to_metadata_can_really_be_anything.json`

It is usually effective as a crontab job, so that you can get email updates every day when there's a new listing.
