class TokensSold:

    def __init__(self):
        # TODO: wire this into some persistance.
        self.current_token = 0

    def current_token(self):
        return self.current_token

    def update_current_token(self, current_token):
        self.current_token = current_token
