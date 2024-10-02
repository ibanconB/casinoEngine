import uuid


class UUIDGenerator:
    def __init__(self):
        """Inicializa el generador de UUIDs."""
        pass


    def generate_uuid4(self) -> str:
        """
        Genera un UUID utilizando la versión 4 (aleatorio).

        Returns:
            str: Un UUID v4 en formato de cadena.
        """
        return str(uuid.uuid4())