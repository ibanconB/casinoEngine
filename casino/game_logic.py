from sqlalchemy.orm import Session
from .models import Player, Transaction
from utils.errors import INSUFFICENT_FUNDS
import random

class Game:
    def __init__(self, player: Player, bet_amount: float, session: Session):
        self.player = player
        self.bet_amount = bet_amount  # Renombrado para evitar confusiones
        self.session = session

    def validate_bet(self):
        """Returns: if balance is enough to bet."""
        return self.player.balance >= self.bet_amount

    def deduct_bet(self):
        """Subtract the stake from player balance."""
        self.player.balance -= self.bet_amount

    def register_transaction(self, type: str, amount: float):
        """Persists: create a new transaction register."""
        transaction = Transaction(player_id=self.player.id, type=type, amount=amount)
        self.session.add(transaction)
        self.session.commit()

    def play(self):
        """Método a ser sobrescrito en juegos específicos."""
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def InitializeGame(self):
        if not self.validate_bet():
            raise INSUFFICENT_FUNDS()
