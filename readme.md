# Automatización de Pruebas con Selenium - Mercado Libre

Este proyecto automatiza la búsqueda de productos en el sitio web de [MercadoLibre México](https://www.mercadolibre.com.mx), aplicando filtros y extrayendo información de los primeros resultados, con generación de capturas y un informe en HTML.

---

# Funcionalidades Automatizadas

- Ingresar a https://www.mercadolibre.com
- Seleccionar México como país
- Buscar el término "playstation 5"
- Filtrar por:
  - Condición: Nuevos
  - Ubicación: Distrito Federal
- Ordenar por Mayor precio
- Extraer e imprimir en consola el nombre y precio de los primeros 5 productos
- Guardar capturas de pantalla de cada paso
- Generar un informe HTML con las capturas

---

# Tecnologías utilizadas

- Python 3.11.4
- Selenium WebDriver
- Google Chrome (137.0.7151.120)
- Librerías auxiliares:
  - os (manejo de archivos/rutas)
  - time (esperas opcionales)




# Requisitos Previos

- Python 3 instalado
- Google Chrome instalado
- Instalar Selenium WebDriver "pip install selenium"

- Descargar el ChromeDriver correspondiente la version de Chrome

---

## Como Ejecutar

1. Clona o descarga este repositorio.
2. Ejecuta el script: python main.py

---

# Mejores prácticas implementadas

- Uso de WebDriverWait para esperas explícitas
- Capturas de pantalla para informes
- Manejo de excepciones y eventos dinámicos (ej. cierre de banner de cookies)
- XPaths dinámicos resistentes a cambios menores en el sitio