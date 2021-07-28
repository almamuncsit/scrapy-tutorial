# Scrapy Tutorial

### Create Project:
```scrapy startproject tutorial```

### Run Spider:
scrapy crawl quotes


### Save Output to JSON File:
```scrapy crawl quotes -o items.json```

```scrapy crawl quotes -o items.csv```

```scrapy crawl quotes -o items.xml```


### Create new spider:
```scrapy genspider example example.com```


## Packages need to be installed:

```pip install mysql-connector-python```

```pip install scrapy-user-agents```

```pip install scrapy-proxy-pool```


