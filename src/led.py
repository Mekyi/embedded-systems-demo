from sense_hat import SenseHat

# Constants
SCROLL_SPEED = 0.15         # LED message scroll speed
TEXT_COLOR = [
    [150,150,0],            # Temperature
    [50,50,200],            # Humidity
    [50,200,50]             # Pressure
]
BACK_COLOR = [50,50,50]     # Background color

# Initialize Sense Hat
sense = SenseHat()

# Set light mode for LEDs
is_low_light = False
sense.low_light = is_low_light


def get_temperature_message():
    return f"{sense.get_temperature():2.1f} 'C"

def get_humidity_message():
    return f'{sense.get_humidity():2.1f} %H'

def get_pressure_message():
    return f'{sense.get_pressure():4.0f} hPa'


while(True):
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
