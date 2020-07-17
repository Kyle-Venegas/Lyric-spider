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

url_list = []
def new_ask():
    artist = input('Artist name?: ')
    tracks = int(input('How many tracks?: '))
    for track in range(tracks):
        song = input('song name?: ')
        artist_song = artist + ' ' + song
        full = artist_song.replace(' ', '-')
        url = 'https://genius.com/' + full + '-lyrics'
        url_list.append(url)

    return url_list

class lyricSpider(scrapy.Spider):
    name = 'lyric'

#   start_urls = [ask()]
    start_urls = new_ask()

    custom_settings = {
            'LOG_ENABLED' : False,
            'CONCURRENT_REQUESTS' : 1
            }

    def parse(self, response):
        os.system('clear')
        h1 = (response.css('h1::text').get())
        h2 = (response.css('h2 a::text').get())
        print(h2, ' - ', h1, '\n')
        for line in response.css('div.lyrics ::text').getall()[2:]:
            print(line, end='')
        delay = input('')

def lyric():
    process = CrawlerProcess()
    process.crawl(lyricSpider)
    process.start()

if __name__ == '__main__':
    lyric()
