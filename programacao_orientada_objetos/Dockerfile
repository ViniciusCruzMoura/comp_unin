FROM ubuntu:22.04 as build

RUN apt -y update \
    && apt -y install openjdk-17-jdk
#RUN apt -y update \
#    && apt -y install openjdk-8-jdk \
#        maven \
#    && apt -y remove openjdk-11-jre-headless

#RUN mkdir -p /root/.m2
#COPY settings.xml /root/.m2/

CMD echo 'usage:' \
    'BUILD: docker build --network=host -t $(basename $PWD) .' \
    'RUN: docker run -it --rm --network=host --name $(basename $PWD) -v "$PWD":/"$(basename $PWD)" -w /"$(basename $PWD)" $(basename $PWD) bash' \
    'RMI: docker rmi $(basename $PWD) --force'

