import requests
import json
import configparser

conf = configparser.ConfigParser()
conf.read("py-aria2.conf")

server = conf.get("aria2-server","server")
token = conf.get("aria2-server","token")
token = "token:"+token
dir = conf.get("aria2-server","dir")


def addUri(url,dir):
    payload = {"jsonrpc":"2.0","method":"aria2.addUri","id":"ID","params":[token,[url],{"dir":dir}]}
    r=requests.post(server,json=payload)
    r.raise_for_status()
    response=r.json()
    print('成功添加下载任务，下载任务的GID是',response['result'])



class mission:

    def __init__(self,gid,dir,url):
        self.gid = gid
        self.dir = dir
        self.url = url
        addUri(url,dir)


