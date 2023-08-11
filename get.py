import json

filename='i2pd.json'
with open(filename, 'r') as myfile:
    data = myfile.read()
releases = json.loads(data)

print("https://api.github.com/repos/PurpleI2P/i2pd/releases")
print(filename)
total_by_releases = 0
relcount = 0
for release in releases:
    assets = release["assets"]
    total = 0
    for asset in assets:
        download_count = asset["download_count"]
        total += download_count
    print(f"release tag {release['tag_name']}: total {total} downloads of assets.")
    total_by_releases += total
    relcount += 1
print(f"avg downloads per release: {(0.0+total_by_releases)/relcount}")
