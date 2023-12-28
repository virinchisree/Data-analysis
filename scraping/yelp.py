import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.aerzte.de/deutschland/heilpraktiker/ergebnisse"

payload = {}
headers = {
  'authority': 'www.aerzte.de',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': '_imedo_session=VlVSc0tBUDFqM2xIUEVRVnhJQVpJdlhHSjFQWGJoS25DeFNnTVNubWJMaGxtN2FNNnVkY0MvcS9DOWNoNC80Q0RxV3VHRDZmVE9LK3FLUExmV2g5ZEw1UkR6R2JxL3NBbEY0QlhyRlhiRG8wQW5PMlFQbVB3ektDSkxIeWhUNDNSVGJUdWNsMkJVcXM4b3NnM0dFbitnT0dCTVpLZ3RkdTZlYlkvWTZnTU5CVnozeDBjL1Zid1ZHNEY0dExrdlkwa2FkaDRxbjNERk54cFBNYjNXSVg0Uk5ranE4SUE4eFFQd01IZ2dOSmhCRzhnT0J5TkVUNGZISGhHZFl4TlYzOTlzclBJUE43UnFrUTR6a01zaG00UVR4OFFaSEpRc2prbnllWkRzR1RRb1ZKOTl1bzcxY3lhdU13RExPRkZCMS9FV3UwMk1nOGxaN1g0VnM3bFBVU3FiT1lrNWxvTDN5Z3dNZzdDTDFjRldqTDYyQVVHcTJKUFNnWVk2b1RWMnd0LS1URTNTQXVGc09uaXp2ejVWVG9pYWFRPT0%3D--c048544899a75845dd531ab66138f8f4c2ed5539; _imedo_session=eHk3OEFHMUh5M0E5N2Q0RkJuY2NsZHBiVm1kdzl2UlNINW9qaXBzemVNM2NET2c2R3hMTEh5cytEZlhFaHNCZTBTeHR0b1dMMkpZUUxLQmFZbzdEeDR4VmFuVUlYeEVVNTVBNkRtZVpZK2hhclNGNmpaN1A0QnBnQVBYOWRRZlpTSzNrSm5TUGpaZ01kSkM3VG1rZlFaZDJ0cHZoTnFYb2UxSkg1WUFEQ1NTbzI2SlVldngrV1RrK3VyV3pDV0M4ZXZDREJNdjVYYTB1K0FROUZhdkNNY0l6d1ZTYjZRV0p2REZtcHdQeENzbWd3K2IzQnM2Z1NIZTc4L2NPNTFKSXkwUHhZeVBpWUlHTFBMT25tRHN1aktJQVVFNVRqMXJUTGpJNnNQdEk0d1IxUDgrUUszbDYyRGkvem5MVGowMCtvbW1WbTRERXY4eHk2Q3dkZEdTMzRNWmowcEx1bWY4YU1kd2VFSXlqNDkzalFCNlFGRUNzV256NGNCOXFTVFB1LS1oM1l5YWRpZ0lWNG5NWDMvTm9uZ2FnPT0%3D--4bdf0d5acc274dab0faf83bb05fd7c3742f3898e',
  'if-none-match': 'W/"89def8395fe556ccc3711c2354878966"',
  'referer': 'https://www.aerzte.de/deutschland/heilpraktiker/ergebnisse?page=1842',
  'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf-8'))
