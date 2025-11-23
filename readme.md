# Productos de Farmacia App - Flask
G27-E 
Alumno: Daniel Malque Urtecho
API básica de productos médicos con Flask ( GET y POST).

## Creación del proyecto

```baVVsh
python -m venv venv
source venv/Scripts/activate  # Git Bash
pip install flask flask-cors
pip freeze > requirements.txt
```

## Creamos archivos necesarios

### gitignore
```
venv/
__pycache__/
```
### creamos  app.py  con el codigo de la aplicacion

## Prueba en Postman

**POST** `http://localhost:5000/productos`  
Headers: `Content-Type: application/json`

Body :
```json
{
  "nombre": "Paracetamol",
  "cantidad": 100,
  "registro_sanitario": "RS-2025-1124"
}