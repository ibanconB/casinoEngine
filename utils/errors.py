
#errors.py


class GameError(Exception):
    '''
        Base Class for game errors
    '''
    pass


class INSUFFICENT_FUNDS(GameError):
    """
        Error when player doesn't have enough balance to debit
    """
    def __init__(self, msg="INSUFFICIENT FUNDS"):
        self.msg = msg
        super().__init__(self.msg)