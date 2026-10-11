# Quantium Software Engineering Job Simulation

This project was completed as part of the Quantium Software Engineering Job Simulation on Forage.

## Project Overview

The project focuses on processing sales data for Pink Morsel products and building an interactive dashboard to visualize sales trends across different regions.

## Technologies Used

- Python
- Pandas
- Plotly
- Dash
- Git and GitHub

## Tasks Completed

### 1. Data Processing
- Read and processed sales data from CSV files.
- Filtered data for Pink Morsel products.
- Cleaned price values and calculated sales.
- Combined processed data into a single CSV file.

### 2. Interactive Dashboard
- Created a dashboard using Dash and Plotly.
- Visualized sales trends over time.
- Added a region filter.
- Highlighted the price increase date on the chart.

### 3. Testing
The repository includes test files and a script for running tests.

## Project Structure

```text
quantium-starter-repo/
├── data/
├── tests/
├── app.py
├── process_data.py
├── formatted_output.csv
├── run_tests.sh
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Mahek-J21/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pandas plotly dash
```

### 4. Process the data

```bash
python process_data.py
```

### 5. Run the dashboard

```bash
python app.py
```

Open the local URL displayed in the terminal to view the dashboard.

## Learning Outcomes

- Data cleaning and preprocessing using Pandas.
- Working with CSV files.
- Building interactive dashboards using Dash and Plotly.
- Using Git and GitHub for version control.
- Understanding software testing workflows.

## Acknowledgement

Completed as part of the Quantium Software Engineering Job Simulation offered through Forage, using the provided starter repository.
