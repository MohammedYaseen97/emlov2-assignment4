# our base image
FROM python:3.8-slim

# set working directory inside the image
WORKDIR /opt/src

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

# copy the full project inside
COPY . .

# expose the port
EXPOSE 8080

# run the scripted model
ENTRYPOINT ["python3", "src/demo_scripted.py", "ckpt_path=logs/train/runs/2022-10-01_04-48-47/model.script.pt"]