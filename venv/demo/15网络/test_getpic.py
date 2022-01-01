import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)

# < divclass ="grid-item work-thumbnail" >
# <a href="http://www.cnu.cc/works/554515"
# class ="thumbnail" target="_blank" >
# < divclass ="title" >【溪涧】< / div >#
#
# < divclass ="grid-item work-thumbnail" >
# < a href = "(.*?)".*title>"(.*?)</div>"
# < divclass ="title" >()< / div >

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s','', name))
