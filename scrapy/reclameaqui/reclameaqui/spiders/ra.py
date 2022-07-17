import scrapy


class RaSpider(scrapy.Spider):
    name = 'ra'
    
    start_urls = ['https://www.reclameaqui.com.br/empresa/itau/lista-reclamacoes/']

    def parse(self, response, **kwargs):
        pass
