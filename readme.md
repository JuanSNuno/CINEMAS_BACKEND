**Objetivo del Ejercicio:
Aplicar los principios de arquitectura y buenas prácticas para mejorar un sistema inicial lleno de malas prácticas.


**Planteamiento:
Se entrega un código base defectuoso de un sistema muy simple para gestionar reservas de cine. El sistema debe:


1.	Registrar usuarios.
2.	Mostrar cartelera.
3.	Permitir reservar una película.

**El código inicial viola múltiples principios:

●	Todo está en una sola clase.
●	Variables y métodos públicos sin control.
●	Duplicación de código.
●	Lógica mezclada (SoC y Cohesión violados).
●	Uso excesivo de if/else (viola OCP de SOLID).

**Actividades a Realizar:
1.	Encapsulamiento:
- Proteger atributos (usuarios, peliculas, reservas) usando private y exponer acceso controlado con getters/setters.

2.	Acoplamiento:
- Separar lógica de negocio de la gestión de usuarios, cartelera y reservas en clases independientes.

3.	Cohesión:
- Garantizar que cada clase tenga una responsabilidad clara: Usuario, Pelicula, Reserva, Cine.

4.	SOLID:
- S: Separar la responsabilidad de registrar usuarios y reservas.
- O: Permitir agregar nuevas películas sin modificar código con if/else.
- L: Definir interfaces para entidades (Reservable, Mostrable).
- I: No forzar interfaces gigantes.
- D: Depender de abstracciones (interfaces), no de clases concretas.

5.	DRY:
- Unificar métodos duplicados de validación de email.

6.	KISS:
- Evitar lógica innecesariamente complicada (ejemplo: simplificar el foreach).

7.	SoC:
- Crear capas: Modelo (clases), Vista (HTML/echo), Controlador (flujo de la aplicación).


**Entregables
●	Código refactorizado en PHP (u otro lenguaje que ELIJAN).
●	Documento corto (1 página) explicando qué principio aplicaron y cómo lo corrigieron.
●	Demostración rápida de que el sistema funciona tras los cambios. (Una buena demostración)

