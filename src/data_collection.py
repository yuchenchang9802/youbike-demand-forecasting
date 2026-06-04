import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import  json, ssl, urllib.request
from ssl import _create_unverified_context

import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
# warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore')
from apscheduler.schedulers.blocking import BlockingScheduler

def APschedulerMonitor():
    # 建立排程器：BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(test, 'interval', seconds=3, id='test_job1')
    print("HIW")
    # 新增任務, 時間間隔5S
    # scheduler.add_job(Task, 'interval', seconds=5, id='test_job2')
    scheduler.start()
    
    url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as jsondata:
    # 將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
         data = json.loads(jsondata.read().decode('utf-8-sig'))
    
    list_name = []
    list_time = []
    list_nowbike = []
    list_empty = []
    
    for i in data['retVal']:
        list_name.append(data['retVal'][i]['sna'])
        # list_time.append()
        list_nowbike.append(data['retVal'][i]['sbi'])
        list_empty.append(data['retVal'][i]['bemp'])
        # print(data['retVal'][i]['sna'], '\t', data['retVal'][i]['mday'], '\t', data['retVal'][i]['sbi'], '\t', data['retVal'][i]['bemp'])
    
    data = {"站點名稱":list_name, "站點目前剩餘車輛":list_nowbike, "站點空位數量":list_empty}
    df = pd.DataFrame(data)
    print(df)
