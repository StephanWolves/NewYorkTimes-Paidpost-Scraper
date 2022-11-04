import requests
import time
import json

api_key = ''

def search(page, api_key, type):
    
    r = requests.get(f'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=document_type:({type})&page={page}&api-key={api_key}').json()
        
    return r


def save_json(json_data, file_name):
    with open(file_name, "w") as outfile:
        outfile.write(json_data)


def scrape_data(save=False):
    articles = []
    page = 0
    for i in range(100):

        response = search(page, api_key, 'paidpost')

        if 'fault' in response:
            print('Rate exeeded, waiting 10 seconds')
            time.sleep(10)
        
        else:
            print(f'Scraping page {page}')
            for article in response['response']['docs']:
                articles.append(article)
            page += 1
        time.sleep(6)

    print(f'Scraped total of {len(articles)} articles')

    if save:
        save_json(json.dumps(articles), 'scraped_data')

scrape_data(save=True)