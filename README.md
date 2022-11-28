# Tarea3SDistri
Primer lugar se debe ejecutar el Wiki.py, aunque los archivos ya se encuentran en las carpetas.

Luego de eso ejecutaremos en docker-hadoop

```
docker-compose up --build
```

Y antes de entrar debemos ingresar las carpetas a los docker con 

```
docker cp .../Carpeta1/Documento1.txt  .../example
```

Al ya ingresar todas los Documentos nos conoctamos a namenode

```
docker exec -it namenode bash
```

Ya dentro nos dirigimos a 

```
cd /opt/hadoop-3.2.1/share/hadoop/mapreduce
```
Ahi podremos encontrar el hadoop-mapreduce-examples-3.2.1.jar, para ejecutarlo se debera utilizar

```
hadoop jar hadoop-mapreduce-examples-3.2.1.jar WordCount ...input.txt ...output
```
Si es que queremos realizar con el .java utilizado por nosotros se debera agregar al docker con
```

docker cp .../WordCount.java .../example
```

Luego se puede modificar con vim y para saber que funciona se debe ejecutar
```
hadoop com.sun.tools.javac.Main WordCount.java
```
Y se transforma luego a .class
```
jar cf wc.jar WordCount*.class
```
Ademas se deben crear los directorios (se debe hacer carpeta por carpeta), tambien se muestran los codigos para usar de ejemplo
```
hdfs dfs –mkdir /user/hadoop/wordcount
```
```
hdfs dfs –mkdir /user/hadoop/wordcount/input
```
```
echo “Hello World Bye World” > ../tutorial01/file01
```
```
hadoop fs –copyFromLocal ../tutorial01/file0*
/user/hadoop/wordcount/input
```
```
hadoop jar wc.jar WordCount /user/hadoop/wordcount/input
/user/hadoop/wordcount/output
```
```
hdfs –cat /user/hadoop/wordcount/output/part*
```
