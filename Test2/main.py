from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)

#Creacion Carpeta Evidencias
repositorio_evidencias = "01_evidencias"
if not os.path.exists(repositorio_evidencias):
    os.makedirs(repositorio_evidencias)
    
def screenshot(paso):
    ruta_archivos= os.path.join(repositorio_evidencias,f"{paso}.png")
    driver.save_screenshot(ruta_archivos)

try:
    # Paso 1: Abrir la web
    driver.get("https://www.mercadolibre.com")
    screenshot("01_inicio")

    # Paso 2: Seleccionar país
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "México"))).click()
    screenshot("02_pais")
    
    #Aceptacion de cookies
    try:
        aceptar_cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aceptar') or contains(., 'Entendido')]"))
        )
        aceptar_cookies.click()
        print("Banner de cookies cerrado.")
    except:
        print("No apareció el banner de cookies.")
        
    # Paso 3: Buscar "playstation 5"
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "as_word")))
    search_box.send_keys("playstation 5")
    search_box.submit()
    screenshot("03_busqueda")
    
    # Paso 4: Filtrar por condición "Nuevo"
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a/span[1]"))).click()
    screenshot("04_nuevo")
    
    # Paso 5: Filtrar por ubicación 
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Distrito Federal"))).click()
    screenshot("05_FiltroPais")
    
    # Paso 5: Orden de productos
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/section/div[2]/div[2]/div/div/div[2]/div"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Mayor precio')]"))).click()
    screenshot("06_orden")
    
    #  # Paso 7: Obtener los primeros 5 productos
    # productos = wait.until(EC.presence_of_all_elements_located(
    #     (By.XPATH, "/html/body/main/div/div[2]/section") 
    # ))[:5]   
    
    # print("Primeros 5 productos (nombre y precio):")
    # for i, producto in enumerate(productos, start=1):
    #     try:
    #         nombre = producto.find_element(By.XPATH, ".//h2").text
    #         precio = producto.find_element(By.XPATH, ".//span[@class='andes-money-amount__fraction']").text
    #         print(f"{i}. {nombre} - ${precio}")
    #     except Exception as e:
    #         print(f"{i}. No se pudo obtener la información del producto.")

    # screenshot("07_resultados")
    
    def generar_informe():
        with open("informe.html", "w", encoding="utf-8") as f:
            f.write("<html><head><title>Informe de Automatización</title></head><body>")
            f.write("<h1>Informe de Automatización: Búsqueda en Mercado Libre</h1>")
            
            pasos = [
                "01_inicio",
                "02_pais",
                "03_busqueda",
                "04_nuevo",
                "05_cdmx",
                "06_orden",
                "07_resultados"
            ]

            for paso in pasos:
                f.write(f"<h2>Paso: {paso}</h2>")
                f.write(f"<img src='{repositorio_evidencias}/{paso}.png' width='800'><hr>")

            f.write("</body></html>")
finally:
    driver.quit()
    generar_informe()
