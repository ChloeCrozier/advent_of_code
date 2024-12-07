from dotenv import load_dotenv
import requests
import sys
import os

load_dotenv(dotenv_path='../.env', verbose=True)
session_id = os.getenv('AOC_SESSION_ID')

if len(sys.argv) < 2:
    print('Usage: python get_input_data.py AOC {DAY}')
    sys.exit(1)
else:
    url = f'https://adventofcode.com/2024/day/{sys.argv[1]}/input'
    headers = {'Cookie': f'session={session_id}'}
    page = requests.get(url, headers=headers)
    print(page.text)

    input_file = open(f'input/day{sys.argv[1]}.txt', 'w')
    input_file.write(page.text)
    print(f'Input data saved to day{sys.argv[1]}.txt!')