# 📝 Documentación de Código - Proyecto Coffee Shop

Este documento resume toda la documentación y comentarios agregados a cada archivo del proyecto.

---

## ✅ Archivos Documentados

### **App: PRODUCTS (Productos)**

#### [models.py](products/models.py)
- **`Product`**: Modelo principal que representa un producto
  - Atributos: name, price, description, available, photo
  - Objetivo: Almacenar productos disponibles en la cafetería
  - Métodos: `__str__()` para representación en texto

#### [forms.py](products/forms.py)
- **`ProductForm`**: Formulario basado en ModelForm
  - Objetivo: Interfaz HTML para agregar nuevos productos
  - Campos: name, description, price, available, photo
  - Etiquetas en español

#### [views.py](products/views.py)
- **`ProductListView`**: Vista para mostrar catálogo (página HOME)
  - GET `/` → Lista de productos
  - Objetivo: Mostrar todos los productos a usuarios
  
- **`ProductFormView`**: Vista para agregar productos
  - GET `/agregar/` → Formulario vacío
  - POST `/agregar/` → Guardar nuevo producto
  - Objetivo: Interfaz para gerentes/admin agregar productos
  
- **`ProductListAPIView`**: Vista API REST
  - GET `/api/` → Retorna JSON con productos
  - Objetivo: Endpoint para aplicaciones externas (móvil, etc)

#### [serializer.py](products/serializer.py)
- **`ProductSerializer`**: Convierte Product a JSON
  - Campos serializados: name, price, description, available, photo
  - Objetivo: Preparar datos para API REST

#### [admin.py](products/admin.py)
- **`ProductAdmin`**: Personalización de admin Django
  - Objetivo: Interfaz mejorada en `/admin/`
  - list_display: nombre, precio, disponibilidad
  - search_fields: búsqueda por nombre

---

### **App: ORDERS (Pedidos)**

#### [models.py](orders/models.py)
- **`Order`**: Modelo para pedidos
  - Atributos: user, is_active, order_date
  - Objetivo: Almacenar información de cada pedido
  - Relación: Un usuario puede tener múltiples órdenes, pero solo una activa
  - Flujo: usuario agrega productos → se crea orden → marca como inactiva cuando confirma
  
- **`OrderProduct`**: Tabla intermedia entre Order y Product
  - Atributos: order, product, quantity
  - Objetivo: Almacenar productos dentro de una orden con cantidades
  - Ejemplo: Order #5 con 2x Café, 1x Cappuccino

#### [views.py](orders/views.py)
- **`MiOrdenView`**: Vista para mostrar pedido actual
  - GET `/ordenes/mi-orden/` → Muestra tabla con productos
  - Objetivo: Permitir usuario revisar su pedido antes de confirmar
  - Requiere: Usuario autenticado (LoginRequiredMixin)
  
- **`CreateOrderProductView`**: Vista para agregar productos al pedido
  - POST `/ordenes/agregar-producto/` → Procesa form de "Agregar al pedido"
  - Lógica: 
    - Si no existe orden activa: la crea
    - Si producto no está en orden: lo agrega
    - Si producto ya existe: incrementa cantidad
  - Objetivo: Agregar productos al carrito/pedido actual
  
- **`index`**: Vista simple de bienvenida
  - GET `/ordenes/` → Mensaje placeholder

#### [forms.py](orders/forms.py)
- **`OrderProductForm`**: Formulario para productos en orden
  - Objetivo: Seleccionar producto y cantidad
  - Campos: product, quantity
  - Nota: No usado actualmente, reservado para futuro

#### [admin.py](orders/admin.py)
- **`OrderProductInlineAdmin`**: Muestra productos dentro de orden
  - Objetivo: Ver/editar productos de forma inline en admin
  
- **`OrderAdmin`**: Personalización de admin para órdenes
  - Objetivo: Interfaz en `/admin/` para gestionar pedidos
  - Incluye: tabla inline con productos de cada orden

---

### **App: USERS (Usuarios)**

#### [views.py](users/views.py)
- **`RegisterView`**: Vista para registro de nuevos usuarios
  - GET `/usuarios/registro/` → Muestra formulario
  - POST `/usuarios/registro/` → Crea cuenta
  - Objetivo: Permitir que nuevos clientes se registren
  - Redirecciona a: `/usuarios/login/` después de registro exitoso
  - Form: UserCreationForm (incluido en Django)

#### [urls.py](users/urls.py)
- **Rutas**:
  - `/usuarios/login/` → LoginView (inicio de sesión)
  - `/usuarios/logout/` → LogoutView (cerrar sesión)
  - `/usuarios/registro/` → RegisterView (registro)
- **Objetivo**: Manejar autenticación de usuarios

---

### **Configuración Principal**

#### [coffe_shop/urls.py](coffe_shop/urls.py)
- **Configuración central de enrutamiento**
- **Mapeo de rutas**:
  - `/` → products.urls (catálogo)
  - `/admin/` → Admin Django
  - `/usuarios/` → users.urls (autenticación)
  - `/ordenes/` → orders.urls (pedidos)
- **En DEBUG**: Sirve archivos estáticos y media

#### [coffe_shop/settings.py](coffe_shop/settings.py)
- **Secciones comentadas**:
  - Configuración de seguridad
  - Apps instaladas (products, users, orders, rest_framework)
  - Middleware
  - Base de datos (PostgreSQL)
  - Archivos estáticos y media
  - Autenticación y redirecciones
  - REST Framework

---

## 🔄 Flujo de Operaciones

### 1. **Registro e Inicio de Sesión**
```
Usuario nuevo:
  → /usuarios/registro/ (RegisterView)
  → Completa formulario
  → Se crea cuenta
  → Redirige a /usuarios/login/

Usuario existente:
  → /usuarios/login/ (LoginView)
  → Ingresa credenciales
  → Se inicia sesión
  → Redirige a /
```

### 2. **Ver Catálogo y Agregar Productos**
```
Usuario entra a:
  → / (ProductListView)
  → Ve tarjetas de productos
  → Click "Agregar al pedido"
  
Detrás de escenas:
  → POST a /ordenes/agregar-producto/ (CreateOrderProductView)
  → Se crea Order (si no existe)
  → Se crea/incrementa OrderProduct
  → Redirige a /ordenes/mi-orden/
```

### 3. **Ver y Confirmar Pedido**
```
Usuario click en "Mi Pedido":
  → GET /ordenes/mi-orden/ (MiOrdenView)
  → Obtiene su orden activa
  → Muestra tabla con productos
  → Puede "Seguir comprando" o "Confirmar pedido"
```

### 4. **Panel de Administración**
```
Admin accede a:
  → /admin/ (Django Admin)
  → Ver/agregar/editar productos
  → Ver todas las órdenes
  → Ver productos dentro de cada orden
```

---

## 🎯 Métodos Principales por Clase

### Product
| Método | Tipo | Función |
|--------|------|---------|
| `__str__()` | Instancia | Retorna nombre del producto |

### ProductListView
| Método | Tipo | Función |
|--------|------|---------|
| Heredado de ListView | Instancia | Obtiene y renderiza todos los productos |

### ProductFormView
| Método | Tipo | Función |
|--------|------|---------|
| `form_valid()` | Instancia | Guarda nuevo producto en BD |

### ProductListAPIView
| Método | Tipo | Función |
|--------|------|---------|
| `get()` | Instancia | Retorna JSON con todos los productos |

### Order
| Método | Tipo | Función |
|--------|------|---------|
| `__str__()` | Instancia | Retorna "Order X by usuario" |

### OrderProduct
| Método | Tipo | Función |
|--------|------|---------|
| `__str__()` | Instancia | Retorna "cantidad x producto for Order X" |

### MiOrdenView
| Método | Tipo | Función |
|--------|------|---------|
| `get_object()` | Instancia | Obtiene orden activa del usuario |
| `get()` | Instancia | Renderiza orden o mensaje vacío |

### CreateOrderProductView
| Método | Tipo | Función |
|--------|------|---------|
| `post()` | Instancia | Procesa agregar producto a orden |

### RegisterView
| Método | Tipo | Función |
|--------|------|---------|
| Heredado de CreateView | Instancia | Procesa registro de usuario |

---

## 🔐 Seguridad Implementada

✅ **CSRF Protection**: Todos los formularios con `{% csrf_token %}`  
✅ **LoginRequiredMixin**: Vistas que requieren autenticación  
✅ **Validación de Contraseñas**: Django hash automático  
✅ **on_delete Rules**:
- `CASCADE`: Si usuario se elimina, se eliminan sus órdenes
- `PROTECT`: No se puede eliminar producto si está en una orden

---

## 📊 Modelos de Base de Datos

### Product
```
- id (PK)
- name (CharField)
- price (DecimalField)
- description (TextField)
- available (BooleanField)
- photo (ImageField)
```

### Order
```
- id (PK)
- user (FK -> auth.User)
- is_active (BooleanField)
- order_date (DateTimeField)
```

### OrderProduct
```
- id (PK)
- order (FK -> Order)
- product (FK -> Product)
- quantity (PositiveIntegerField)
```

---

## 📱 Endpoints Principales

| Método | URL | Vista | Descripción |
|--------|-----|-------|-------------|
| GET | `/` | ProductListView | Catálogo de productos |
| GET | `/api/` | ProductListAPIView | API JSON de productos |
| POST | `/ordenes/agregar-producto/` | CreateOrderProductView | Agregar producto al pedido |
| GET | `/ordenes/mi-orden/` | MiOrdenView | Ver pedido actual |
| GET | `/usuarios/login/` | LoginView | Formulario login |
| POST | `/usuarios/login/` | LoginView | Procesar login |
| POST | `/usuarios/logout/` | LogoutView | Cerrar sesión |
| GET | `/usuarios/registro/` | RegisterView | Formulario registro |
| POST | `/usuarios/registro/` | RegisterView | Procesar registro |
| GET | `/admin/` | AdminSite | Panel de administración |

---

## 📚 Convenciones Utilizadas

- **Nombres de variables en español**: user, orden, producto
- **Docstrings en cada clase/función**: Explicar objetivo y flujo
- **Comentarios inline**: Para lógica compleja
- **LoginRequiredMixin**: Para proteger vistas que requieren autenticación
- **reverse_lazy()**: Para redirecciones en vistas
- **get_or_create()**: Para obtener u crear órdenes sin duplicados

---

**Última actualización**: Mayo 2026  
**Versión del proyecto**: 1.0
