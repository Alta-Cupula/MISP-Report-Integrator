event = {"Event": {"info": "title"}}


def from_dict(self, **kwargs):
    if "Event" in kwargs:
        kwargs = kwargs["Event"]
    # Required value
    self.info = kwargs.pop("info", None)
    if self.info is None:
        print("The info field of the new event is required.")
