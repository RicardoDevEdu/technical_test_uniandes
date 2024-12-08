FROM ubuntu:latest
LABEL authors="josericardo"

ENTRYPOINT ["top", "-b"]