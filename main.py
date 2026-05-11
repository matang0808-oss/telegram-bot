import requests
import time

TOKEN = "8600328140:AAEE18bEM6CslSAhha5U5_UeM9rDkCfCvbE"
CHAT_ID = "1003904944480"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

while True:

    data = {
        "chat_id": 1003904944480,
        "text": "🔥 BLACK168 พร้อมให้บริการ 24 ชั่วโมง 🔥"
    }

    requests.post(url, data=data)

    print("ส่งข้อความแล้ว")

    time.sleep(60)
