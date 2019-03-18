#
# Docker file that builds RelEx and visual question answering pipeline.
#
# To start:
#    docker run -it -p 8888:8888 vqa
#
# To demo:
#    open in browser localhost:8888
#    use password: password 
#
# That will open jupyter notebook with vqa demo
#
FROM ubuntu:18.04
# use bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# Avoid triggering apt-get dialogs (which may lead to errors). See:
# https://stackoverflow.com/questions/25019183/docker-java7-install-fail
ENV DEBIAN_FRONTEND noninteractive

ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64

RUN apt-get update ; apt-get -y upgrade ; apt-get -y autoclean

# Java
RUN apt-get -y install maven screen telnet netcat-openbsd byobu \
                       wget vim git unzip sudo apt-utils

RUN apt-get -y install openjdk-11-jdk

# GCC and basic build tools
RUN apt-get -y install gcc g++ make swig ant

# Wordnet
RUN apt-get -y install wordnet wordnet-dev wordnet-sense-index

# There are UTF8 chars in the Java sources, and the RelEx build will
# break if build in a C environment.
RUN apt-get -y install locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /usr/local/share/java

WORKDIR /home/Downloads/

# guile
RUN apt install -y guile-2.2
# build tools
RUN apt install -y libboost-python-dev libblas-dev libboost-thread-dev libboost-filesystem-dev libboost-system-dev
RUN apt install -y cmake libboost-program-options-dev libboost-regex-dev libiberty-dev guile-2.2-dev protobuf-compiler uuid-dev

# Conda
# install conda 

RUN apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1

# Create and switch user. The user is privileged, with no password
# required.  That is, you can use sudo.
RUN adduser --disabled-password --gecos "ReLex USER" relex
RUN adduser relex sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER relex

RUN sudo chown -R relex:relex .
RUN sudo chown -R relex:relex /home/relex 
# Punch out ports
## plain-text-server.sh port
EXPOSE 3333
## opencog-server.sh port
EXPOSE 4444
## link-grammar-server.sh port
EXPOSE 9000

WORKDIR /home/relex

# Link Parser -- changes often
# Download the current released version of link-grammar.
# The wget gets the latest version w/ wildcard

RUN wget -r --no-parent -nH --cut-dirs=2 https://www.abisource.com/downloads/link-grammar/current/
RUN tar -zxf current/link-grammar-5*.tar.gz
# get linkgrammar version
RUN bash -l -c 'echo `ls|grep link|sed 's/link-grammar-//g'` >> LINKGRAMMAR_VERSION'

USER root

RUN cd link-grammar-5.*/; ./configure; make -j6; sudo make install; \
    ldconfig;

USER relex
RUN cd link-grammar-5.*/; mvn install:install-file \
    -Dfile=./bindings/java/linkgrammar-`cat ../LINKGRAMMAR_VERSION`.jar \
    -DgroupId=org.opencog \
    -DartifactId=linkgrammar \
    -Dversion=`cat ../LINKGRAMMAR_VERSION` \
    -Dpackaging=jar

USER root
RUN rm -rf /home/relex/link-grammar*
RUN rm -rf /home/relex/current

USER relex

# Relex -- changes often
RUN wget https://github.com/opencog/relex/archive/master.tar.gz -O master.tar.gz
RUN tar -xvf master.tar.gz; cd relex-master; mvn install



RUN echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib/" >> /home/relex/.profile
RUN echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/home/relex/miniconda3/envs/demo/lib/" >> /home/relex/.profile

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b && \
    rm ~/anaconda.sh

RUN /home/relex/miniconda3/bin/conda create -y --name demo python=3.5 && \
source /home/relex/miniconda3/bin/activate demo && \
    conda install -y cython cytoolz pip jupyter && \
    conda install -c pytorch pytorch && \
    conda install -y -c conda-forge jpype1 && pip install easydict ipywebrtc

user root
RUN apt install -y postgresql-server-dev-10 cython
user relex 

# vqa piplie(java)
RUN wget https://github.com/singnet/semantic-vision/archive/master.zip

RUN unzip master.zip

RUN rm master.zip

RUN mkdir ~/projects

RUN mv semantic-vision-master/ ~/projects/semantic-vision-1

ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64" >> /home/relex/.profile

USER relex 

# cogutil
RUN wget https://github.com/singnet/cogutil/archive/master.zip
RUN unzip master.zip && cd cogutil-master/ && mkdir build &&  cd build && cmake ..
RUN cd cogutil-master/build && sudo make install
RUN sudo rm -rf cogutil-master master.zip

# atomspace


RUN wget https://github.com/singnet/atomspace/archive/master.zip
RUN unzip master.zip 
RUN source /home/relex/miniconda3/bin/activate demo && cd atomspace-master && mkdir build && cd build/ && cmake .. && make
run cd atomspace-master/build && sudo make install
RUN sudo rm -rf atomspace-master/build master.zip
RUN mv atomspace-master /home/relex/projects/atomspace

# opencog


RUN wget https://github.com/singnet/opencog/archive/master.zip
RUN unzip master.zip
RUN source /home/relex/miniconda3/bin/activate demo && cd opencog-master && mkdir build && cd build/ && cmake .. && make
RUN cd opencog-master/build && sudo make install
RUN sudo rm -rf opencog-master/build master.zip
RUN mv opencog-master /home/relex/projects/opencog

RUN echo "export GUILE_AUTO_COMPILE=0" >> /home/relex/.profile

RUN echo "(use-modules (ice-9 readline)) (activate-readline)\ 
(add-to-load-path \"/usr/local/share/opencog/scm\")\
(add-to-load-path \"/home/relex/projects/opencog/examples/pln/conjunction/\")\
(add-to-load-path \"/home/relex/projects/atomspace/examples/rule-engine/rules/\")\
(add-to-load-path \"/home/relex/projects/opencog/opencog/pln/rules/\")\
(add-to-load-path \".\")\
(use-modules (opencog))\
(use-modules (opencog query))\
(use-modules (opencog exec))" >> /home/relex/.guile

RUN echo "export PYTHONPATH=\$PYTHONPATH:/usr/local/lib/python3.5/dist-packages/" >> /home/relex/.profile
RUN echo "export PYTHONPATH=\$PYTHONPATH:/usr/local/lib/python3/dist-packages/" >> /home/relex/.profile

RUN source /home/relex/miniconda3/bin/activate demo && jupyter notebook --generate-config 

RUN echo "c.NotebookApp.password = 'sha1:b6e570f197d6:b920933b262cf450f5c11dc21d878c53972cb2fa'" >> /home/relex/.jupyter/jupyter_notebook_config.py

RUN echo "c.NotebookApp.password_required = False" >> /home/relex/.jupyter/jupyter_notebook_config.py

RUN echo "c.NotebookApp.port = 8888" >> /home/relex/.jupyter/jupyter_notebook_config.py

#RUN chmod +x /home/relex/projects/semantic-vision-1/experiments/opencog/pattern_matcher_vqa/vqa
RUN wget https://github.com/noskill/opencog-intro/archive/master.zip && unzip master.zip && rm master.zip
RUN chmod +x /home/relex/opencog-intro-master/notebook.sh
user root
# cleanup
RUN apt-get -y remove gcc g++ make swig ant
RUN apt-get remove -y postgresql-server-dev-10
RUN apt-get -y autoclean
RUN rm -r /home/relex/miniconda3/pkgs/*
# build tools
RUN apt autoremove -y
RUN apt remove -y libboost-python-dev libblas-dev libboost-thread-dev libboost-filesystem-dev libboost-system-dev
RUN apt remove -y cmake libboost-program-options-dev libboost-regex-dev libiberty-dev guile-2.2-dev protobuf-compiler uuid-dev

RUN rm /home/relex/miniconda3/envs/demo/lib/libQt5*

user relex

CMD /home/relex/projects/semantic-vision-1/experiments/opencog/pattern_matcher_vqa/vqa
