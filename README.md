# opencog-intro
simple examples for opencog

fetch data for vqa demo

```
wget https://s3-us-west-2.amazonaws.com/abelikov/data-small.tar.gz
```

unpack
```
tar -xvf data-small.tar.gz
```

to build docker image run

```
docker build docker
```

To start docker with simple examples notebook:  

```
docker run -p8888:8888  -it <image id> /home/relex/opencog-intro-master/notebook.sh 
```

If notebook successully started you should  
be able to open it at localhost:8888

To start vqa demo:

```
docker run -p8888:8888 -v ~/projects/data:/home/relex/projects/data -it <image id> /home/relex/projects/semantic-vision-1/experiments/opencog/pattern_matcher_vqa/vqa
```
