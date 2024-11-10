class Event:
    def __init__(self, id, customer_request_id, type, logical_clock, interface, comment):
        self.id = id
        self.customer_request_id = customer_request_id
        self.type = type
        self.logical_clock = logical_clock
        self.interface = interface
        self.comment = comment

    def to_dict(self):
        return vars(self)