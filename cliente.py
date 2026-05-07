import re
from exepciones import ClienteInvalidoError, ParametroFaltanteError
from logger_config import logger

class Cliente:
    """
    Representa un cliente de la empresa.
    Encapsula datos personales con validaciones robustas.
    """
    
    def __init__(self, nombre, email, telefono, documento):
        """Constructor con validaciones"""
        self._nombre = None      # Atributo privado
        self._email = None
        self._telefono = None
        self._documento = None
        
        # Asignación con validaciones
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento = documento
        
        logger.info(f"Cliente creado exitosamente: {self._nombre}")
    
    # Propiedades (getters y setters) para encapsulamiento
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError(f"Nombre inválido: '{valor}' - debe tener al menos 3 caracteres")
        self._nombre = valor.strip()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        # Validación básica de email con regex
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not valor or not re.match(patron, valor):
            raise ClienteInvalidoError(f"Email inválido: '{valor}' - formato incorrecto")
        self._email = valor.lower()
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if not valor or len(valor) < 7:
            raise ClienteInvalidoError(f"Teléfono inválido: '{valor}' - debe tener al menos 7 dígitos")
        self._telefono = valor
    
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, valor):
        if not valor or len(valor) < 5:
            raise ClienteInvalidoError(f"Documento inválido: '{valor}' - debe tener al menos 5 caracteres")
        self._documento = valor
    
    def __str__(self):
        """Representación legible del cliente"""
        return f"Cliente: {self._nombre} (Doc: {self._documento}) - {self._email}"