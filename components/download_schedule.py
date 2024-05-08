import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")

def download_schedule():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(URL, headers=headers, verify=False)
    with open('./schedule.xlsx', 'wb') as f:
        f.write(r.content)