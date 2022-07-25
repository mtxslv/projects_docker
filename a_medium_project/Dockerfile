FROM python:3.10
RUN python -m pip install fastapi
RUN python -m pip install uvicorn
ADD ./main.py .
ARG PORT_MEDIUM_DOCKER=9876
ENV PORT_UVICORN=$PORT_MEDIUM_DOCKER
EXPOSE $PORT_MEDIUM_DOCKER
CMD uvicorn main:app --host 0.0.0.0 --port $PORT_UVICORN