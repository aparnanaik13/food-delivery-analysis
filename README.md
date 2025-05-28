# 📦 Food Delivery Data Analysis Project

A comprehensive data analysis project focused on understanding the **cost structure**, **profitability**, and **impact of discounts and commissions** in a food delivery business using real-world inspired data.

---

## 📊 Project Overview

This project leverages a dataset of 1000 food delivery orders to:

- Clean and prepare data for analysis  
- Calculate key business metrics (cost, revenue, profit)  
- Visualize cost and profit structures  
- Simulate new commission and discount strategies to enhance profitability  

---

## 🧰 Tools & Libraries Used

- **Python (Pandas, NumPy)** – Data cleaning and transformation  
- **Matplotlib, Seaborn** – Data visualization  
- **Jupyter Notebook** – Interactive analysis  

---

## 📁 Dataset Details

- 1000 orders  
- 12 columns including:  
  - Order & Delivery timestamps  
  - Monetary values (Order Value, Delivery Fee, Payment Fee)  
  - Discounts & Offers  
  - Commission Fees  

---

## 🔧 Data Preparation Steps

- Converted `Order Date and Time` and `Delivery Date and Time` to datetime format  
- Extracted and standardized discount values from varied formats (e.g., `₹50 off`, `10%`)  
- Calculated:  
  - `Discount Percentage`  
  - `Discount Amount`  
  - `Total Costs`, `Revenue`, `Profit` per order  

---

## 💰 Profitability & Cost Analysis

- **Total Revenue, Costs & Profit** calculated  
- Orders with **negative profit identified**  
- Cost Breakdown:  
  - Delivery Fee  
  - Payment Processing Fee  
  - Discount Amount  

### 📉 Key Finding

> 💡 A significant portion of costs comes from **discounts**, heavily impacting profits.

---

## 📊 Visualizations

- 📈 **Profit Distribution** – Shows many orders operate at a loss  
- 🥧 **Cost Proportion Pie Chart** – Discounts dominate cost structure  
- 📊 **Revenue vs Costs vs Profit Bar Chart**

![Total Revenue vs Costs vs Profit](Revenue%20vs%20Costs%20vs%20Profit%20Bar%20Chart.png)

---

## 🧪 Strategy Simulation

### 🔁 Proposed Strategy

- Increase commission to **30%**  
- Limit discounts to **6%**  

### 🔍 Simulated Changes

- New columns:  
  - `Simulated Commission Fee`  
  - `Simulated Discount Amount`  
  - `Simulated Profit`  

- Comparison of **actual vs. simulated** profitability using KDE plot

> (Add comparison plot image link here)

> 📈 Simulation shows significant profit improvement under new strategy.

---

## 📌 Key Insights

- Discounts, while attracting customers, hurt profits the most.  
- Adjusting the **commission-discount balance** can shift operations toward profitability.  
- Data-driven pricing and marketing strategies are vital.  

---

## ✅ Future Improvements

- Integrate time-based trends (e.g., peak hours/days)  
- Add customer segmentation analysis  
- Explore ML models to predict profit/loss per order  

---

## 🚀 Run This Project

```bash
# Clone the repository
git clone https://github.com/yourusername/food-delivery-analysis.git
cd food-delivery-analysis

# Install dependencies
pip install pandas matplotlib seaborn

# Run the analysis
python food-delivery.py
```

---

## 📬 Connect With Me

📧 your.email@example.com  
💼 [LinkedIn](https://www.linkedin.com/in/your-profile)  
📁 [Portfolio](https://your-portfolio-link.com)
