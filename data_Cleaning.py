import pandas as  pd
import untitled


def load_data():
    contry = untitled.contry #traemos la cidad
    year = untitled.year #traemos el año
    #Parsing Salary
    
    df = pd.read_csv('glassdoor_jobs.csv')
    df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
    df['employer_Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
    
    
    df = df [df['Salary Estimate'] !=  '-1']
    salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) #Retirar los textos a partir de los corchetes (
    minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
    
    min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))
    df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
    df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
    df['avg_salary'] = (df.min_salary+df.max_salary)/2
    
    #Name Company
    df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)
    #state field
    df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
    
    
    #comparamos si la columna locaciòn "ciudad" y la columna Headquarters "sede" par determinar donde sera el trabajo.
    df['some_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)
    
    #age company
    df['age'] = df.Founded.apply(lambda x: x if x <1 else year - x) #traemos la antiguedad de las empresas
    
    #parsin of job descriptio (Python etc)
    #Organizamos por los lenguajes mas utilizados
    #python
    df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
    df.python_yn.value_counts()
    #r studio
    df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
    df.R_yn.value_counts()
    #spark
    df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
    df.Spark.value_counts()
    
    #Citizen
    
    if len(contry) <=0: #valida si hay o no ciudad a filtrar
        pass
    else: 
        df = df [df['job_state'] == contry]
    df.job_state.value_counts()
    
    df.columns
    
    df_out = df.drop([], axis = 0)
    df_out.to_csv('salary_data_Cleaned.csv', index = False)
    pd.read_csv('salary_data_Cleaned.csv')