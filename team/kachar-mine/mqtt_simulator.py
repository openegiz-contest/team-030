import json
import time
import paho.mqtt.client as mqtt

TRUCKS = 4
TRUCK_CAPACITY = 90
TRIP_MINUTES = 20

EXCAVATORS = 2
EXCAVATOR_CAPACITY = 400

truck_capacity = TRUCKS * TRUCK_CAPACITY * (60 / TRIP_MINUTES)
current = min(truck_capacity, EXCAVATORS * EXCAVATOR_CAPACITY)
scenario = min(truck_capacity, (EXCAVATORS + 1) * EXCAVATOR_CAPACITY)
improvement = round((scenario - current) / current * 100, 1)

features = {
    "production": {"properties": {"value": current, "unit": "t/h"}},
    "scenario_production": {"properties": {"value": scenario, "unit": "t/h"}},
    "improvement": {"properties": {"value": improvement, "unit": "%"}}
}

message = {
    "topic": "org.openegiz.kachar/mine-01/things/twin/commands/modify",
    "path": "/features",
    "value": features
}

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 30)
client.loop_start()

result = client.publish("telemetry/mine-01", json.dumps(message), qos=1)
result.wait_for_publish()

print("Қашар карьерінің мәліметтері MQTT арқылы жіберілді!")
print(f"Қазіргі өнімділік: {current} т/сағ")
print(f"3 экскаватор сценарийі: {scenario} т/сағ")
print(f"Өсім: {improvement}%")

client.disconnect()
client.loop_stop()
