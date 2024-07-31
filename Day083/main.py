# MultiProcessing in Python

import multiprocessing
import requests

def downloadFile(url,name):
  response = requests.get(url)
  # open(f"Day083/{name}.jpg","wb").write(response.content)
  # open(f"Day083/Files/file{name}.jpg","wb").write(response.content)
  print(f"Started downloading : fileB{name}")
  open(f"Day083/FilesB/fileB{name}.jpg","wb").write(response.content)
  print(f"Finished downloading : fileB{name}")

if __name__=="__main__":
  # url = "https://picsum.photos/200/300"
  # url = "https://picsum.photos/2000/3000"
  url = "https://picsum.photos/20000/30000"
  processes = []
  for i in range(5):
    # downloadFile(url,i)
    p = multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    processes.append(p)
  
  for pro in processes:
    pro.join()