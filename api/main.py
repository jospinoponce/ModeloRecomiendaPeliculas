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
   df = pd.read_csv('../Datasets/df.csv')


# DESARROLLO DE CONSULTAS

# Consulta 1 :------------------------------------------------------------------------------

''' Función que genera la consulta de la película o serie con mayor duración 
   dependiendo el año, la plataforma, y el tipo de duración (season) o (minutos)'''

@app.get('/get_max_duration/({year}, {platform}, {duration_type})')
async def get_max_duration(year:int,platform:str,duration_type:str):

   if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
      return f' ValueError:La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.'
   if duration_type is not None and duration_type not in ['min', 'season']:
      return f'ValueError: Los valores validos para duración son: min, season'
   if year is not None and year not in [1920, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]:
     return f'ValueError: No hay registros para este año'

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

   if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
      return f' ValueError:La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.'
   if score  >5 or score<0 :
      return f' ValueError:El score debe estar entre (0-5).'
   if year is not None and year not in [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]:
      return f'ValueError: No hay registros para este año el rango es 1995-2017'

   df_1 = pd.read_parquet('../Datasets/df_1.parquet')
   movie=df_1[(df_1['plataforma']==platform) & (df_1['score']>score) & (df_1['year_scored']==year)]
   movie=movie.groupby(["id","plataforma"])[['score']].mean().shape[0]
   return f" {platform}: tiene {movie} peliculas con un score mayor a {score}  " 
 
# Consulta 3:------------------------------------------------------------------------------------

''' función que genera la consulta de la cantidad de peliculas por plataforma '''

@app.get('/get_count_platauvform/({platform})')
async def get_count_platform(platform:str):

   if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
      return f' ValueError:La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.'

   # cantidad de películas 
   movie =((df['plataforma']==platform) & (df.iloc[:, 2].str.contains('movie'))).sum()  

   # cantidad series
   tv_show =((df['plataforma']==platform) & (df.iloc[:, 2].str.contains('tv show'))).sum() 

   return f" {platform}: tiene {movie} peliculas y {tv_show} series "

# Consulta 4:------------------------------------------------------------------------------------   

'''función que genera la consulta del actor que más se repite según plataforma y año '''

@app.get('/get_actor/({platform},{year})')
async def get_actor(platform:str, year:int):

   if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
      return f' ValueError:La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.'
   if year is not None and year not in [1920, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]:
     return f'ValueError: No hay registros para este año'

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