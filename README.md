<div align="center">

# EMLO 2.0 Assignment 3

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

In this assignment, we add DVC support to the repo, and conduct hyperparameter sweep using optuna.

## How to run

Install dependencies

```bash
# clone project
git clone https://github.com/MohammedYaseen97/emlo-2.0-assignment-2
cd emlo-2.0-assignment-2

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

To run the container in interactive mode, use:

```bash
docker run -it --volume `pwd`:/app ace47/emlo-2.0:session02 ubuntu bash
```

You can also just run the train and eval scripts:

```bash
docker run --volume `pwd`:/app ace47/emlo-2.0:session02 python src/train.py
```

```bash
docker run --volume `pwd`:/app ace47/emlo-2.0:session02 python src/eval.py ckpt_path=logs/train/runs/2022-09-12_15-47-43/checkpoints/epoch_001.ckpt
```

We mount the volume instead of copying all the files inside the docker while building so as to examine the system's performance inside docker with real time changes. 
