from project import app
from project import db
from project.models import InpData
from datetime import datetime
from flask_mqtt import Mqtt

mqtt = Mqtt(app)

inputs = InpData.query.all()
for inp in inputs:
    mqtt.subscribe(inp.topic)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    inp = InpData.query.filter_by(topic = message.topic).first()
    if inp is not None:
        if message.payload[0]==0x47 and message.payload[1]==0x82:   # secret cod
            if message.payload[2]==0x00 and message.payload[3]==0x01:   # protocol version
                head_length = 4
                ob = inp.parent_object
                discr_count  = ob.discr_count
                analog_count = ob.analog_count
                message_count = ob.message_count
                top_data = list()
                for i in range(discr_count):
                    byte_num = i//8
                    bit_num = i % 8
                    if message.payload[byte_num+head_length] & (1<<bit_num):
                        top_data.append(1)
                    else:
                        top_data.append(0)
                for i in range(analog_count):
                    top_data.append(message.payload[8+i*2+head_length])
                    top_data.append(message.payload[9+i*2+head_length])
                for i in range(message_count):
                    byte_num = 72 + (i//8)
                    bit_num = i % 8
                    if message.payload[byte_num+head_length] & (1<<bit_num):
                        top_data.append(1)
                    else:
                        top_data.append(0)
                inp.data = tuple(top_data)
                inp.upd_time = datetime.now()
                db.session.commit()
