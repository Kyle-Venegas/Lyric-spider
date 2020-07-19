import scrapy
from scrapy.crawler import CrawlerProcess
import os

def album_ask():
    artist = (input('Artist name?: ')).replace(' ','-')
    album = (input('Album name?: ')).replace(' ','-')
    album_url = 'https://genius.com/albums/' + artist + '/' + album
    return album_url

class song_Spider(scrapy.Spider):
    name = 'lyric'

    start_urls = [album_ask()]

    custom_settings = {
            'LOG_ENABLED' : False,
            'CONCURRENT_REQUESTS' : 1
            }

    def parse(self, response):
        links = response.css('a.u-display_block ::attr(href)').getall()
        prio = len(links)
        for link in links:
            yield scrapy.Request(link, self.parse_lyrics, priority = prio)
            prio -= 1

    def parse_lyrics(self, response):
        os.system('clear')
        h1 = response.css('h1::text').get()
        h2 = response.css('h2 a::text').get()
        print(h2, ' - ', h1, '\n')
        for line in response.css('div.lyrics ::text').getall()[2:-2]:
            print(line, end='')
        delay = input('')

def lyric():
    process = CrawlerProcess()
    process.crawl(song_Spider)
    process.start()

if __name__ == '__main__':
    lyric()
