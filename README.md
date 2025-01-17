# Virny Software Library

<p align="left">
  <!-- Tests -->
  <a href="https://github.com/DataResponsibly/Virny/actions/workflows/ci.yml">
    <img src="https://github.com/DataResponsibly/Virny/actions/workflows/ci.yml/badge.svg" alt="CI Pipeline">
  </a>
  <!-- Documentation -->
  <a href="https://dataresponsibly.github.io/Virny/">
    <img src="https://img.shields.io/website?label=docs&style=flat-square&url=https://dataresponsibly.github.io/Virny/" alt="documentation">
  </a>
  <!-- PyPI -->
  <a href="https://pypi.org/project/virny">
    <img src="https://img.shields.io/pypi/v/virny.svg?label=release&color=blue&style=flat-square" alt="pypi">
  </a>
  <!-- License -->
  <a href="https://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_(%22BSD_License_2.0%22,_%22Revised_BSD_License%22,_%22New_BSD_License%22,_or_%22Modified_BSD_License%22)">
    <img src="https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square" alt="bsd_3_license">
  </a>
  <!-- Code Size -->
  <a href="">
    <img src="https://img.shields.io/github/languages/code-size/DataResponsibly/Virny.svg" alt="code_size">
  </a>
  <!-- Last Commit -->
  <a href="">
    <img src="https://img.shields.io/github/last-commit/DataResponsibly/Virny.svg" alt="last_commit">
  </a>
</p>


### Note for FAccT24! Because of the anonymous mode, we cannot provide links on our documentation. However, you can go to `docs/examples/` directory in this repo to look at our use case examples.


## 📜 Description

**Virny** serves as a model profiling library, empowering data scientists _to engage in responsible model selection_ and
_to generate a "nutritional label" for an ML model_, which uncovers the model performance across different overall and disparity dimensions. 
The Virny library was developed based on three fundamental principles: 

1) easy extensibility of model analysis capabilities;

2) compatibility to user-defined/custom datasets and model types;

3) simple composition of parity metrics based on the context of use.

Virny decouples model auditing into several stages, including: **subgroup metric computation**, **disparity metric composition**,
and **metric visualization**. This gives data scientists more control and flexibility to use the library
for model development and monitoring post-deployment.

For quickstart, look at our [Use Case Examples](https://dataresponsibly.github.io/Virny/examples/Multiple_Models_Interface_Use_Case/).


## 🛠 Installation

Virny supports **Python 3.8 and 3.9** and can be installed with `pip`:

```bash
pip install virny
```


## 📒 Documentation

* [Introduction](https://dataresponsibly.github.io/Virny/)
* [API Reference](https://dataresponsibly.github.io/Virny/api/overview/)
* [Use Case Examples](https://dataresponsibly.github.io/Virny/examples/Multiple_Models_Interface_Use_Case/)


## 💡 Features

* Entire pipeline for profiling model accuracy, stability, uncertainty, and fairness
* Metric static and interactive visualizations
* Ability to analyze non-binary sensitive attributes and their intersections
* Convenient metric computation interfaces: an interface for multiple models, an interface for multiple test sets, and an interface for saving results into a user-defined database
* An `error_analysis` computation mode to analyze model stability and confidence for correct and incorrect prodictions broken down by groups
* Data loaders with subsampling for popular fair-ML benchmark datasets
* User-friendly parameters input via config yaml files
* Check out [our documentation](https://dataresponsibly.github.io/Virny/) for a comprehensive overview


## 📖 Library Overview

![Virny_Architecture](https://github.com/DataResponsibly/Virny/assets/42843889/91620e0f-11ff-4093-8fb6-c88c90bff711)

The software framework decouples the process of model profiling into several stages, including **subgroup metric computation**,
**disparity metric composition**, and **metric visualization**. This separation empowers data scientists with greater control and
flexibility in employing the library, both during model development and for post-deployment monitoring. The above figure demonstrates
how the library constructs a pipeline for model analysis. Inputs to a user interface are shown in green, pipeline stages are shown in blue,
and the output of each stage is shown in purple.


## 🤗 Affiliations

![NYU-UCU-Logos](https://user-images.githubusercontent.com/42843889/216840888-071bf184-f0e3-4a3e-94dc-c0d1c7784143.png)


## 📝 License

**Virny** is free and open-source software licensed under the [3-clause BSD license](https://github.com/DataResponsibly/Virny/blob/main/LICENSE).
