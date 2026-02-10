FROM python:3.10-slim
COPY demp.py /
CMD [ "python", "demo.py" ]
# get to your folder using cd an the run "dockedocker build -t virt-demo"
# command meaning
# docker build create image
# 1 docker run "docker run virt-demo"create + start container
# docker start Start existing container
# docker logs see output

