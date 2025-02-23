# JORLDY (Beta)

[![license badge](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)

Hello Wo**RL**d!!:hand:  **Join Our Reinforcement Learning framework for Developing Yours (JORLDY)** is an open-source Reinforcement Learning (RL) framework provided by [KakaoEnterprise](https://www.kakaoenterprise.com/). It is named after Jordy, one of the [Kakao Niniz](https://www.kakaocorp.com/page/service/service/Niniz) character. It provides various RL algorithms and environment and they can be easily used using single code. This repository is opened for helping RL researchers and students who study RL.


## :fire: Features

- 20+ RL Algorithms and various RL environment are provided
- Algorithms and environment are customizable
- New algorithms and environment can be added 
- Distributed RL algorithms are provided using [ray](https://github.com/ray-project/ray)
- Benchmark of the algorithms is conducted in many RL environment

## :heavy_check_mark: Tested

| Python |   Windows   |   Mac   |   Linux  |
| :----: | :---------: | :-----: | :------: |
|  3.8  | :heavy_check_mark: | :heavy_check_mark: | WSL, Ubuntu 18.04 |

## :arrow_down: Installation

```
git clone https://github.com/kakaoenterprise/JORLDY.git  
cd JORLDY
pip install -r requirements.txt

# linux
apt-get update 
apt-get -y install libgl1-mesa-glx # for opencv
apt-get -y install libglib2.0-0    # for opencv
apt-get -y install gifsicle        # for gif optimize
```

__:whale: To use docker__

(customize if necessary)
```
cd JORLDY

# mac, linux
docker build -t jorldy -f ./docker/Dockerfile .
docker run -it --rm --name jorldy -v `pwd`:/JORLDY jorldy /bin/bash

# windows
docker build -t jorldy -f .\docker\Dockerfile .
docker run -it --rm --name jorldy -v %cd%:/JORLDY jorldy /bin/bash
```

__:heavy_plus_sign: To use additional environments__

(atari and super-mario-bros need to be installed manually due to licensing issues)
```
# To use atari
pip install --upgrade gym[atari,accept-rom-license]
 
# To use super-mario-bros
pip install gym-super-mario-bros
```

## :rocket: Getting started

```
cd jorldy

# Examples: python [script name] --config [config path]
python single_train.py --config config.dqn.cartpole
python single_train.py --config config.rainbow.atari --env.name assault

# Examples: python [script name] --config [config path] --[optional parameter key] [parameter value]
python single_train.py --config config.dqn.cartpole --agent.batch_size 64
python sync_distributed_train.py --config config.ppo.cartpole --train.num_workers 8 

```

## :card_index_dividers: Release 

| Version |   Release Date   |   Source   |   Release Note  |
| :-----: | :--------------: | :--------: | :----------: |
|  0.0.3  | November 23, 2021 | [Source](https://github.com/kakaoenterprise/JORLDY/tree/v0.0.3) | [Release Note](https://github.com/kakaoenterprise/JORLDY/releases/tag/v0.0.3) |
|  0.0.2  | November 06, 2021 | [Source](https://github.com/kakaoenterprise/JORLDY/tree/v0.0.2) | [Release Note](https://github.com/kakaoenterprise/JORLDY/releases/tag/v0.0.2) |
|  0.0.1  | November 03, 2021 | [Source](https://github.com/kakaoenterprise/JORLDY/tree/v0.0.1) | [Release Note](https://github.com/kakaoenterprise/JORLDY/releases/tag/v0.0.1) |


## :mag: How to

- [How to use](./docs/How_to_use.md)
- [How to customize config](./jorldy/config/README.md)
- [How to customize agent](./jorldy/core/agent/README.md)
- [How to customize environment](./jorldy/core/env/README.md)
- [How to customize network](./jorldy/core/network/README.md)
- [How to customize buffer](./jorldy/core/buffer/README.md)


## :page_facing_up: Documentation

- [Distributed Architecture](./docs/Distributed_Architecture.md)
- [Role of Managers](./jorldy/manager/README.md)
- [List of Contents](./docs/List_of_Contents.md)
- [Naming Convention](./docs/Naming_convention.md)
- [Benchmark](https://kepnex.notion.site/Benchmark-e20f16b4d4f84b83b490edef13226658)
- [Reference](./docs/Reference.md)


## :busts_in_silhouette: Contributors

:mailbox: Contact: jorldy@kakaoenterprise.com

<img src="./resrc/contributors.png" alt="contributors" width=80%/> 


## :copyright: License

[Apache License 2.0](./LICENSE.md)

## :no_entry_sign: Disclaimer

Installing in JORDY and/or utilizing algorithms or environments not provided KEP may involve a use of third party’s intellectual property. It is advisable that a user obtain licenses or permissions from the right holder(s), if necessary, or take any other necessary measures to avoid infringement or misappropriation of third party’s intellectual property rights.
