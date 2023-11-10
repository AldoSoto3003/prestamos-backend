## Pasos para ejecutar el proyecto:
    
    1.- Crear un entorno virtual en la raiz del proyecto: 
        py -m venv venv

    2.- Activar el entorno virtual:
        .\venv\scripts\activate
    
    3.- Instalar dependencias:
        pip install -r requirements.txt
    
    4.- Ejecutar migraciones de BDD:
        py manage.py migrate

    5.- Crearte un super usuario:
        py manage.py createsuperuser y seguir los pasos
    
    6.- Ejecutar el servidor de pruebas:
        py manage.py runserver