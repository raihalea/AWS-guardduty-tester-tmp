FROM debian
RUN apt-get update && apt-get install -y dnsutils
COPY ./test.sh .
RUN chmod +x test.sh
ENTRYPOINT [ "./test.sh" ]