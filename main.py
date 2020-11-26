import scraper

#scrape current energy rates from Ontario Energy Board
scraped = scraper.oeb_scraper()
    
c_peak = scraped[0]
c_cost = scraped[1]

print(c_cost)
print(c_peak)

