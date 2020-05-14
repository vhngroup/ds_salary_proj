import glassdoor_scraper as gs
import data_Cleaning as d_T
import pandas as pd

contry = '' #ingrese las iniciales del pais o ciudad a filtrar
year = 2020

def main():
      #inicializar()
      extrac_Data()

def inicializar():
   path =  "D:/Git/ds_salary_proj/chromedriver"
   df = gs.get_jobs('data science', 1000, False, path, 15)
   df.to_csv('glassdoor_jobs.csv', index = False)

def extrac_Data():
    m_DT = d_T.load_data()
    # return contry, year
 
if __name__ == "__main__": # Se inicializa el programa
    main()

def extrac_Data():
    print('inicia extract data')
    m_DT = d_T.load_data()
    # return contry, year

if __name__ == "__main__": # Se inicializa el programa
    main()