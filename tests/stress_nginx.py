import requests
import time
from multiprocessing import Pool

# Replace with the URL of your web server
url = "http://localhost"

# Duration for which to generate high traffic, in seconds
duration = 5

def load_url(url):
    # Request the server
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")

# Pool of 4 workers to make the GET requests
pool = Pool(processes=4)

# Record time
start = time.time()

# Run while loop for the desired duration and stop when duration is reached
while time.time() - start < duration:
    pool.apply_async(load_url, (url,))

pool.close()
pool.join()