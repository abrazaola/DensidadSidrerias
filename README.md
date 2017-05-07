# MapReduce con Apache Hadoop
## Authors
* Aitor Brazaola
* Sergio Anguita

## Dataset (API)
```http://opendata.euskadi.eus/catalogo/-/restaurantes-asadores-y-sidrerias-de-euskadi/```

## Obtención del dataset de la API
```./get_dataset.py```

## Para ejectutarlo sin Hadoop:
```cat restaurantes.xml | ./mapper.py | sort | ./reducer.py```

## Para ejecutarlo en Hadoop:
1. Colocar el fichero de datos dentro de Hadoop fs:
```hadoop fs -put restaurantes.xml```
2. Ejecutar Hadoop sobre el fichero:
```hs ./mapper.py ./reducer.py restaurantes.xml salida```
3. Comprobar los ficheros de salida:
```hadoop fs -ls salida```
4. Obtener el fichero de datos resultante
```hadoop fs -get salida/part-00000```
5. Mostrarlo en local
```cat part-00000```





