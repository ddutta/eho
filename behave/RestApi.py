import requests
from re import match, search, sub
from os.path import dirname, join

echo = True

class RestApi():
    def __init__(self):
        self.baseurl = ""
        self.token = "5af9c6e50aa94dfc92f5163f68f02909"
        for line in open(join(dirname(__file__), "config.txt"), "r"):
            m = match('^baseurl\s*=\s*\"(?P<url>http://.*)/*\"$', line)
            if m:
                self.baseurl = m.group("url")
                break

    def execute_post(self, url, body = ""):
       URL = self.baseurl + url
       resp = requests.post(URL, data = body, headers = {"x-auth-token": self.token,"Content-Type":"application/json"})
       if echo:
           print("URL = %s\ndata = %s\nresponse = %s\n" % (URL, body, resp.status_code))
       return resp

    def execute_get(self, url):
        URL = self.baseurl + url
        resp = requests.get(URL, headers = {"x-auth-token": self.token})
        if echo:
            print("URL = %s\nresponse = %s\n" % (URL, resp.status_code))
        return resp

    def execute_delete(self, url, body = ""):
        URL = self.baseurl + url
        resp = requests.delete(URL, data = body, headers = {"x-auth-token": self.token, "Content-Type":"application/json"})
        if echo:
            print("URL = %s\ndata = %s\nresponse = %s\n" % (URL, body, resp.status_code))
        return resp

    def get_cluster(self):
        url = "/clusters"
        res = self.execute_get(url)
        return res
	
    def create_cluster(self, cluster):
        url = "/clusters"
        body = cluster
        res = self.execute_post(url, body)
        return res
	
    def delete_cluster(self, cluster):
        url = "/clusters/dcb487e5537043309073ce63b0938c07"
        body = cluster
        res = self.execute_delete(url, body)
        return res
	
    def get_template(self):
        url = "/node-templates"
        res = self.execute_get(url)
        return res

    def create_template(self, template):
	url = "/node-templates"
        body = template
        res = self.execute_post(url, body)
        return res
	
    def delete_template(self, template):
        url = "/node-templates/6d99bb3437b44144b8878380014b8e37"
        body = template
        res = self.execute_delete(url, body)
        return res
