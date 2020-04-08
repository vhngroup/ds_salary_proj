import glassdoor_scraper as gs
import pandas as pd
path =  "D:/Git/ds_salary_proj/chromedriver"

df = gs.get_jobs('data science', 15, False, path, 15)
df
