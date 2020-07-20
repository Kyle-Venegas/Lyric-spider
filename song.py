import scrapy
from scrapy.crawler import CrawlerProcess
import os

def ask():
    artist = (input('Artist name?: ')).replace(' ','-')
    song = (input('Song name?: ')).replace(' ','-')
    artist_song = artist + '-' + song
    url = 'https://genius.com/' + artist_song + '-lyrics'
    return url

class lyricSpider(scrapy.Spider):
    name = 'lyric'

    start_urls = [ask()]

    custom_settings = {
            'LOG_ENABLED' : False
            }

    def parse(self, response):
        os.system('clear')
        h1 = response.css('h1::text').get()
        h2 = response.css('h2 a::text').get()
        print(h2, ' - ', h1, '\n')
        for line in response.css('div.lyrics ::text').getall()[2:-2]:
            print(line, end='')
        delay = input('')

def lyric():
    process = CrawlerProcess()
    process.crawl(lyricSpider)
    process.start()

if __name__ == '__main__':
    lyric()
