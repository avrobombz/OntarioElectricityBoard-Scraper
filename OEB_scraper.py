import requests
from bs4 import BeautifulSoup
import time

def oeb_scraper():
    url = "https://www.oeb.ca/rates-and-your-bill/electricity-rates"
    page = requests.get(url)
    status = page.status_code
    
    while status != 200:
        print(str(status) +" retrying connection to OEB....")
        page = requests.get(url)
        status = page.status_code
        time.sleep(10)

    bs = BeautifulSoup(page.content, 'html.parser')
    bs_r = bs.find(id='block-homepageelectricityblock-2')

    off_peak = bs_r.find_all('li', class_='off-peak')
    off_peak_active = len(off_peak) == 0

    mid_peak = bs_r.find_all('li', class_='mid-peak')
    mid_peak_active = len(mid_peak) == 0

    # on_peak = bs_r.find_all('li', class_='on-peak')
    # on_peak_active = len(on_peak) == 0

    if off_peak_active == True:
        peak_elems = bs_r.find_all('li', class_='off-peakactive')
        for peak_elem in peak_elems:
            cost_elem = peak_elem.find('span', class_='value')
            cost = str((cost_elem.text.strip()))
            cost = cost[:-6]
            cost = float(cost)
            peak = "off"

    elif mid_peak_active == True:
        peak_elems = bs_r.find_all('li', class_='mid-peakactive')
        for peak_elem in peak_elems:
            cost_elem = peak_elem.find('span', class_='value')
            cost = str((cost_elem.text.strip()))
            cost = cost[:-6]
            cost = float(cost)
            peak = "mid"

    else:
        peak_elems = bs_r.find_all('li', class_='on-peakactive')
        for peak_elem in peak_elems:
            cost_elem = peak_elem.find('span', class_='value')
            cost = str((cost_elem.text.strip()))
            cost = cost[:-6]
            cost = float(cost)
            peak = "on"

    cost = cost/100
    return [peak, cost]
