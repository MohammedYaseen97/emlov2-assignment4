<div align="center">

# EMLO 2.0 Assignment 4

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

In this assignment, we deploy using gradio and optimise runs using torchscript.

## How to run

Install dependencies

```bash
# clone project
git clone https://github.com/MohammedYaseen97/emlo-2.0-assignment-4
cd emlo-2.0-assignment-4

# [OPTIONAL] create conda environment
conda create -n myenv python=3.8
conda activate myenv

# install pytorch according to instructions
# https://pytorch.org/get-started/

# install requirements
pip install -r requirements.txt
```

Train model with default configuration

```bash
# train on CPU
python src/train.py trainer=cpu

# train on GPU
python src/train.py trainer=gpu
```

Train model with chosen experiment configuration from [configs/experiment/](configs/experiment/)

```bash
python src/train.py experiment=experiment_name.yaml
```

You can override any parameter from command line like this

```bash
python src/train.py trainer.max_epochs=20 datamodule.batch_size=64
```

You can test it on any combination of hyperparameters 

```bash
python src/train.py -m hparams_search=cifar_optuna experiment=cifar
```

## Docker Support

Docker support has been added to the [Makefile](Makefile).

To build the docker container, use:

```bash
make build
```

This build also exists on [dockerhub](hub.docker.com)

To run the container, use:

```bash
docker run -p 8080:8080 -t ace47/emlo-2.0:session04
``` 

To run the demo which uses torchscript, make and run the docker file as above. Alternatively, run it in your local using:

```bash
python3 src/demo_scripted.py ckpt_path=logs/train/runs/2022-10-01_04-48-47/model.script.pt
```