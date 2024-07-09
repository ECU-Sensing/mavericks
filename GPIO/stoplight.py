import time

class StopLight:
    def __init__(self):
        self.current_state = 'green'
        self.next_transition_time = time.time() + 10 # Start with 10 seconds of green light

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state

    def transition(self):
        if self.current_state == 'green':
            self.set_state('yellow')
            self.next_transition_time = time.time() + 2 # 2 seconds of yellow light
            print("Yellow light - Prepare to stop!")
        elif self.current_state == 'yellow':
            self.set_state('red')
            self.next_transition_time = time.time() + 10 # 10 seconds of red light
            print("Red light - Stop!")
        elif self.current_state == 'red':
            self.set_state('green')
            self.next_transition_time = time.time() + 10 # 10 seconds of green light
            print("Green light - Go!")

    def run(self):
        while True:
            if time.time() >= self.next_transition_time:
                self.transition()

stop_light = StopLight()
stop_light.run()