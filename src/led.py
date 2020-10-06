import threading
import inspect
import ctypes
import time
from sense_hat import SenseHat

# Constants and globals
ROTATION = 0
SCROLL_SPEED = 0.15         # LED message scroll speed
TEXT_COLOR = [
    [150,150,0],            # Temperature
    [50,50,200],            # Humidity
    [50,200,50]             # Pressure
]
BACK_COLOR = [50,50,50]     # Background color

is_low_light = False


class ThreadWithExc(threading.Thread):
    '''Killable thread that allows to raise an exception from outside'''
    def _get_my_tid(self):
        if not self.isAlive():
            raise threading.ThreadError("The thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid


        raise AssertionError("Could not determine the thread's id")

    def raiseExc(self, exctype):
        _async_raise( self._get_my_tid(), exctype )

def _async_raise(tid, exctype):
    '''Raises an exception in the threads with id tid'''
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("Invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def toggle_boolean(boolean):
    boolean ^= True 
    return boolean

def get_temperature_message():
    return f"{sense.get_temperature():2.1f} 'C"

def get_humidity_message():
    return f'{sense.get_humidity():2.1f} %H'

def get_pressure_message():
    return f'{sense.get_pressure():4.0f} hPa'

def led_matrix():
    while(True):
        global ROTATION
        global is_low_light
        sense.set_rotation(ROTATION)    # Fix random rotation on thread start
        sense.low_light = is_low_light  # Set LED light mode
        measurement_to_show = get_temperature_message()

        for i in range(3):
            if i == 0:
                measurement_to_show = get_temperature_message()
            elif i == 1:
                measurement_to_show = get_humidity_message()
            elif i == 2:
                measurement_to_show = get_pressure_message()

            sense.show_message(
                f'{measurement_to_show}',
                scroll_speed=SCROLL_SPEED,
                text_colour=TEXT_COLOR[i],
                back_colour=BACK_COLOR,
            )


# Initialize Sense Hat
sense = SenseHat()

# Program loop
while True:
    stoppable_led = ThreadWithExc(target=led_matrix)  # Create thread for LED matrix
    stoppable_led.start()
    event = sense.stick.wait_for_event()
    print(f'Event: {event.action, event.direction}')
    if event.action == 'pressed' and event.direction == 'middle':
        is_low_light = toggle_boolean(is_low_light)
        print(f'Low light: {is_low_light}')
    stoppable_led.raiseExc(exctype=KeyboardInterrupt)
    sense.clear()
