FROM python:3
RUN git clone https://github.com/oshrishaul/wog.git
WORKDIR /wog.git
RUN pip install -r requirements.txt
CMD [ "python3", "./MainScores.py" ]