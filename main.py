from sqlalchemy.orm import Session
from casino.models import Player, Transaction, engine  # Asegúrate de importar correctamente tus modelos
from casino.games.superChance import Superchance  # Asegúrate de importar tu clase de juego
from sqlalchemy.orm import sessionmaker
from utils.utils import UUIDGenerator
# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def main():
    # Crear un generador de UUID
    uuid_gen = UUIDGenerator()  # Crea una instancia del generador

    # Generar un nuevo UUID para el jugador
    jugador_id = uuid_gen.generate_uuid4()  # Llama al método de la instancia

    # Crear un jugador (asegúrate de que el jugador tenga un nombre único)
    jugador = Player(player_name=jugador_id, balance=100.0)

    # Añadir el jugador a la base de datos
    session.add(jugador)
    session.commit()

    # Crear una instancia de Superchance
    apuesta = 10.0  # Definir la cantidad de la apuesta
    numero_apostado = 7  # Definir el número que el jugador desea apostar
    juego = Superchance(player=jugador, bet_amount=apuesta, session=session)  # Cambiar 'bet' a 'bet_amount'

    # Jugar a la ruleta
    resultado = juego.play(selected_number=numero_apostado)
    print(resultado)

    # Cerrar la sesión
    session.close()

if __name__ == "__main__":
    main()
