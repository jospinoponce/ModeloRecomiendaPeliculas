# <h1> Pj_05-001 Desarrollo de un Modelo de Machine Learning para la recomendación de peliculas en plataformas de streaming</h1> 
## **HENRY BOOTCAMP | Proyecto Individual Nº1** **`Machine Learning Operations (MLOps)`**
<hr>

*El presente proyecto se desarrolla para dar cumplimiento a las actividades planteadas en la etapa de labs en el Bootcamp de Data Science de [Soy Henry](https://www.soyhenry.com/). Pretende abarcar todo el ciclo de vida de un proyecto de Machine Learning  desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML.*<br>

## Introducción

Se realiza la ingesta y análisis a datos informativos de series y películas de las plataformas (Amazon, Disney, Hulu, Netflix) para llevar a cabo un **`MVP`** (_Minimum Viable Product_) de un sistema que por medio de Ciencia de Datos y Machine Learning  permita generar recomendaciones en las aplicaciones de estas plataformas de streaming a los usuarios nuevos o activos. <br>

Se cuenta con doce (12) datasets. Los cuales contienen las películas/series de cada plataforma de streaming e información de las calificaciones de películas generadas por los usuarios de estas aplicaciones. Se aplican las transformaciones pertinentes a los datasets para disponibilizar los datos limpios y generar consultas a través de una API construida en un entorno virtual dockerizado.<br>

Se implementa un modelo de ML 

<hr>



## Objetivos
<hr>

## Desarrollo

Los requerimientos que plantea [Soy Henry](https://www.soyhenry.com/) son:<br>

**1. Limpieza de datos:**

* *Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)*

* *Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”)*

* *Las fechas, deberán tener el formato AAAA-mm-dd*

* *Los campos de texto deberán estar en minúsculas, sin excepciones*

* *El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).*


**2. Desarrollo API:**  disponibilizar los datos para realizar las siguientes consultas:

* *Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))*

* *Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))*

* *Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))*

* *Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))*

**3. Deployment**

**4. Sistema de recomendación ML**
<hr>


## Recursos implementados:

Python Version: 3.9<br>
Packages: pandas, numpy<br>
Docker<br>
Render<br>
Framework FastAPI <hr>

## Limpieza de datos

[**Origen de los datos**](https://drive.google.com/drive/folders/1_aDmVMpuOBCjlyEr86vpNFoYGloQ0bB9?usp=sharing) Los datasets tienen  información acerca de Movies y Tv Shows de  Netflix, Amazon, Hulu y Disney; tienen columnas como el año de publicación, la duración (en minutos o temporadas), el año que se subió a la plataforma, el cast, director, entre otros.<br>

- Se cargan los datos para su normalización.<br>

- Se relaciona el conjunto de datos.<br>

- Se realiza los requerimientos [Soy Henry](https://www.soyhenry.com/).<br>

- Se crean dos datasets generales para realizar consultas. Uno es un **.csv**, tiene los datos de todas las peliculas y series. Mientras el otro es un **.parquet** almacena todas las calificaciones realizadas por usuarios en las plataformas (*se pueden consultar en:* [Datasets](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/tree/main/Datasets)).<br>

*Los procesos realizados están en:* [**EDA_report**](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/blob/main/Notebooks/EDA_report.ipynb)<hr>


## Desarrollo API

Se utiliza el Framework FastAPI basado en python.<br>

- Se generan las consultas solicitadas.<br>

**API:** [**main.py**](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/blob/main/main.py)
<hr>


## Deployment

Se implementa la nube de[Render](https://render.com/) para realizar el deploy y correr en su entorno la app.<br> 
[DockerFile](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/blob/main/DockerFile)<br>
[****]() <hr>

## Sistema de recomendación ML

[**ML model**](https://github.com/jospinoponce/MLmodelRecomendacionPeliculas/blob/main/Notebooks/ML_model.ipynb)
<hr>

## Conclución
