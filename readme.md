# 🎭 playwright-python-POM

Este proyecto implementa automatización de pruebas para **SauceDemo** utilizando **Playwright** con **Python**. Se basa en el patrón **Page Object Model (POM)** para mantener un código modular y organizado.

## 🧑‍💻 Autor

👤 **Jhon Hader Rojas Cabrera**  
📌 Proyecto desarrollado como parte de una prueba técnica de automatización.

## 🚀 Tecnologías utilizadas

- **Python 3.x**: Lenguaje de programación.
- **Playwright**: Herramienta para automatización de pruebas web.
- **pytest**: Framework para ejecutar las pruebas.
- **Page Object Model (POM)**: Patrón de diseño utilizado para la organización del código.

## 📁 Arquitectura del proyecto

```
playwright-python-POM/
│── __pycache__/
│── .pytest_cache/
│── .vscode/
│   ├── launch.json
│   ├── settings.json
│── pages/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│── .gitignore
│── conftest.py
│── pytest.ini
│── test_example.py
│── README.md
```

## ⚡ Instalación y configuración

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/jhonrojas1998/Test-frontend-QA-Cod.git
   cd playwright-python-POM
   ```

2. **Crea y activa un entorno virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Instala las dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Instala Playwright y sus navegadores**  
   ```bash
   playwright install
   ```

## 🛠️ Cómo ejecutar las pruebas

Ejecutar todas las pruebas:  
```bash
pytest --headed
```

Ejecutar un caso de prueba específico:  
```bash
pytest tests/test_cart.py --headed
```

Ejecutar en modo **headless** (sin interfaz gráfica):  
```bash
pytest tests/ --headless
```


