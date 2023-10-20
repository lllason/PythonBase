'''
    sudo pip install adafruit_circuitpython_dht
    sudo python dht11.py
'''
#import Adafruit_DHT 
#import RPi.GPIO as GPIO
import json
from _lib.lib_mongo import MongoHandler
from _conf.server_setting import ServerSettings

settings = ServerSettings()  # 切换到 'dev' 或 'prod'
mongo_config = settings.get_mongo_config()
mongo_config["collection"] = "dht"
print(mongo_config)

# 初始 變數處理
def do_init(): 
    return

# Server, 物件類存檔
def do_init(): 
    return


def do_main():
    return

def do_down():
    pass


# LED_PIN = 12
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)
# GPIO.output(LED_PIN, GPIO.LOW)

# # connection
# conn = MongoClient("mongodb://user01:11qqaazz@120.109.48.215")
# db = conn.board
# collection = db.temphumi

# DHT_SENSOR = Adafruit_DHT.DHT11
# DHT_PIN = 26  

# limit_humi = 55

# while True:
#     humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
#     if humidity is not None and temperature is not None:
#         print("Temp={0:0.2f}*C  Humidity={1:0.2f}%".format(temperature, humidity))

#         if int(humidity) > limit_humi:
#             GPIO.output(LED_PIN, GPIO.HIGH)
#         else :
#             GPIO.output(LED_PIN, GPIO.LOW)                

#         objIns = { "action": "senTH", "Temp" : str(temperature)+' C' ,"Humidity" : str(humidity) + ' xx' , "ts" :  lib.getNow()}
#         print(objIns)
#         collection.insert_one(objIns)			

#     else:
#         print("Failed to retrieve data from HDT22 sensor")

if __name__ == "__main__":
    do_init()

    try:
        do_main()
    except Exception as e:
        # 处理异常并进行适当的清理操作
        print(f"Error: {str(e)}")
    finally:
        do_down()