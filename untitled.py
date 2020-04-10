import glassdoor_scraper as gs
import pandas as pd

def inicializar():
    path =  "D:/Git/ds_salary_proj/chromedriver"
    df = gs.get_jobs('data science', 1000, False, path, 15)
    df.to_csv('glassdoor_jobs.csv', index = False)

def arreglo ():
    contry = '' #ingrese las iniciales del pais o ciudad a filtrar
    year = 2020
    return contry, year


if __name__ == "__main__": # Se inicializa el programa
    arreglo()
    inicializar()
    
 




