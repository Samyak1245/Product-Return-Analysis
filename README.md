# 📊 Product Return Analysis System

A Python-based Data Analytics and Visualization mini-project that analyzes retail product returns, identifies common return reasons, and examines whether return rates differ across product categories using statistical hypothesis testing.

## 🌐 Live Project Link

https://prduct-return-analysis-a4knmfprmpgxndqhhrvzb8.streamlit.app/

## 📌 Project Overview

Retail companies often face challenges understanding why customers return products and which product categories experience higher return rates. This project uses Python to analyze retail transaction data, identify patterns in product returns, and visualize insights through an interactive dashboard.

The system helps users understand return trends, investigate customer complaints, and make data-driven decisions to improve product quality and customer satisfaction.

## 🎯 Objectives

* Analyze product returns across different product categories.
* Identify the most common reasons for product returns.
* Calculate overall and category-wise return rates.
* Analyze customer complaints associated with returned products.
* Apply statistical hypothesis testing to examine the relationship between product category and return status.
* Visualize insights through interactive charts and graphs.
* Support data-driven decisions to reduce product returns.

## 🛠️ Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core programming language      |
| Pandas     | Data cleaning and analysis     |
| NumPy      | Numerical computations         |
| Matplotlib | Data visualization             |
| Seaborn    | Statistical visualization      |
| SciPy      | Statistical hypothesis testing |
| Streamlit  | Interactive dashboard          |
| CSV        | Dataset storage                |

## ✨ Features

### 1. Product Return Analysis

Calculates total orders, returned orders, and the overall return rate.

### 2. Category-Wise Analysis

Compares return rates across product categories such as Electronics, Clothing, Grocery, and Furniture.

### 3. Return Reason Analysis

Identifies common reasons for product returns, including damaged products, wrong products, size issues, and poor quality.

### 4. Statistical Hypothesis Testing

Uses the Chi-square test of independence to examine whether product category and return status are associated.

**Hypotheses:**

* **Null Hypothesis (H₀):** Product category and return status are independent.
* **Alternative Hypothesis (H₁):** Product category and return status are associated.

A significance level of 0.05 is used to interpret the test results.

### 5. Interactive Dashboard

Provides a Streamlit dashboard with summary metrics, category filters, return-rate charts, return-reason analysis, and transaction data.

### 6. Data Visualization

Uses bar charts and other visualizations to make return patterns easier to understand.

## 📁 Project Structure

```text
Product-Return-Analysis/
│
├── app.py
├── analysis.py
├── product_returns.csv
├── requirements.txt
└── README.md
```

| File                  | Description                           |
| --------------------- | ------------------------------------- |
| `app.py`              | Streamlit dashboard                   |
| `analysis.py`         | Data analysis and statistical testing |
| `product_returns.csv` | Retail transaction dataset            |
| `requirements.txt`    | Required Python libraries             |
| `README.md`           | Project documentation                 |

## 📋 Dataset Description

The dataset contains sample retail transaction records with the following fields:

| Column           | Description                                         |
| ---------------- | --------------------------------------------------- |
| Order_ID         | Unique order identifier                             |
| Product_Category | Category of the purchased product                   |
| Price            | Product price                                       |
| Return_Status    | Indicates whether the order was returned            |
| Return_Reason    | Reason for returning the product                    |
| Complaint        | Indicates whether a customer complaint was recorded |
| Order_Date       | Date of the order                                   |

**Note:** The included dataset contains illustrative sample records for demonstration purposes. Results should not be interpreted as actual retail industry findings.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.9 or later
* pip package manager
* Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shamik-Modak/Product-Return-Analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Product-Return-Analysis
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Dashboard

```bash
python -m streamlit run app.py
```

### Step 5: Open the Application

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📦 Requirements

The `requirements.txt` file should contain:

```text
streamlit
pandas
numpy
matplotlib
seaborn
scipy
openpyxl
```

## 📈 Analysis and Expected Outcomes

The system is designed to help answer the following questions:

* Which product category has the highest return rate?
* What are the most frequent reasons for product returns?
* How many orders have associated customer complaints?
* How do return rates vary across product categories?
* Is there statistical evidence of an association between product category and return status?

The results depend on the dataset provided. The system can be extended to analyze larger retail datasets for more reliable insights.

## 🔬 Statistical Methodology

The Chi-square test of independence is used to investigate whether product category and return status are associated.

The significance level is set to:

**α = 0.05**

* If the p-value is less than 0.05, reject the null hypothesis.
* If the p-value is greater than or equal to 0.05, fail to reject the null hypothesis.

The test indicates an association, if supported by the data, but does not establish causation or prove that every category has a significantly higher return rate than every other category.

## 🚀 Future Enhancements

* Sentiment analysis of customer complaint descriptions.
* Monthly and seasonal return trend analysis.
* Machine learning models to predict return probability.
* Exportable reports in Excel and PDF formats.
* Support for uploading custom CSV datasets.
* Advanced dashboards with additional filters.
* Recommendations for improving product quality and reducing returns.

## 🎓 Applications

* Retail analytics
* Customer behavior analysis
* Product quality monitoring
* Business intelligence
* Data-driven decision-making

## 👨‍💻 Author

**Shamik Modak**

GitHub: [Shamik-Modak](https://github.com/Shamik-Modak)

## 📄 License

This project is developed for educational and academic purposes. You may add an open-source license if you intend to permit others to reuse or modify the code.

---

⭐ If you find this project useful, consider starring the repository.
