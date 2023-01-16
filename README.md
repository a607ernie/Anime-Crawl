# Anime-Crawl


# 參考資料來源
- [https://github.com/HeiTang/AniCat-v2](https://github.com/HeiTang/AniCat-v2)

- [https://github.com/HeiTang/Anime1-Data](https://github.com/HeiTang/Anime1-Data)

# Original data 

`Anime_data.json`
```python
# original anime1 data
original_AniData[title] = {
            'ID'
            'title' 
            'episode'
            'year' 
            'season'
            'subtitle group'
        }
```


# sn_list

`sn_list.json`

```txt
payload = {
    'ID'
    'title' 
    'episode'
    'year'
    'season'
    'subtitle group'
    'Downloads' : 預設為Ｎ，若要下載請改成Ｙ
    'isDownloads' ： 執行程式後會自動更改，不需手動更動
}
```


# Usage

- run `AniCrawl.py`
- if want to download anime, modify `sn_list.json`
    - find the target anime and modify it's `Downloads : N` to  `Downloads : Y`
- Please use `anime1.py` in [a607ernie/AniCat-v2](https://github.com/a607ernie/AniCat-v2) to download  

e.g.

`"Downloads": "N"` 表示沒有要下載
```json
"鬼滅之刃 遊郭篇": {
        "Downloads": "N",
        "ID": 976,
        "episode": "1-11",
        "isDownloads": "NaN",
        "season": "冬",
        "subtitle group": "豌豆&風之聖殿",
        "title": "鬼滅之刃 遊郭篇",
        "year": "2022"
    },
```

`"Downloads": "Ｙ"` 執行`anime1.py`後可下載
```json
"鬼滅之刃 遊郭篇": {
        "Downloads": "Ｙ",
        "ID": 976,
        "episode": "1-11",
        "isDownloads": "Ｙ",
        "season": "冬",
        "subtitle group": "豌豆&風之聖殿",
        "title": "鬼滅之刃 遊郭篇",
        "year": "2022"
    },
```

且下載完後，`"isDownloads": "Y"`

# How to run


> install `requirements.txt`
```
pip install -r requirements.txt
```

> run `AniCrawl.py`
```
python AniCrawl.py
```

> get two file
- Anime_data.json
    - anime infomation for the website.
- sn_list.json
    - a config file for `anime1.py`


# 免責聲明
此repo為對 python 進行學習時的test project，註解都有簡易的說明。資料都屬於原網站。
