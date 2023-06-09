# <h1> Pj_05-001 Desarrollo de un Modelo de Machine Learning para la recomendación de películas en plataformas de streaming</h1> 

*El presente proyecto se desarrolla para dar cumplimiento a las actividades planteadas en la etapa de labs en el Bootcamp de Data Science de [Soy Henry](https://www.soyhenry.com/). Pretende abarcar todo el ciclo de vida de un proyecto de Machine Learning  desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML.*<hr>

## 1. Introducción

Se realiza la ingesta y análisis a datos de series y películas en (Amazon, Disney, Hulu, Netflix) para llevar a cabo un **`MVP`** (_Minimum Viable Product_) de un sistema que permita generar recomendaciones de peliculas y series a usuarios que realizaron reseñas en estas plataformas de streaming. Se cuenta con doce (12) datasets. Se aplican  transformaciones pertinentes para disponibilizar los datos y generar consultas a través de una API construida en un entorno virtual dockerizado. <br>

Se implementa un modelo de machine learnig ML no supervisado. Usando la técnica: descomposición singular de valores (SVD) se analiza y predice las preferencias de películas y series del usuario dada sus calificaciones. <hr>

## 2. Objetivos
- Desarrollar una API que permita al usuario realizar 4 consultas a los datos de las películas y series.
- Embeber el modelo de machine learning en una app disponibilizada al usuario.<hr>

## 3. Recursos implementados

Python Versión: 3.9<br>
Packages: Uvicorn, Pandas, Matplotlib, Seaborn, Surprise, Gradio.<br>
Render.<br>
Framework FastAPI. <hr>

## 4. Desarrollo
### 4.1 ETL
Los datos de origen: [**data**](https://drive.google.com/drive/folders/1_aDmVMpuOBCjlyEr86vpNFoYGloQ0bB9?usp=sharing).<br>

- Se cargan los datos para su normalización (Tratamiento de nulos, valores duplicados, formateo de variables, entre otros..).. <br>

- Se crean dos datasets para realizar consultas: ( [**df.csv** ](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Datasets/df.csv) tiene los datos de todas las películas y series. ) & ([**df_1.parquet** ](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Datasets/df_1.parquet): almacena calificaciones realizadas por usuarios en las plataformas).<br>

*Los procesos realizados para el ETL están en el notebook:* [**1.ETL**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/1.ETL_report.ipynb)

### 4.2 Análisis Exploratorio de datos EDA

*115077 usuarios realizaron 11005757  calificaciones a películas/series en las distintas plataformas streaming con un score de 1 a 5.*

| score |    %    |
|:-----:|:-------:|
|   1  |  4.67 % |
|   2  |  8.24 % |
|   3  | 25.07 % |
|   4  | 39.01 % |
|   5  | 23.02 % |

*Los usuarios ven en las plataformas de streaming más películas que series.*<br>
*La plataforma de streaming que más visualizaciones tiene es netflix.*<br>
*Las dos películas más vistas con más de 560 reseñas son de amazon "from other worlds" y "the organization".*<br>
*El género de películas o series que más visualizaciones tiene es "comedia".*

<img src="_src/1.png" width="700" height="500px">

*Los procesos realizados para el EDA están en el notebook:* [**2.EDA**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/2.EDA_report.ipynb)<hr>

## 5. Resultados

### 5.1 Desarrollo API

Se utiliza el Framework FastAPI. Se disponibilizan las siguientes consultas:<br>

* *Película con mayor duración con filtros de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (función: get_max_duration(year, platform, duration_type))*
* *Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (función: get_score_count(platform, scored, year))*
* *Cantidad de películas por plataforma con filtro de PLATAFORMA. (función:  get_count_platform(platform))*
* *Actor que más se repite según plataforma y año. (función: get_actor(platform, year))*

*Los procesos realizados están en el .py:* [**main.py**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/main.py)

#### Deployment

Se implementa la nube del web service gratuito que proporciona [Render.com](https://render.com/) para realizar el deploy y correr en su entorno la app.<br> 

*Las consultas a la API, URL:* [**API_RENDER**](https://consultas-api-peliculas-3.onrender.com)<br>
 
### 5.2 Sistema de recomendación ML

EL sistema de recomendación que se desarrolla define si para un id usuario seleccionado una película determinada sería recomendable o no.<br> 

El modelo establece una recomendación positiva a una calificación predicha superior al 3,7 de rating en un score del 1 al 5.

Se usa la librería Surprise, Gradio.<br>

- Se instancia y se entrena un modelo SVD (Descomposición Singular de Valores). 
- Se genera el modelo de recomendación.
- Se calcula el error cuadrático medio (RMSE) y el error absoluto medio (MAE) al modelo. 
- Se validan hiperparámetros.
- Se desarrolla una interfax para el MVP del sistema de recomendación a través de Gradio.

<img src="_src/2.png" width="800" height="320px">


Se puede acceder a la consulta de la interfaz a través de Gradio. *Los procesos realizados para el Modelado de Machine Learning están en el notebook:* [**3.ML_model**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/3.ML_model.ipynb)

<hr>

## 6. Conclusión

Se concluye que como un **`MVP`** (_Minimum Viable Product_) el modelo es aceptable. Tiene un MAE de 0.75 indicando que, en promedio, comete un error absoluto medio del 75% en las predicciones de calificaciones de películas para un usuario, esto significa que hace predicciones precisas. El valor de RMSE es de 0.96 es alto, el modelo tiene una gran variabilidad en las predicciones.

Para modelos de recomendación de películas, es importante tener en cuenta otros aspectos como: la diversidad, serendipia de las recomendaciones, cobertura de las recomendaciones, escalabilidad, capacidad de explicar las recomendaciones. Variables que no se tienen en cuenta para el desarrollo de este modelo.


