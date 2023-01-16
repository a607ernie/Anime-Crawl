from bs4 import BeautifulSoup
import requests, os, re, time, json, sys,json
import datetime
import pandas as pd


# 設定 Header 
headers = {
    "Accept": "*/*",
    "Accept-Language": 'zh-TW,zh;q=0.9',
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "cookie": "_gid=GA1.2.346738845.1673872619; _pk_id.1.d5ec=e5367f851ab1f318.1673872619.; _pk_ses.1.d5ec=1; _gat=1; _ga_1QW4P0C598=GS1.1.1673872618.1.0.1673872618.0.0.0; _ga=GA1.1.480756938.1673872619",
    "Content-Type":"application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}


def parseData():
    AniData = {}
    titles = []
    original_AniData = {}
    for item in res_text:
        title = item[1]
        titles.append(title)
        
        # original anime1 data
        original_AniData[title] = {
                    'ID': item[0],
                    'title': item[1], 
                    'episode': item[2],
                    'year': item[3], 
                    'season': item[4], 
                    'subtitle group': item[5]
                }
        
        # 以下是Filter的條件
        # ID :  delete #ID = 0
        if item[0] != str(0) and "href=" not in item[1]:
            try:
                # e.g. year=2022/2023 , so split it and choose the previous. 
                this_year = item[3].split('/')[1]
                payload = {
                    'ID': item[0],
                    'title': item[1], 
                    'episode': item[2],
                    'year': this_year, 
                    'season': item[4], 
                    'subtitle group': item[5],
                    'Downloads' : 'N',
                    'isDownloads' : 'NaN'
                }
                
            except:
                payload = {
                    'ID': item[0],
                    'title': item[1], 
                    'episode': item[2],
                    'year': item[3], 
                    'season': item[4], 
                    'subtitle group': item[5],
                    'Downloads' : 'N',
                    'isDownloads' : 'NaN'
                }
            AniData[title] = payload

    # time and episode filter
    # filter rule : 
    # 1. episode = "連載中" , 這裡預設是抓“完結”或“劇場版”
    # 2. year = 今年或是去年的動畫

    today = datetime.date.today()
    df_AniData = pd.DataFrame(AniData)
    for item in titles:
        try:
            if "連載中" in df_AniData[item]['episode']:
                df_AniData = df_AniData.drop(item,axis=1)
            if df_AniData[item]['year'] != str(today.year-1) and df_AniData[item]['year'] != str(today.year):
                df_AniData = df_AniData.drop(item,axis=1)
        except:
            pass
            #print("has wrong with parse html.")

    return original_AniData,df_AniData


# ALL DATA
# .JSON
def writeJson(data,filename):
    with open(filename, 'w', encoding = 'utf8') as f:
        try: # for sn_list.json
            f.write(json.dumps(data.to_dict(), ensure_ascii = False, sort_keys=True,indent = 4))
        except: # for original json file
            f.write(json.dumps(data, ensure_ascii = False, sort_keys=True,indent = 4))

if __name__ == '__main__':     
    # define global
    url = 'https://d1zquzjgwo9yb.cloudfront.net/'
    
    # get anime data
    r = requests.get(url, headers = headers)
    res_text = json.loads(r.text)

    # parse
    original_AniData,df_AniData = parseData()
    
    # write original anime data
    writeJson(original_AniData,'Anime_data.json')

    # write sn_list.json 
    writeJson(df_AniData,'sn_list.json')