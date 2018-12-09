FROM opencog/vqa

USER relex
RUN wget https://github.com/noskill/opencog-intro/archive/master.zip
RUN unzip master.zip
RUN rm master.zip
RUN chmod +x /home/relex/opencog-intro-master/notebook.sh
RUN cd /home/relex/projects && \
    rm -r semantic-vision-1 && \
    git clone https://github.com/noskill/semantic-vision-1.git && \
    cd semantic-vision-1 && git checkout precomputed-images-demo
