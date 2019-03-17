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

## running vqa demo
fetch data for vqa demo

```
wget https://s3-us-west-2.amazonaws.com/abelikov/data-small.tar.gz
```

unpack
```
tar -xvf data-small.tar.gz
```

To start vqa demo:

```
docker run -p8888:8888 -v ~/projects/data:/home/relex/projects/data -it singnet-demo /home/relex/projects/semantic-vision-1/experiments/opencog/pattern_matcher_vqa/vqa
```
