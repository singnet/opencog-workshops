# opencog-intro
simple examples for opencog

The demo requires docker and 64-bit OS 


## running opencog introduction  
to build docker image run

```
docker build . -t singnet-demo
```

To start docker with simple examples notebook:  

```
docker run -p8888:8888  -it singnet-demo /home/relex/opencog-intro-master/notebook.sh 
```

If notebook successully started you should  
be able to open it at localhost:8888

Use password as password
