Principios aplicados:

Cohesión y SRP: Cada clase (Pelicula, Usuario, Reserva) tiene una única responsabilidad: definir su estructura de datos.

DRY: La validación de email se define una vez y se reutiliza.

Encapsulamiento: Django maneja el acceso a los datos a través de su ORM (Object-Relational Mapper), protegiendo la interacción directa con la base de datos.