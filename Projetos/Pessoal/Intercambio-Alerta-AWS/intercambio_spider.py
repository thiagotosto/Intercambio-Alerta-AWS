import scrapy


class IntercambioSpider(scrapy.Spider):
    name = "intercambio"
    start_urls = [
        'http://www.sr2.uerj.br/dci/index.php/editais',
    ]
    i = 0

    def parse(self, response):
        for new in response.css('td.list-title'):
            #print new.css('a::text').extract_first()
            #print new.css('a::text').extract_first().strip('\n')

	    yield {
                'text': new.css('a::text').extract_first().strip('\n').strip('\t'),
		#'author': new.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
