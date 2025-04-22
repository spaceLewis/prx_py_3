

import urllib.request
import itertools
from queue import Queue
import threading

class ExampleClass(object):
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print("Data:", self.data)

def fetch_url(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code, url)
    except urllib.error.URLError as e:
        print("URL Error:", e.reason, url)

def process_data():
    data_points = range(100) 
    for data in data_points:
        print("Processing data:", data)

def divide(a, b):
    return a / b  

def use_lambda():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    # Sorting with a lambda function
    pairs.sort(key=lambda x: x[0])
    print("Sorted pairs:", pairs)

def thread_function(name, queue):
    while not queue.empty():
        item = queue.get()
        print("Thread", name, "got", item)

def main():
    urls = ["http://example.com", "http://example.net", "http://example.org"]
    results = list(map(fetch_url, urls))

    queue = Queue()
    for i in range(5):
        queue.put(i)

    threading.Thread(target=thread_function, args=("A", queue)).start()
    threading.Thread(target=thread_function, args=("B", queue)).start()

    print("Threads started")

    example = ExampleClass("example data")
    example.print_data()
    process_data()
    print("10 / 3 equals", divide(10, 3))
    use_lambda()

    threading.Thread(target=thread_function, args=("A", queue)).join()
    threading.Thread(target=thread_function, args=("B", queue)).join()

if __name__ == "__main__":
    main()