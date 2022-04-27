import requests
import re
import html
import json
import csv   


print("Scraping alltrails.com");


lastTrailId = 10259537
loop = 1
trailIds = {}

while loop < 100:
  print(loop, "url: ", lastTrailId)
  allTrails = requests.get("https://www.alltrails.com/api/alltrails/v2/trails/"+str(lastTrailId)+"/photos?per_page=6", headers={"authority": "www.alltrails.com", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", 'accept-language': 'en-US,en;q=0.9', 'cookie': '_alltrails_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWY2Y2NlZjdkMGE1YWI4YmNlZjFiMGMwYzg1NmVlMjU1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXAzQzNScCtrSURZci8wVUdlT2pDV3AwWW9mYS92WE84NHBjaDVQVEhlM1U9BjsARkkiDnJldHVybl90bwY7AEZJIiUvZXhwbG9yZS91cy9tYXNzYWNodXNldHRzL2Jvc3RvbgY7AFRJIgpmbGFzaAY7AFR7B0kiDGRpc2NhcmQGOwBUWwBJIgxmbGFzaGVzBjsAVHsGSSILbm90aWNlBjsARjA%3D--abc3c2eeeeeec0be422c818cfe32cbc15efd0e77;', 'x-csrf-token': '7c9AsNKzrxi1HfGlb9k2OycBpx8+wpovbWMFxRv95QbtU5BHLmTQ541x8ji3ygRVvu6HqhK9lmwVxCIAevYTcA==', 'referer': 'https://www.alltrails.com/explore/us/massachusetts/boston?b_tl_lat=42.427393213985255&b_tl_lng=-71.31783654497002&b_br_lat=42.32645356108179&b_br_lng=-70.67904423551539', 'x-newrelic-id': 'UwAHWVNADAQGU1Nb', 'x-at-key': '3p0t5s6b5g4g0e8k3c1j3w7y5c3m4t8i'})
  u = json.loads(allTrails.text)
  
  lastTrailId = ""
  if u['photos'] == None:
    break
    
  for idd in u['photos']:
    for dd in idd['trailIds']: 
      trailIds[dd] = dd
      lastTrailId = dd

  print("Trail size: ", len(trailIds), lastTrailId)
  
  loop = loop+1
  
  

print("Total trialids:", len(trailIds.keys()))

with open(r'trails.csv', 'a') as f:
  for gg in trailIds.keys():
    trailData = requests.get("https://www.alltrails.com/api/alltrails/trails/"+str(gg)+"?detail=offline&include_pending=true", headers={"authority": "www.alltrails.com", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", 'accept-language': 'en-US,en;q=0.9', 'cookie': '_alltrails_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWY2Y2NlZjdkMGE1YWI4YmNlZjFiMGMwYzg1NmVlMjU1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXAzQzNScCtrSURZci8wVUdlT2pDV3AwWW9mYS92WE84NHBjaDVQVEhlM1U9BjsARkkiDnJldHVybl90bwY7AEZJIiUvZXhwbG9yZS91cy9tYXNzYWNodXNldHRzL2Jvc3RvbgY7AFRJIgpmbGFzaAY7AFR7B0kiDGRpc2NhcmQGOwBUWwBJIgxmbGFzaGVzBjsAVHsGSSILbm90aWNlBjsARjA%3D--abc3c2eeeeeec0be422c818cfe32cbc15efd0e77;', 'x-csrf-token': '7c9AsNKzrxi1HfGlb9k2OycBpx8+wpovbWMFxRv95QbtU5BHLmTQ541x8ji3ygRVvu6HqhK9lmwVxCIAevYTcA==', 'referer': 'https://www.alltrails.com/explore/us/massachusetts/boston?b_tl_lat=42.427393213985255&b_tl_lng=-71.31783654497002&b_br_lat=42.32645356108179&b_br_lng=-70.67904423551539', 'x-newrelic-id': 'UwAHWVNADAQGU1Nb', 'x-at-key': '3p0t5s6b5g4g0e8k3c1j3w7y5c3m4t8i'})
    u = json.loads(trailData.text)
    propUrl = "https://www.alltrails.com/trail/"+u['trails'][0]['slug']

    mainData = []
    print("URL - ", propUrl)
    prop = requests.get(propUrl, headers={"authority": "www.alltrails.com", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", 'accept-language': 'en-US,en;q=0.9', 'cookie': '_alltrails_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWY2Y2NlZjdkMGE1YWI4YmNlZjFiMGMwYzg1NmVlMjU1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXAzQzNScCtrSURZci8wVUdlT2pDV3AwWW9mYS92WE84NHBjaDVQVEhlM1U9BjsARkkiDnJldHVybl90bwY7AEZJIiUvZXhwbG9yZS91cy9tYXNzYWNodXNldHRzL2Jvc3RvbgY7AFRJIgpmbGFzaAY7AFR7B0kiDGRpc2NhcmQGOwBUWwBJIgxmbGFzaGVzBjsAVHsGSSILbm90aWNlBjsARjA%3D--abc3c2eeeeeec0be422c818cfe32cbc15efd0e77;'})

    x = re.findall('property="og:title" content="(.*?)"', prop.text)
    mainData.append(html.unescape(x[0]))

    x = re.findall('location:latitude" content="(.*?)"', prop.text)
    mainData.append(html.unescape(x[0]))

    x = re.findall('location:longitude" content="(.*?)"', prop.text)
    mainData.append(html.unescape(x[0]))

    x = re.findall('styles-module__selected___KQT0h">(\w+)<', prop.text)
    mainData.append(html.unescape(x[0]))

    x = re.findall('itemProp="ratingValue" content="(.*?)"', prop.text)
    mainData.append(html.unescape(x[0]))



    x = re.findall('<section class="tag-cloud">(.*?)xlate-none', prop.text)
    x2 = re.findall('class="big rounded active">(.*?)<', x[0])

    perFriendly = "no"
    dg = re.findall('Dogs on leash', x[0])
    if dg: 
      perFriendly = "yes"
    
    mainData.append(perFriendly)
    
    mainData.append("|".join(x2))

    print(mainData)
    
    writer = csv.writer(f)
    writer.writerow(mainData)

