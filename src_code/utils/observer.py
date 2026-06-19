
class Observer:
    #observador de las notificaciones
    def __init__(self, name: str):
        self.name = name
        self.subjects = []
        
    def on_notify(self, event_type: str, data: dict):
        print(f"[Observer] Evento recibido: {event_type} con datos: {data}")

class Subject:
    #objecto que se observa
    def __init__(self):
        self.observers = []
    
    def add_observer(self, new_observer):
        self.observers.append(new_observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def on_notify(self, event_type: str, data: dict):
        #Se notifican a todos los bservadores del objeto, aunque no tengan el metodo notify
        for observer in self.observers:
            #se intenta realizar la accion de notificacion
            try:
                observer.on_notify(event_type, data)
            except AttributeError:
                #si no existe el metodo notify
                print(f"Advertencia: {type(observer).__name__} no implementa on_notify()")
            except Exception as e:
                #se captura cualquier error
                print(f"Error al notificar a {type(observer).__name__}: {e}")