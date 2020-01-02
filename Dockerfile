FROM python:3
ADD MainScores.py /
ADD scores.txt /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python3", "./MainScores.py" ]