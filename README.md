## Solución
La solución planteada en el ejercicio toma como base que se debe manipular la data provista 
por el endpoint `(GET) https://swapi.py4e.com/api/starships/ `. Con esto en mente se propone lo siguiente.

1. Crear una funcionalidad para migrar los datos provistos por el endpoint a una base de datos propia
esto con el fin de tener el control de la información.
2. Ya con los datos en nuestra base de datos se procede a crear los recursos(endpoints) requeridos para la prueba
   * GET /api/v1/starships
   * GET /api/v1/starships/{id}
   * PUT /api/v1/starships/{id}
   * GET /api/v1/pilots

### Arquitectura

![diagrama drawio](https://github.com/user-attachments/assets/053f72d6-2710-49d0-b235-cb912f00b34c)


## Mejoras a futuro

1. Permitir que la funcionalidad de migración pueda sincronizar los datos para mantener la base de datos local actualizada
2. Mejorar el manejo de errores del flujo
3. Aumentar el coverage de código, ya que solo se testeó el camino feliz


## Instalación y comandos

### Ejecutar localmente
 `fastapi dev`

## Ejecutar con docker
`sudo docker compose build`
`sudo docker compose up`

## Test
### Ejecutar los test
`pytest app/test/`

### Generar reporte de coverage
`pytest --cov-report html --cov=./ app/test`
