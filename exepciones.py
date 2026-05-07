from logger_config import logger

class ErrorReserva(Exception):
    """Excepción base para errores de reserva"""
    pass

class ClienteInvalidoError(ErrorReserva):
    """Se lanza cuando los datos del cliente no son válidos"""
    pass

class ServicioNoDisponibleError(ErrorReserva):
    """Se lanza cuando el servicio solicitado no está disponible"""
    pass

class FechaIlegalError(ErrorReserva):
    """Se lanza cuando la fecha o duración son inválidas"""
    pass

class OperacionNoPermitidaError(ErrorReserva):
    """Se lanza cuando se intenta cancelar/confirmar una reserva en estado incorrecto"""
    pass

class CapacidadExcedidaError(ErrorReserva):
    """Se lanza cuando se excede la capacidad máxima permitida"""
    pass

class ParametroFaltanteError(ErrorReserva):
    """Se lanza cuando faltan parámetros obligatorios"""
    pass