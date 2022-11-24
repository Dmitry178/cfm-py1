FROM python:3.10-slim
COPY ./main.py ./main.py
COPY ./my_bill.py ./my_bill.py
COPY ./victory.py ./victory.py
CMD python ./main.py
