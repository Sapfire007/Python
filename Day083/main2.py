import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"Day083/FilesC/fileC{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")



url = "https://picsum.photos/20/30"
# pros = []
# for i in range(50):
#   # downloadFile(url, i)
#   p = multiprocessing.Process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)