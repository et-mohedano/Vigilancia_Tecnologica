# Agregar librerias
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Cargar opciones del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get("https://siga.impi.gob.mx/newSIGA/content/common/principal.jsf")
sleep(3)
# Seleccionar la opción “Búsqueda por sección”.
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/form/nav/div/div[2]/ul/li[3]/a",
        )
    )
).click()
sleep(3)
# Aplicar filtros
## Área: Patentes
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[2]/div[1]/div/table/tbody/tr[1]/td/input",
        )
    )
).click()
sleep(3)
## Datos e imagen: 75
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[2]/div[2]/div[3]/table/tbody/tr[3]/td/input",
        )
    )
).click()
sleep(3)
## Gaceta: Patentes, Registros de Modelos del Utilidad y Diseños Industriales
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[3]/div/div/div/div[2]/ul/li[3]",
        )
    )
).click()
sleep(3)
## Sección: Patentes
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[4]/div/div/div/div[2]/ul/li[6]",
        )
    )
).click()
sleep(3)
## Click en medio de búsqueda para "Título"
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[5]/div/div/div[2]/select",
        )
    )
).click()
sleep(3)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[5]/div/div/div[2]/select/option[16]",
        )
    )
).click()
sleep(3)
## Ingresar frase a buscar "armas"
driver.find_element("xpath","/html/body/div[2]/div[1]/form/div[5]/div/div/div[3]/input").send_keys("arma")
sleep(3)
# Seleccionar el botón “Buscar”.
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[2]/div[1]/form/div[6]/div/div[3]/input",
        )
    )
).click()
sleep(20)
# Extraer información
indice = 1
lista_informacion = []
while True:
    try:
        indice_columna = 1
        informacion = {}
        informacion["Oficina, No de Patente y Tipo de documento"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        informacion["Tipo de documento"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Fecha de concesión"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Número de solicitud"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Fecha de presentación"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Número de solicitud internacional"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Fecha de presentación internacional"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Número de publicación internacional"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Fecha de publicación internacional"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Inventor(es)"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Titular"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Agente"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        try:
            informacion["Prioridad (es)"] = driver.find_element(
                    "xpath",
                    f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
                ).text
            indice_columna += 1
        except:
            informacion["Prioridad (es)"] = ""
        informacion["Clasificación CIP"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Clasificación CPC"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Título"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Resumen"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice_columna += 1
        informacion["Fecha de Puesta en Circulación"] = driver.find_element(
                "xpath",
                f"/html/body/div[2]/div[1]/form/div[7]/div/table/tbody/tr[{indice}]/td/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[{indice_columna}]/td[2]",
            ).text
        indice += 1
        lista_informacion.append(informacion)
    except:
        # Construir archivo CSV
        campos = ["Oficina, No de Patente y Tipo de documento", "Tipo de documento", "Fecha de concesión", "Número de solicitud", "Fecha de presentación", "Número de solicitud internacional", "Fecha de presentación internacional", "Número de publicación internacional", "Fecha de publicación internacional", "Inventor(es)", "Titular", "Agente", "Prioridad (es)", "Clasificación CIP", "Clasificación CPC", "Título", "Resumen", "Fecha de Puesta en Circulación"]
        with open('resultados.csv', 'w', encoding="utf-8") as csvfile:
            Writer = csv.DictWriter(csvfile, fieldnames = campos)
            Writer.writeheader()
            Writer.writerows(lista_informacion)
        # Terminar ejecución
        exit()