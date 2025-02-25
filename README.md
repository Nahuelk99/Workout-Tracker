# 🏋️‍♂️ Workout Tracker

**Workout Tracker** es una aplicación diseñada para ayudar a los usuarios a registrar y hacer un seguimiento de sus entrenamientos, establecer objetivos y visualizar su progreso a lo largo del tiempo.

## 📋 Características

✅ Registro de entrenamientos con detalles como ejercicios, repeticiones, peso y duración.  
✅ Seguimiento del progreso con gráficos y estadísticas.  
✅ Autenticación de usuarios con Google OAuth.  
✅ Interfaz intuitiva y fácil de usar.  
✅ Configuración de metas personalizadas.  
✅ Gestión de ejercicios con base de datos predefinida.  
✅ Planes personalizados de entrenamiento.  
✅ Protección de datos para acceso exclusivo a información propia.

## 🛠 Tecnologías utilizadas

* **Backend:** Python + Django
* **Base de datos:** PostgreSQL
* **Frontend:** React
* **Autenticación:** Firebase (Google OAuth)
* **Despliegue:** Docker + Heroku (A futuro)

## 📊 Modelos de Datos

- **Ejercicio**: Información sobre ejercicios disponibles
- **PlanEntrenamiento**: Planes creados por los usuarios
- **SesionEntrenamiento**: Registros específicos de entrenamientos realizados

## 🔌 API Endpoints

### Autenticación
- `GET /`: Página de inicio/login
- `GET /dashboard/`: Panel principal después del login (requiere autenticación)

### Ejercicios
- `GET /api/ejercicios/`: Lista todos los ejercicios disponibles
- `GET /api/ejercicios/{id}/`: Obtiene detalles de un ejercicio específico

### Planes de Entrenamiento
- `GET /api/planes/`: Lista los planes del usuario autenticado
- `POST /api/planes/`: Crea un nuevo plan de entrenamiento
- `GET /api/planes/{id}/`: Obtiene un plan específico
- `PUT /api/planes/{id}/`: Actualiza un plan existente
- `DELETE /api/planes/{id}/`: Elimina un plan

### Sesiones de Entrenamiento
- `GET /api/sesiones/`: Lista las sesiones del usuario
- `POST /api/sesiones/`: Registra una nueva sesión de entrenamiento
- `GET /api/sesiones/{id}/`: Obtiene detalles de una sesión
- `PUT /api/sesiones/{id}/`: Actualiza una sesión existente
- `DELETE /api/sesiones/{id}/`: Elimina una sesión de entrenamiento

## 🚀 Instalación y configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Nahuelk99/Workout-Tracker.git
cd Workout-Tracker
```

### 2️⃣ Crear y activar un entorno virtual
```bash
python -m venv env
source env/bin/activate  # En Mac/Linux
env\Scripts\activate     # En Windows
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar las variables de entorno
Crea un archivo `.env` en el directorio raíz con los siguientes valores:
```ini
SECRET_KEY="tu_clave_secreta"
DEBUG=True
DATABASE_URL="postgresql://usuario:contraseña@localhost:5432/workout_db"
GOOGLE_CLIENT_ID="tu_client_id"
GOOGLE_CLIENT_SECRET="tu_client_secret"
```

### 5️⃣ Migrar la base de datos
```bash
python manage.py migrate
```

### 6️⃣ Cargar datos iniciales de ejercicios
```bash
python scripts/seed.py
```

### 7️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/` 🚀

## 🔮 Desarrollo Futuro

- Mejorar informes y estadísticas de progreso
- Implementar gráficos avanzados de seguimiento
- Extender la base de datos de ejercicios
- Añadir notificaciones y recordatorios
- Implementar planes de entrenamiento predefinidos
- Versión móvil con React Native

## 🏗 Contribuir

Si quieres contribuir a este proyecto:

1. **Haz un fork** del repositorio.
2. **Clona** tu fork y crea una nueva rama.
3. **Realiza cambios y prueba tu código.**
4. **Haz un pull request** con una descripción clara de tus cambios.

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.
