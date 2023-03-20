FROM nginx
RUN apt-get update && apt-get install -y dnsutils
COPY ./test.sh /docker-entrypoint.d/test.sh
RUN chmod +x /docker-entrypoint.d/test.sh
# ENTRYPOINT [ "./test.sh" ]