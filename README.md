# MATSim Plans Generator: matsimPlansGenerator (Python)

[![matsimPlansGenerator Homepage](https://img.shields.io/badge/matsimPlansGenerator-develop-orange.svg)](https://github.com/davidvelascogarcia/matsimPlansGenerator/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/matsimPlansGenerator.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/matsimPlansGenerator/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/matsimPlansGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimPlansGenerator)

- [MATSim Plans Generator: matsimPlansGenerator (Python)](#matsim-plans-generator-matsimplansgenerator-python)
  - [Introduction](#introduction)
  - [Running Software](#running-software)
    - [Arguments](#arguments)
  - [Requirements](#requirements)
  - [Status](#status)
  - [Related projects](#related-projects)

## Introduction

`matsimPlansGenerator` is a module in `python` language that automate MATSim simulation planification files generation.

Documentation available on [docs](https://davidvelascogarcia.github.io/matsimPlansGenerator)

## Running Software

1. Run [matsimPlansGenerator.py](./programs).

```bash
python3 matsimPlansGenerator.py
```

### Arguments

Avaliable arguments allowed:

| Argument | Full  | Simple | Description  |
| -------  |  ---  |  ----  | -----------  |
|  Database  |  --database  |  -d  | Input csv database  |
|  Input  |  --input  |  -i  | Input network image  |

## Requirements

`matsimConfigGenerator` requires:

[Install pip3](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)

```bash
pip3 install -r requirements.txt
```

Tested on: `windows 10`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `kubuntu 20.04`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/matsimPlansGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimPlansGenerator)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/matsimPlansGenerator.svg?label=Issues)](https://github.com/davidvelascogarcia/matsimPlansGenerator/issues)

## Related projects

* [davidvelascogarcia: matsimConfigGenerator (Python)](https://github.com/davidvelascogarcia/matsimConfigGenerator)
* [davidvelascogarcia: matsimDataAdapter (Python)](https://github.com/davidvelascogarcia/matsimDataAdapter)
* [davidvelascogarcia: matsimDataGenerator (Python)](https://github.com/davidvelascogarcia/matsimDataGenerator)
* [davidvelascogarcia: matsimNetGenerator (Python)](https://github.com/davidvelascogarcia/matsimNetGenerator)
* [davidvelascogarcia: matsimPlansGenerator (Python)](https://github.com/davidvelascogarcia/matsimPlansGenerator)
* [davidvelascogarcia: matsimVoronoiGenerator (Python)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator)
