FROM ubuntu:22.04 as build

RUN apt -y update \
    && apt -y install openjdk-17-jdk

CMD echo 'usage:' \
    'BUILD: docker build --network=host -t $(basename $PWD) .' \
    'RUN: docker run -it --rm --network=host --name $(basename $PWD) -v "$PWD":/"$(basename $PWD)" -w /"$(basename $PWD)" $(basename $PWD) bash' \
    'RMI: docker rmi $(basename $PWD) --force'

