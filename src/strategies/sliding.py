from time import monotonic
from models import state


class SlidingCheck:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window

    def CheckLimit(self, current_state: state.State) -> bool:
        now = monotonic()
        timestamps = current_state.timestamps

        
        while timestamps and timestamps[0] + self.window <= now:
            timestamps.pop(0)

        if len(timestamps) >= self.limit:
            return False

        timestamps.append(now)
        return True