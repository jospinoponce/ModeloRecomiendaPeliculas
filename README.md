# <h1> Pj_05-001 Desarrollo de un Modelo de Machine Learning para la recomendación de peliculas en plataformas de streaming</h1> 
## **HENRY BOOTCAMP | Proyecto Individual Nº1** **`Machine Learning Operations (MLOps)`**
<hr>

*El presente proyecto se desarrolla para dar cumplimiento a las actividades planteadas en la etapa de labs en el Bootcamp de Data Science de [Soy Henry](https://www.soyhenry.com/). Pretende abarcar todo el ciclo de vida de un proyecto de Machine Learning  desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML.*<br>

## 1. Introducción

Se realiza la ingesta y análisis a datos informativos de series y películas de las plataformas (Amazon, Disney, Hulu, Netflix) para llevar a cabo un **`MVP`** (_Minimum Viable Product_) de un sistema que por medio de Ciencia de Datos y Machine Learning  permita generar recomendaciones en las aplicaciones de estas plataformas de streaming a los usuarios nuevos o activos. <br>

Se cuenta con doce (12) datasets. Los cuales contienen las películas/series de cada plataforma de streaming e información de las calificaciones de películas generadas por los usuarios de estas aplicaciones. Se aplican las transformaciones pertinentes a los datasets para disponibilizar los datos limpios y generar consultas a través de una API construida en un entorno virtual dockerizado.<br>

Se implementa un modelo de ML 

<hr>



## 2. Objetivos
<hr>

## 3. Desarrollo

Los requerimientos que plantea [Soy Henry](https://www.soyhenry.com/) son:<br>

**3.1. ETL Limpieza de datos:**

* *Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)*

* *Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”)*

* *Las fechas, deberán tener el formato AAAA-mm-dd*

* *Los campos de texto deberán estar en minúsculas, sin excepciones*

* *El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).*


**3.2. Desarrollo API:**  disponibilizar los datos para realizar las siguientes consultas:

* *Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))*

* *Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))*

* *Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))*

* *Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))*

**3.3. Deployment**

**3.4. EDA**

**3.5. Sistema de recomendación ML**
<hr>


## 4. Recursos implementados

Python Version: 3.9<br>
Packages: uvicorn, pandas, matplotlib, seaborn<br>
Render<br>
Framework FastAPI <hr>

### 3.1. ETL Limpieza de datos

El proceso de ETL se realiza con este [**Origen de los datos**](https://drive.google.com/drive/folders/1_aDmVMpuOBCjlyEr86vpNFoYGloQ0bB9?usp=sharing).<br>

- Se cargan los datos para su normalización.<br>

- Se relaciona el conjunto de datos.<br>

- Se realiza los requerimientos [Soy Henry](https://www.soyhenry.com/).<br>

- Se crean dos datasets para realizar consultas: ( [**df.csv** ](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Datasets/df.csv) tiene los datos de todas las peliculas y series. ) & ([**df_1.parquet** ](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Datasets/df_1.parquet): almacena calificaciones realizadas por usuarios en las plataformas).<br>

*Los procesos realizados para el ETL están en el notebook:* [**1.ETL**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Notebooks/1.ETL_report.ipynb)<hr>


### 3.2. Desarrollo API

Se utiliza el Framework FastAPI basado en python.<br>

- Se generan las consultas solicitadas.<br>

*Los procesos realizados están en el .py:* [**main.py**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/main.py)
<hr>


### 3.3. Deployment

Se implementa la nube del web service gratuito que proporciona [Render.com](https://render.com/) para realizar el deploy y correr en su entorno la app.<br> 

*Las consultas a la API, URL:* [**API_RENDER**](https://consultas-api-peliculas-3.onrender.com)<br>
 <hr>

### 3.4. Análisis Exploratorio de datos EDA

*Los procesos realizados para el EDA están en el notebook:* [**2.EDA**](https://github.com/jospinoponce/ModeloRecomiendaPeliculas/blob/main/Notebooks/2.EDA_report.ipynb)<hr>

### 3.5. Sistema de recomendación ML

[**ML model**](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/blob/main/Notebooks/ML_model.ipynb)
<hr>

## 5. Conclución
## 6. Recomendaciones
