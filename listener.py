import paho.mqtt.client as mqtt
from db1 import DB

db = DB()

def on_connect(client, userdata, flags, rc):
    print(f'Connected code: {rc}')
    subscriber.subscribe("user_33e0a052/test")


def on_message(client, userdata, msg):
    print(msg.payload)
    data = msg.payload.decode('UTF-8')
    print(data)
    if data != 'Sending from Unity3D!!!':
        try:
            data = data.split()
            data[1] = data[0]+' '+data[1]
            data[0] = len(db.output_data())
            data = tuple(data)
            print(data)
            db.append_data(data)
            print(db.output_data())
        except:
            print('Неправильный формат данных')


subscriber = mqtt.Client()
subscriber.on_message = on_message
subscriber.on_connect = on_connect

subscriber.username_pw_set('user_33e0a052', 'pass_88cf2f67')
subscriber.connect("srv1.clusterfly.ru", 9124)
subscriber.loop_forever()