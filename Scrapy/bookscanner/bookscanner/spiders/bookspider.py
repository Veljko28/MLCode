import random
import scrapy
from bookscanner.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    custom_settings = {
        'FEEDS': {
            'bookdata.json': {'format': 'json', 'overwrite': False}
        }
    }

    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]

    def parse(self, response):
        url = "https://books.toscrape.com/"
        books = response.css('article.product_pod')
        next_page = response.css('li.next a::attr(href)').get()

        for book in books:
            book_page = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in book_page:
                url = url+book_page
            else:
                url = "https://books.toscrape.com/catalogue/"+book_page

            #yield {
            #    'name': book.css('h3 a::text').get(),
            #    'price': book.css('.product_price .price_color::text').get(),
            #    'url': book.css('h3 a::attr(href)').get()
            #}

            yield response.follow(url, callback=self.parse_book_page,
                        #headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)] }
                                  )


        if next_page is not None:
            next_page_url = ""
            if 'catalogue' in next_page:
                next_page_url = "https://books.toscrape.com/"
            else:
                next_page_url = "https://books.toscrape.com/catalogue/"

            yield response.follow(next_page_url+next_page, callback=self.parse,
                        #headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)] }
                                  )

    def parse_book_page(self, response):
        table_rows = response.css('table tr')
        book_item = BookItem()

        book_item['url'] = response.url
        book_item['title'] = response.css('.product_main h1::text').get(),
        book_item['upc'] = table_rows[0].css('td ::text').get(),
        book_item['product_type'] = table_rows[1].css('td ::text').get(),
        book_item['price_excl_tax'] = table_rows[2].css('td ::text').get(),
        book_item['price_incl_tax'] = table_rows[3].css('td ::text').get(),
        book_item['tax'] = table_rows[4].css("td ::text").get(),
        book_item['availability'] = table_rows[5].css('td ::text').get(),
        book_item['num_reviews'] = table_rows[6].css('td ::text').get(),
        book_item['stars'] = response.css('p.star-rating').attrib['class'],
        book_item['category'] = response.xpath('//*[@id="default"]/div/div/ul/li[3]/a/text()').get(),
        book_item['description'] = response.xpath('//*[@id="content_inner"]/article/p/text()').get(),
        book_item['price'] = response.css('p.price_color ::text').get()

        yield book_item
