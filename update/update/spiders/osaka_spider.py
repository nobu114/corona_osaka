import scrapy


class OsakaSpider(scrapy.Spider):
    name = "osaka"

    def start_requests(self):
        urls = [
            "http://www.pref.osaka.lg.jp/default.html",
            (
                "http://www.pref.osaka.lg.jp/hodo/index.php?"
                "HST_BUCODE=&HST_SYOCODE=&HST_STARTDATE2_START"
                "=2020%2F04%2F27&HST_STARTDATE2_END=2020%2F05%2F04"
                "&HST_STARTDATE2=&HST_TITLE1=%90V%8C%5E%83R%83%8"
                "D%83i%83E%83C%83%8B%83X%8A%B4%90%F5%8F%"
                "C7%8A%B3%8E%D2&SEARCH_NUM=50&searchFlg=%8C%9F%81%40%8D%F5"
                "&site=fumin&start=1"
            )
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"osaka-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
