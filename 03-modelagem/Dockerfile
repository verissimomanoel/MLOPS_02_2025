FROM amazonlinux:latest

LABEL maintainer="Manoel Verissimo"

RUN yum update -y \
    && yum install -y \
    gcc gcc-c++ freetype-devel yum-utils findutils openssl-devel \
    && yum clean all

ARG RELEASEVER=latest
RUN dnf update -y --releasever ${RELEASEVER} && \
    dnf install -y --releasever ${RELEASEVER} python3.12 python3.12-pip && \
    dnf clean packages

RUN ln -s /usr/bin/python3.12 /usr/bin/python
RUN ln -s /usr/bin/pip-3.12 /usr/bin/pip

WORKDIR /opt/app

COPY requirements.txt start_server.sh /opt/app/
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R root:root /opt/app
RUN chmod -R 777 /opt/app

EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/app/start_server.sh"]