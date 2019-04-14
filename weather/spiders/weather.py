import scrapy

class WeatherSpider(scrapy.Spider):
    name = "weather"
    start_urls = [
        'https://weather.com/zh-CN/weather/today/l/CHXX0008:1:CH',
    ]

    def parse(self, response):
        location = response.css('.h4.today_nowcard-location::text')
        alarm = response.css('.title.text.text-overflow div span::text')
        weather = response.css('.today_nowcard-phrase::text')
        temp = response.css( '.deg-feels::text' )
        yield {
            'location': location.get(),
            'temp': temp.get(),
            'alarm': alarm.get(),
            'weather': weather.get()
        }
        # yield {
        #     'alarm': weather.css('a[class^=alarm]::text').get(),
        #     'temperture': weather.css('.skInfo #temp::text').get(),
        #     'air': weather.css('#aqi::text').get(),
        #     'windD': weather.css('#windD::text').get(),
        #     'windS': weather.css('#windS::text').get(),
        #     'sd': weather.css('#sd::text').get(),
        # }