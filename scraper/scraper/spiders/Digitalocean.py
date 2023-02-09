import scrapy
# from ..items import QuotesItem
import requests
from bs4 import BeautifulSoup
from ..items import BlogItem

class QuotesSpider(scrapy.Spider):

    start_urls = [
        'https://www.digitalocean.com/community/tutorials']

    name = "digitalocean"

    allowed_domains = ['digitalocean.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://www.digitalocean.com'


    def parse(self, response, **kwargs):
        import json
        # print(all_div_quotes)
        # print()
        res=response.css('div.LayoutCommunityStyles__StyledLayout-sc-1t77shh-0')
        content=res.css('div.TutorialIndexTemplateStyles__StyledWrapper-sc-pkg21j-0')
        postCart=content.css("div.TutorialIndexTemplateStyles__IndexContent-sc-pkg21j-2")
        snglePOst=postCart.css("div.MasonryStyles__Col-sc-n3swdp-1")
        urlsngpost=snglePOst.css('a::attr(href)').extract()

        # contner=response.css('div.LayoutCommunityStyles__StyledLayout-sc-1t77shh-0')
        # postContenr=contner.css('div.TutorialIndexTemplateStyles__IndexContent-sc-pkg21j-2')

        # # print(contner.extract())
        
        # for quote in contner.css('div.TutorialCardListStyles__StyledIndexListItemContainer'):
        #     print(quote.extract())
            # json_object = quote.extract()
            # url = quote.css('a::attr(href)').extract()
            # urlJob = url

            # print(quote)
        for ur in urlsngpost:
            # print(ur)

            comURL = self.base_url + ur
            # book_url = 'https://www.moxa.com/en/products/industrial-network-infrastructure/secure-routers/secure-routers/edr-810-series'
            # print(comURL)
            yield scrapy.Request(comURL, callback=self.parse_book)

    def parse_book(self, response):
        # print(response.url)
        # page = requests.get(response.url).text
        item = BlogItem()

        soup = BeautifulSoup(response.body, 'html.parser')
        tag_obj = soup.title # The first title tag
        # print("###################################")
        # print(tag_obj.string)
        last_a_tag=soup.find("h1", class_="HeadingStyles__StyledH1-sc-kkk1io-0")
        # last_a_tag = soup.find("h1", class_="HeadingStyles__StyledH1-sc-kkk1io-0 inLkjD TutorialTemplate___StyledHeading2-sc-dk9clm-2")

        # last_a_h3=soup.find("h3", class_="Markdown_markdown__wHGCe")
        mydivs = soup.find_all("div", {"class": "Markdown_markdown__wHGCe"})
        content=mydivs


        if last_a_tag   is not None and content   is not None :
            # print(last_a_tag)

            item['detail'] =content
            item['title'] =last_a_tag.string
            yield item


            



        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        # res=response.css('div.LayoutCommunityStyles__StyledLayout-sc-1t77shh-0')
        # content=res.css('div.QuestionAndTutorialOuterContainerStyles__StyledOuterContainer-sc-l9p98c-0')
        # postCart=content.css("div.TutorialTemplateStyles__StyledRecordHeaderContainer-sc-1gdp4d7-0")
        # postTitle=postCart.css("h1::text").extract()
        # cont=postCart.css("div.Markdown_markdown__wHGCe")
        # print(cont.css("h2[1]::text").extract)
        # ntro=cont.css("h3[0]::text")
        # print(cont.extract())
        # for p in cont.xpath('.//p'): 
        #      # extracts all <p> inside
        #     print (p.extract())
                
    # #     item = JobItem()
    #     import json

    # #     #header work post
    #     model=response.css('.modal__body')
    #     pageData = response.css('.tab-section__main')
    #     pass 