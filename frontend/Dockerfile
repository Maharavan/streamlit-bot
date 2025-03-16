FROM python:latest

WORKDIR /app

COPY . . 

RUN python -m pip install streamlit requests

WORKDIR /app/frontend

CMD ["streamlit","run","streamlit.py"]