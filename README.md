## Usage

Create `email.json` with the following in the same directory as `watcher.py`:

```json
{
    "user":"myExchangeEmailAddr@some.com",
    "password":"my_password",
    "mailto":"theEmailToSendUpdatesTo@example.com"
}
```

Edit the following lines of `watcher.py` by changing start_urls to the URL of your Craigslist search (i.e. go to Craigslist, search 'klr 650' and put whatever is in the address bar in here as string literals):

```python
    class CLSpider(Spider):
        name = "cl-spider"
        start_urls = ["https://pittsburgh.craigslist.org/search/sss?query=klr%20650&sort=rel",
                      "https://philadelphia.craigslist.org/search/sss?query=klr%20650&sort=rel"]
```

And then run the whole thing with:

`python3 watcher.py`

It is usually effective as a crontab job, so that you can get email updates every day when there's a new listing.