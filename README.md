# Research on Predicting YouBike Station Depletion Timing Using Deep Learning Techniques
> 利用深度學習技術在 YouBike 借罄時點預測的研究 <br>
> This project was supported by Taiwan’s National Science and Technology Council (NSTC) undergraduate research program.

## Overview
This project predicts YouBike station availability using GNN and LSTM models.

## Project Goal
To predict YouBike station availability in real time and help users avoid arriving at empty stations.

## The workflow includes:
- Real-time data collection
- Time-series preprocessing
- Graph-structured modeling
- GNN-LSTM forecasting

## Model Architecture

![Model Architecture](images/model_architecture.png)

## Tech Stack
- Python
- TensorFlow
- BeautifulSoup
- Pandas
- NumPy

## Features
- Automated real-time data collection
- Data preprocessing for time-series analysis
- Constructed graph-based spatial representations of YouBike stations for GNN modeling
- Deep learning forecasting framework

## Repository Structure
```text
youbike-demand-forecasting/
├── README.md
├── images/
│   ├── model_architecture.png
│   ├── prediction_result.png
├── src/
│   ├── data_collection.py
│   ├── data_processing.py
│   └── model_training.py
├── .gitignore
```
