FROM python:3.9


# Install dependencies
RUN python -m pip install --upgrade pip
# tooks very long time
RUN pip install pandas

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
