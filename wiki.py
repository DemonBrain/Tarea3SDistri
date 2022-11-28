
import wikipedia as wiki


busqueda = ['soccer','League of Legends','jugada','England','informacion','Text file','Manga','Anime','Argentina','Chile']


for i in range(10):

    if i<5:
        txt = 'Tarea3/Carpeta1/Documento'
        archv = open(txt+str(i+1)+'.txt','w') #Abriendo y creando 
        archv.close()

        info = wiki.page(busqueda[i])
 
        archv = open(txt+str(i+1)+'.txt','a')
        archv.write(info.content) 
        archv.close()
     
    else:
        txt = 'Tarea3/Carpeta2/Documento'
        archv = open(txt+str(i+1)+'.txt','w') #Abriendo y creando 
        archv.close()

        info = wiki.page(busqueda[i])
 
        archv = open(txt+str(i+1)+'.txt','a')
        archv.write(info.content) 
        archv.close()









