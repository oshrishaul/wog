FROM python:3
ADD MainScores.py /
ADD scores.txt /
CMD [ "python3", "./MainScores.py" ]
