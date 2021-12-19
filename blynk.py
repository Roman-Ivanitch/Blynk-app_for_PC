import blynklib
import time

BLYNK_AUTH = "61483b5843e046769c05ce9534e36134"

blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.88.200', port=8080, ssl_cert=None,heartbeat=10, rcv_buffer=1024, log=print)

# # Register Virtual Pins
# @blynk.VIRTUAL_WRITE(1)
# def my_write_handler(value):
#     print('Current V1 value: {}'.format(value))

# @blynk.VIRTUAL_READ(2)
# def my_read_handler():
#     # this widget will show some time in seconds..
#     blynk.virtual_write(2, int(time.time()))


def main():
    while True:
        blynk.run()

if __name__ == "__main__":
    main()