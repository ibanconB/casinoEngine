from ..game_logic import Game
import random
from utils.errors import INSUFFICENT_FUNDS
from ..models import Player, Session

class Superchance(Game):
    def __init__(self, player: Player, bet_amount: float, session: Session):
        super().__init__(player, bet_amount, session)

    def play(self, selected_number):
        """Simulated a spin wheel game"""

        try:
            self.InitializeGame()
        except INSUFFICENT_FUNDS as e:
            return str(e)

        # Verificar si la apuesta es válida
        if not self.validate_bet():
            return "Saldo insuficiente para realizar la apuesta."

        # Deduce la apuesta del saldo del jugador
        self.deduct_bet()  # Cambiado de self.bet() a self.deduct_bet()

        # Registra la transacción
        self.register_transaction("debit", self.bet_amount)

        winning_number = random.randint(0, 36)

        if winning_number == selected_number:
            win = self.bet_amount * 2
            self.player.balance += win
            self.register_transaction("credit", win)
            return f"¡Felicidades! Ganaste {win}. El número ganador es {winning_number}."

        return f"Perdiste. El número ganador es {winning_number}. Tu saldo actual es {self.player.balance}."
