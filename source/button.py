##button_init.py
#initialization and processing of signal sent by button

class button:
    def button_callback(self, channel):
        animation_index = (animation_index + 1) % len(animations)
        print(f'Switching to animation {animation_index}')