import json


def download_file(url):
    r = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(r.content)

api_url = 'https://api.fda.gov/download.json'
r = requests.get(api_url)
files = [file['file'] for file in json.loads(r.text)['results']['drug']['event']['partitions']]

count = 1
for file in files:
    download_file(file)
    print(f"{count}/{len(files)} downloaded!")
    count += 1