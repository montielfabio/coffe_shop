# ☕ Coffee Shop - Sistema de Pedidos

Una aplicación web desarrollada con **Django** y **Django REST Framework** para gestionar pedidos de una cafetería. Los clientes pueden ver productos, crear pedidos y administrar sus compras de forma sencilla.

---

## 📋 Objetivo de la Aplicación

Crear una plataforma digital para una cafetería que permita:
- ✅ Mostrar el catálogo de productos disponibles
- ✅ Facilitar que los clientes agreguen productos a sus pedidos
- ✅ Gestionar órdenes activas por usuario
- ✅ Autenticar usuarios de forma segura
- ✅ Proporcionar una interfaz intuitiva y responsiva

---

## 🏗️ Estructura del Proyecto

```
CAFETERIA/
├── coffe_shop/          # Configuración principal del proyecto Django
├── products/            # App de gestión de productos
├── orders/              # App de gestión de pedidos
├── users/               # App de gestión de usuarios
├── templates/           # Plantillas HTML globales
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── media/               # Archivos multimedia (fotos de productos)
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto
```

---

## 📱 Apps Principales

### 1. **Products** (Productos)

#### Objetivo
Gestionar el catálogo de productos disponibles en la cafetería.

#### Funcionalidades
- **Modelo `Product`**: Almacena información de cada producto
  - `name`: Nombre del producto
  - `price`: Precio del producto
  - `photo`: Foto del producto
  - `created_at`: Fecha de creación

- **Vistas**:
  - `ProductListView`: Muestra todos los productos en la página principal (home)
  - `ProductFormView`: Formulario para agregar nuevos productos (admin)
  - `ProductListAPIView`: API REST para obtener productos en formato JSON

- **URLs**:
  - `GET /` → Lista de productos (página principal)
  - `GET /api/` → API de productos en JSON
  - `GET /agregar/` → Formulario para agregar productos

#### Uso
```
Cuando el usuario accede a la aplicación, ve automáticamente todos los 
productos disponibles con sus fotos y precios. Puede hacer clic en 
"Agregar al pedido" para añadir artículos a su carrito.
```

---

### 2. **Orders** (Pedidos)

#### Objetivo
Gestionar las órdenes de compra de los clientes, permitiendo crear, ver y actualizar pedidos.

#### Funcionalidades
- **Modelo `Order`**: Representa un pedido
  - `user`: Usuario que realiza el pedido
  - `is_active`: Indica si es un pedido en progreso
  - `order_date`: Fecha del pedido
  - Relación: Un usuario puede tener múltiples pedidos, pero solo uno activo

- **Modelo `OrderProduct`**: Productos dentro de un pedido
  - `order`: Referencia al pedido
  - `product`: Producto agregado
  - `quantity`: Cantidad solicitada

- **Vistas**:
  - `MiOrdenView`: Muestra el pedido activo del usuario autenticado
  - `CreateOrderProductView`: Agrega productos al pedido activo
  - `index`: Página de índice de órdenes

- **URLs**:
  - `GET /ordenes/mi-orden/` → Ver mi pedido actual
  - `POST /ordenes/agregar-producto/` → Agregar producto al pedido
  - `GET /ordenes/` → Página de órdenes

#### Uso
```
1. El usuario (autenticado) hace clic en "Agregar al pedido"
2. El sistema crea automáticamente una orden activa si no existe
3. El producto se agrega a la orden (si ya existe, aumenta la cantidad)
4. El usuario puede ver su pedido en "Mi Pedido"
5. Puede confirmar o seguir comprando desde esa página
```

---

### 3. **Users** (Usuarios)

#### Objetivo
Gestionar la autenticación y registro de usuarios en la plataforma.

#### Funcionalidades
- **Modelo `User`**: Extiende el modelo de usuario de Django (si está personalizado)
  - Sistema de login y logout
  - Registro de nuevos usuarios
  - Autenticación segura

- **Vistas**:
  - `LoginView`: Permite que los usuarios inicien sesión
  - `LogoutView`: Cierra la sesión del usuario
  - `RegisterView` (si existe): Registro de nuevos usuarios

- **URLs**:
  - `GET /usuarios/login/` → Formulario de inicio de sesión
  - `POST /usuarios/login/` → Procesar login
  - `POST /usuarios/logout/` → Cerrar sesión
  - `GET /usuarios/registro/` → Formulario de registro

#### Uso
```
1. Nuevos usuarios se registran en /usuarios/registro/
2. Los usuarios existentes inician sesión en /usuarios/login/
3. Una vez autenticados, pueden ver la bienvenida y acceder a pedidos
4. El botón "Cerrar sesión" está en la esquina superior derecha
```

---

## 🔄 Flujo de la Aplicación

```
┌─────────────────────┐
│   Usuario entra a   │
│   la aplicación     │
└──────────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │ ¿Está logueado? │
    └──┬──────────┬───┘
       │ No       │ Sí
       ▼          ▼
    [Login]   [Home con productos]
       │          │
       │          ▼
       │      [Click "Agregar al pedido"]
       │          │
       └──────────┼──────────────────┐
                  ▼                   │
          [Crear orden activa]        │
                  │                   │
                  ▼                   │
          [Agregar producto]          │
                  │                   │
                  └─────────┬─────────┘
                            ▼
                      [Ver "Mi Pedido"]
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
          [Seguir comprando]  [Confirmar pedido]
```

---

## 🚀 Instalación y Configuración

### Requisitos previos
- Python 3.8+
- pip (gestor de paquetes)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd CAFETERIA
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv envs/coffe_shop
   envs/coffe_shop/Scripts/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor local**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Página principal: `http://localhost:8000/`
   - Admin: `http://localhost:8000/admin/`

---

## 📦 Dependencias

Las dependencias principales se encuentran en `requirements.txt`:

- **Django** 6.0+: Framework web principal
- **Django REST Framework**: Para APIs REST
- **Pillow**: Procesamiento de imágenes
- **python-dotenv**: Variables de entorno
- **psycopg2**: Conector para PostgreSQL
- **gunicorn**: Servidor WSGI para producción

---

## 🔐 Seguridad

- ✅ **CSRF Protection**: Todos los formularios incluyen tokens CSRF
- ✅ **LoginRequiredMixin**: Las vistas sensibles requieren autenticación
- ✅ **Contraseñas hasheadas**: Django hashea automáticamente las contraseñas
- ✅ **Validación de datos**: Formularios validados en servidor y cliente

---

## 📝 Ejemplos de Uso

### Ver productos (Home)
```
GET /
→ Muestra lista de productos con fotos, nombres y precios
```

### Agregar producto al pedido (requiere login)
```
POST /ordenes/agregar-producto/
Datos: product_id
→ Agrega o incrementa cantidad en la orden activa
```

### Ver mi pedido
```
GET /ordenes/mi-orden/
→ Muestra tabla con productos, cantidades y detalles
```

### API de productos
```
GET /api/
→ Retorna JSON con todos los productos
```

---

## 🎨 Interfaz de Usuario

La aplicación utiliza **Tailwind CSS** para un diseño moderno y responsivo:

- **Header**: Logo, nombre de usuario, botones de "Mi Pedido" y "Cerrar sesión"
- **Productos**: Grid responsive de tarjetas con imágenes
- **Mi Pedido**: Tabla clara con detalles de la orden
- **Login/Registro**: Formularios seguros y validados

---

## 📧 Contacto y Soporte

Para más información o reportar problemas, contacta al equipo de desarrollo.

---

**Versión**: 1.0  
**Última actualización**: Mayo 2026  
**Licencia**: MIT
