from scrapy import cmdline

#cmdline.execute('scrapy genspider douban movie.douban.com/top250'.split())
cmdline.execute('scrapy crawl douban -o test.csv'.split())
