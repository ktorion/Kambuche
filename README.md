# Kambuche
#one house in a cloud, la vecindad cosmica
simple aplicación de prueba con flask usando docker 
clonar este repositorio en /var/www/ para desplegar imagen de nginx y flask en una maquina local
con docker.


#pasos:
maquina local: linux
instalar docker:
```
apt install docker 
```
#clone este repositorio y copie el contenido en /www/var
```
git clone https://github.com/ktorion/Kambuche.git 
```
compruebe que tiene el puerto libre con:

sudo nc localhost 56733 < /dev/null; echo $?
 si la salida del comando es 1 el puerto esta libre si es 0 pruebe con otro puerto
 el script en bash levantara el contenedor de docker ya configurado
```
 sudo bash start.sh
```
# una vez levantado el contenedor compruebe que todo ha ido bien con:
```
docker ps -a
```
 es hora de revisar que todo funciona en el navegador vaya a la pagina localhost:56733

#bienvenido al la vecindad cosmica :p 

# puedes crear o cambiar lo que desees para tu proyecto personal

# el siguiente paso es apuntar nuestra pagina a un dominio
 
 dudas o madrazos a telegram : t.me/vecindadcosmica

