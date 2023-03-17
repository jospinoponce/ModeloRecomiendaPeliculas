from fastapi import FastAPI
import pandas as pd

# CREACION APP:----------------------------------------------------------------------------

app = FastAPI(title='Consulta [movies|series] en (Amazon Prime, Disney+, Hulu, Netflix)',
description='Desarrollo de sistema de consultas para series y peliculas en las principales plataformas de streaming hasta el año (2021).',
version='1.00.01')

# METODOS :---------------------------------------------------------------------------------

@app.get('/')
async def read_root():
   return {'API':"hi world"}

@app.get('/about/')
async def about():
   return {'Proyecto individual del Bootcamp de Data Science de Henry. Desarrollado por Jaime Ospino cohorte 08.'}

# Carga del dataframe que tiene (Peliculas/series en plataformas):--------------------------

@app.on_event('startup')
async def startup():
   global df
   df = pd.read_csv('Datasets/df.csv')


# DESARROLLO DE CONSULTAS

# Consulta 1 :------------------------------------------------------------------------------

''' Función que genera la consulta de la película o serie con mayor duración 
   dependiendo el año, la plataforma, y el tipo de duración (season) o (minutos)'''

@app.get('/get_max_duration/({year}, {platform}, {duration_type})')
async def get_max_duration(year:int,platform:str,duration_type:str):
     
   result=df.loc[(df['release_year'] == year) & (df['plataforma'] == platform) & (df['duration_type'] == duration_type)]
   maximo =result['duration_int'].max()
   names = result[result['duration_int']==maximo] ['title']
   name = names.to_list()
   name = name[0]
   if duration_type =="min": 
      return f"Pelicula de mayor duración: {name} con {maximo} minutos"
   elif duration_type =="season":
      return f"Serie de mayor duración: {name} con {maximo} seasons" 

# Consulta 2:-------------------------------------------------------------------------------------
   
'''función que genera la consulta de la cantidad de películas por plataforma 
   con un puntaje mayor a XX en determinado año'''

@app.get('/get_score_count/({platform}, {score},{year})')
async def get_score_count(platform:str,score:float, year:int ): 
   
   df_1 = pd.read_parquet('Datasets/df_1.parquet')
   movie=((df_1['plataforma']==platform)&(df_1['score']>score) & (df_1['year']==year) ).sum()
   return f" {platform}: tiene {movie} peliculas con un score mayor a {score}  " 
 
# Consulta 3:------------------------------------------------------------------------------------

''' función que genera la consulta de la cantidad de peliculas por plataforma '''

@app.get('/get_count_platauvform/({platform})')
async def get_count_platform(platform:str):

   # cantidad de películas 
   movie =((df['plataforma']==platform) & (df.iloc[:, 2].str.contains('movie'))).sum()  

   # cantidad series
   tv_show =((df['plataforma']==platform) & (df.iloc[:, 2].str.contains('tv show'))).sum() 

   return f" {platform}: tiene {movie} peliculas y {tv_show} series "

# Consulta 4:------------------------------------------------------------------------------------   

'''función que genera la consulta del actor que más se repite según plataforma y año '''

@app.get('/get_actor/({platform},{year})')
async def get_actor(platform:str, year:int):

   result = (df[(df['plataforma']==platform) & (df['release_year']==year)])
   '''se itera en la columna cast los registros diferentes a 'not_data', para ver los actores. 
   se reemplaza la coma y el espacio, por coma. '''

   for i in result['cast']:
      if i != 'not_data':
         i=i.replace(', ', ',')
      else:
         pass
# Se crea una lista para guardar los actores. Se separan por ','.
   lista=[]
   for i in result['cast']:
      if i != 'not_data':
         s=i.split(',')
         for j in range(len(s)):             
               if s[j] not in lista:
                  lista.append(s[j])
               else:
                  pass
      else:
         pass
   lista=list(set(lista))
# Se crea un diccionario para guardar las veces que se repite cada actor
   contador = 0
   dict={}
   for i in lista:
      contador = 0
      for j in result['cast']:
         if i in j.split(','):
               contador+=1
      dict[i]=contador
   return f"Actor con más peliculas o series en el {year} y en {platform} es:{max(dict,key=dict.get)} "



   #------------------------------------------------------------------------------------------------------    