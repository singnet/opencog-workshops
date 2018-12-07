# opencog-intro
simple examples for opencog

fetch data for vqa demo

wget https://s3-us-west-2.amazonaws.com/abelikov/data-small.tar.gz

to build docker image run

```
docker build docker
```

To start docker with simple examples notebook:  

```
docker run -p8888:8888 -it <image id> /home/relex/opencog-intro-master/notebook.sh 
```

# todo: mount data
