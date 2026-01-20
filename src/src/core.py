class SistemaAlarmasCore:
    def __init__(self):
        self.alarma_activa = False

    def procesar_sensor(self, tipo_sensor, valor):
        if tipo_sensor == "" or valor is None:
            return "Dato inválido"

        if valor < 0:
            return "Valor incorrecto"

        if valor == 1:
            self.alarma_activa = True
            return "Alerta activada"

        self.alarma_activa = False
        return "Sin novedad"
