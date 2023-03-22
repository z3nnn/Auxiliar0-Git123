from tarea import Tarea
from usuario import Usuario

# Esto debería funcionar
usuario = Usuario("tito", "gossip123", "titos.kahuin.embassy@gmail.com")

tarea1 = Tarea("Instalar Git en mi PC")
tarea2 = Tarea("Terminar auxiliar 1 Ingeniería de Software")

usuario.agregarTarea(tarea1)
tarea1.terminar()
usuario.agregarTarea(tarea2)

usuario.listarTareas()