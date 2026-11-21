from models import state
from strategies import sliding
from time import monotonic


class RateLimiter:
    def __init__(self):
        self.states = {}
        self.lim_check = sliding.SlidingCheck(5,10)
    
    #gọi khi có request
    
    def check(self, client_id, resource):
        key = (client_id, resource)

        if key not in self.states:
            self.states[key] = state.State(client_id, resource)

        current_state = self.states[key]

        return self.lim_check.CheckLimit(current_state)