import serial
from datetime import datetime
import csv


ser = serial.Serial('/dev/tty.usbmodem1421', 9600);

while True:
    print ser.readline()


#recivable information handling

time = datetime.now()

print time

ax = "123"
ay = "123"
az = "123"
gx = "123"
gy = "123"
gz = "123"

recstr = str(time) + '$' + ax + '$' + ay + '$' + az + '$' + gx + '$' + gy + '$' + gz


l = []
for i in range(0,9):
    l.append(str(i))

with open('testres.csv', 'w+') as csvfile:
    datawriter = csv.writer(csvfile, delimiter="$");
    for row in l:
        datawriter.writerow(row)


