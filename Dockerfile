FROM quay.io/moredread/calibre:latest
MAINTAINER code@andre-bubel.de

USER root

RUN mkdir /news
ADD fetch_news.sh /news
RUN chown user:user /news -R

USER user

CMD /news/fetch_news.sh
