from hdfs import InsecureClient
import os
client = InsecureClient('http://localhost:9870', user='m2')

# file_list = client.content('dat')
# print(file_list)

# 한 번 실행하면 폴더가 이미 만들어져있으므로 중복실행은 안됨
# client.makedirs('/input/logs/')

local_file_path = '/Users/m2/damf2/data/bitcoin/'
hdfs_file_path = '/input/bitcoin/'

local_files = os.listdir(local_file_path)
# print(local_files)

for file_name in local_files:
    if not client.content(hdfs_file_path + file_name, strict=False):
        client.upload(hdfs_file_path + file_name, local_file_path + file_name)