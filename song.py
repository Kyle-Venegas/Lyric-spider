import scrapy
from scrapy.crawler import CrawlerProcess
import os

def ask():
    artist = input('Artist name?: ')
    song = input('Song name?: ')
    artist_song = artist + ' ' + song
    full = artist_song.replace(' ', '-')
    url = 'https://genius.com/' + full + '-lyrics'
    return url

class lyricSpider(scrapy.Spider):
    name = 'lyric'

    start_urls = [ask()]

    custom_settings = {
            'LOG_ENABLED' : False
            }

    def parse(self, response):
        os.system('clear')
        for line in response.css('div.lyrics ::text').getall()[2:-2]:
            print(line, end='')
        delay = input('')

def lyric():
    process = CrawlerProcess()
    process.crawl(lyricSpider)
    process.start()

if __name__ == '__main__':
    lyric()
