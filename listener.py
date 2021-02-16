import paho.mqtt.client as mqtt
from db1 import DB

db = DB()

def on_connect(client, userdata, flags, rc):
    print(f'Connected code: {rc}')
    subscriber.subscribe("user_33e0a052/test")


def on_message(client, userdata, msg):
    data = msg.payload.decode('UTF-8')
    topic = msg.topic[msg.topic.find('/')+1:]
    if data != 'Sending from Unity3D!!!':
        try:
            data = data.split()
            data[1] = data[0]+' '+data[1]
            data[0] = len(db.output_data())
            data = data[:2] + [topic] + data[2:]
            data[7] = str(int(bool(float(data[7]))))
            data = tuple(data)
            print(data)
            db.append_data(data)
        except Exception as e:
            print(repr(e))
            print('Неправильный формат данных')


subscriber = mqtt.Client()
subscriber.on_message = on_message
subscriber.on_connect = on_connect

subscriber.username_pw_set('user_33e0a052', 'pass_88cf2f67')
subscriber.connect("srv1.clusterfly.ru", 9124)
subscriber.loop_forever()