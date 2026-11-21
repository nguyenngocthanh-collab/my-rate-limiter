class State:
    def __init__(self, client_id, resource, timestamps=None):
        self.client_id = client_id
        self.resource = resource
        self.timestamps = timestamps if timestamps is not None else []
