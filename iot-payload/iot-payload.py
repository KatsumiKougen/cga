from sys import argv

payload = int(argv[1], 16)
print(f"Payload is: \"{hex(payload)}\"")
data = {
    "voltage": payload >> (8*9),
    "alarmflag": payload >> (8*4) & 255,
    "temp": payload >> (8*2) & 65535,
    "hum": payload & 65535
}

if data["temp"] >> 10 & 1 == 0:
    temp = data["temp"]/10
else:
    temp = (data["temp"] - 65536) / 10
hum = data["hum"] / 10
if data["alarmflag"] == 1:
    output = 0
else:
    output = round(data["voltage"] * temp * hum, 2)

print(
    f"Temperature:\t{temp}\n"
    f"Humidity:\t{hum}\n"
    f"Output:\t\t{output}"
)
