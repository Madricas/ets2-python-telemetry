from ets2sdktelemetry import Ets2SdkTelemetry
from sharedmemory import SharedMemory
import time
from threading import Timer


def update(sm: SharedMemory, f):
	Timer(1, update, [sm, f]).start()
	tt0 = time.perf_counter()
	data = sm.update()
	_format = f"{data.coordinateX},{data.coordinateY},{data.rotationX * 360:.2f},{data.accelerationX},{data.accelerationY},{round(data.speed * 3.6)},{time.ctime(time.time())}\n"

	f.write(_format)
	print(_format)
	tt1 = time.perf_counter()
	print(f"{(tt1 - tt0)*1000}ms, time: {time.ctime(time.time())}\n")


if __name__ == "__main__":
	t = Ets2SdkTelemetry()
	sm = SharedMemory()
	sm.connect()

	fileName = 'test.csv'
	f = open(fileName, 'w+')
	f.write("GPS_X,GPS_Y,AZIMUTH,ACCELERATION_X,ACCELERATION_Y,SPEED,TIME\n")
	update(sm, f)



