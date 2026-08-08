# Medical Data Visualizer

A comprehensive data science and visualization project focused on analyzing patient medical examination records. This project cleans, transforms, and visualizes health metrics to identify key risk factors associated with cardiovascular disease.

---

## Overview

Cardiovascular disease is a leading health concern worldwide. This project processes patient health data—including physiological measurements, blood panel results, and personal lifestyle habits—to explore how factors like body mass index (BMI), blood pressure, glucose levels, and cholesterol correlate with cardiac diagnoses.

---

## Key Features & Workflow

* **Data Normalization & Feature Engineering:**
  * Calculated Body Mass Index (BMI) using patient height and weight to create a binary `overweight` indicator (BMI > 25).
  * Normalized blood test indicators (`cholesterol` and `gluc`) so that `0` represents normal/healthy readings and `1` represents elevated/unhealthy readings.
* **Data Cleaning & Outlier Removal:**
  * Filtered out physiological inconsistencies (e.g., cases where diastolic blood pressure exceeded systolic blood pressure).
  * Removed extreme height and weight measurements outside the 2.5th and 97.5th percentiles to eliminate statistical noise.
* **Categorical Feature Visualization:**
  * Reshaped data into long format using `pd.melt()`.
  * Generated side-by-side bar plots (`sns.catplot`) comparing metric counts between patients diagnosed with cardiovascular disease (`cardio = 1`) and those without (`cardio = 0`).
* **Correlation Heatmap Analysis:**
  * Computed a correlation matrix across all numerical attributes.
  * Applied an upper-triangle mask (`np.triu`) to eliminate mirrored redundancy and created an annotated heatmap using Seaborn.

---

## What I Learned & Key Takeaways

Building this project provided hands-on experience in real-world data preprocessing and exploratory data analysis (EDA):

* **Data Reshaping with Pandas:** Mastered reshaping datasets using `pd.melt()` and aggregating metrics with `.groupby()` to prepare datasets for multi-variable plotting.
* **Exploratory Data Analysis (EDA):** Learned how to clean raw datasets by filtering out physical anomalies and statistical outliers using quantiles.
* **Advanced Data Visualization:** Gained practical experience using `Seaborn` and `Matplotlib` to build customized bar charts, multi-panel grids, and masked correlation heatmaps.
* **Automated Testing & Quality Assurance:** Used Python's built-in `unittest` framework to validate data structures, plot dimensions, and feature counts against expected targets.

---

## Key Insights & Conclusions

1. **Impact of Weight & Metabolic Markers:** Patients diagnosed with cardiovascular disease showed noticeably higher rates of high cholesterol, elevated glucose, and overweight status compared to non-diagnosed patients.
2. **Physiological Correlations:** Strong positive correlations exist between height and weight, as well as between systolic (`ap_hi`) and diastolic (`ap_lo`) blood pressure readings.

---

## Tech Stack & Libraries Used

* **Language:** Python 3.8+
* **Data Processing:** `pandas`, `numpy`
* **Data Visualization:** `seaborn`, `matplotlib`
* **Testing Framework:** `unittest`

---

## Project Structure

```text
├── medical_data_visualizer.py  # Primary script containing data transformation and plotting functions
├── medical_examination.csv     # Patient medical examination dataset
├── main.py                     # Entry point script executing visualizer functions and unit tests
├── test_module.py             # Automated unit test suite
├── catplot.png                 # Output: Categorical comparison plot
├── heatmap.png                 # Output: Correlation matrix heatmap
└── README.md                   # Project documentation
