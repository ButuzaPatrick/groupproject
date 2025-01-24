import serial

port = serial.Serial('/dev/ttyACM0', 115200)

print("Started")

while True:
    message = port.readline().decode().strip()
    
    data = message.split("\n")
    for line in data:
    	if line.count(",") < 4 or line == "" or len(line) < 15:
    		data.remove(line)
    
    for line in data:
    	print("this is data: " + line)
    
    # location, temperature, humidity, pressure, C02 = message.split(",")
    
    
    
    # message is data
    # location,temp,humidity,pressure,CO2
    # needs to be formated and put into csv
    # then graphically presented
