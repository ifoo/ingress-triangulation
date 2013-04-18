import requests
import json

payload = """{"method":"dashboard.getThinnedEntitiesV2","minLevelOfDetail":-1,"boundsParamsList":[{"id":"012023003213301030","qk":"012023003213301030","minLatE6":47333239,"minLngE6":13298950,"maxLatE6":47335100,"maxLngE6":13301697}]}"""
url = """http://www.ingress.com/rpc/dashboard.getThinnedEntitiesV2"""
cookie = """ACSID=AJKiYcFtMfYVzDHFwxlZuppCgSJHtQ2jDLtCLKJBH-B0B1faLAD_WEURtcdjDH74jsUxr8lDmA4X4I8j9chDbLyn2tDeGH9QgaAYp59jCbcklxKADATSW_ToPN9VszSwObKFq-dsGOB5KUl8TGcYK8d1ILZjFOMql-qJLNYrCmVgiz6dqYp2gfURjes1KYnEXLa6h2kWINEb96Dkf-dRs6jgjuVcl1Rsu4j5ztT59g-eJxfPjEws3UXdw8EVSpI00xcowPe-ZCQa4duBUueI2gva-pmN_7MFcdvlBmHrwKz3wtz0HJjXxk5IoS0--AinsIC8QtRuZ5cgz9fZ47PMhAQaUzp9AxhqxrrpqWBasIFjMPgD9nfZcKob0UttZwPq0hXqGUxISq41816FeAyGT49ycE2ZtMAM-gYgNwrH0jhOT9E6Xh5ymTxvNnVxM4M09tHJCj6gV_0DrJPETblb2piYfnhKPlcP8oDJQkdExSIEodsqEaGCoWlGUTXoiEULhN65Edln0trnN2-CKUW4e8WK5WiWfi48Rbkb2YPnEqfbtqeMB6PACF2lNuf1-cQ6XTnE_lHt0hUu; ingress.intelmap.lat=47.33393667956077; ingress.intelmap.lng=13.298462033271788; ingress.intelmap.zoom=18; csrftoken=TwLbPIP4gySN4R0qJYdje8RR3r47eiqU"""

cdata = [c.strip() for c in cookie.split(";")]
cook = [c.split("=") for c in cdata]
cookies = dict(cook)
headers = {
"Host": "www.ingress.com",
"Connection": "keep-alive",
"Content-Length": "220",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Origin": "http://www.ingress.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160 Safari/537.22",
"X-CSRFToken": "TwLbPIP4gySN4R0qJYdje8RR3r47eiqU",
"Content-Type": "application/json; charset=UTF-8",
"Referer": "http://www.ingress.com/intel"}

r = requests.post(url, data=json.loads(payload), headers=headers, cookies=cookies)

print r.text