FROM ubuntu

LABEL Elaine Grenot Castellano

WORKDIR /root

RUN  echo "**** Instalando Python y otras herramientas ****" && \
     apt-get -y update && \
     apt-get install -yq curl nano unzip pip python3

RUN  pip install plotly.express pandas

ADD  bd_dengue.sh /root/bd_dengue.sh

ADD  casos_dengue.py /root/casos_dengue.py

RUN  bash bd_dengue.sh

RUN  python3 casos_dengue.py

CMD ["bash"]
