# Use latest Python runtime as image
FROM python:3.6.10-slim

# Set the working directory to /app and copy current dir
RUN mkdir /opt/calc/
WORKDIR /opt/calc/

COPY requirements.txt .
COPY dist/calc /opt/calc/

CMD [ "./calc" ]
#CMD [ "echo", "./calc", ">", "calc_out.txt"]