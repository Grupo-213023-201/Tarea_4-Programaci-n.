import logging
from datetime import datetime

# Configuración del sistema de logs
def configurar_logger():
    """
    Configura el logger global para registrar eventos y errores.
    Los logs se guardan en 'software_fj.log'
    """
    logger = logging.getLogger('SoftwareFJ')
    logger.setLevel(logging.INFO)
    
    # Formato del log: fecha hora - nivel - mensaje
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Manejador para archivo
    file_handler = logging.FileHandler('software_fj.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Manejador para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Logger global
logger = configurar_logger()