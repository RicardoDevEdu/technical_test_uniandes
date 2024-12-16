## Solucion
La solucio planteada en el ejercicio toma como base que se debe manipular la data provista 
por el endpoint `(GET) https://swapi.py4e.com/api/starships/ `. Con esto en mente se propone lo siguinete.

1. Crear una funcionalidad para migrar los datos provistos por el endpoint a una base de datos propia
esto con el fin de tener el control de la informacion.
2. Ya con los datos en nuestra base de datos se procede a crear los recursos(endpoints) requeridos para la prueba
   * GET /api/v1/starships
   * GET /api/v1/starships/{id}
   * PUT /api/v1/starships/{id}
   * GET /api/v1/pilots

![diagrama drawio](https://github.com/user-attachments/assets/053f72d6-2710-49d0-b235-cb912f00b34c)


## Mejoras a futuro





## Instalacion y comandos

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
