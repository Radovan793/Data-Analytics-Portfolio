# Government Spend Analysis – Power BI Dashboard

## Project Overview

<<<<<<< HEAD
This is an end-to-end Business Intelligence project analyzing government expenditure using the State of Connecticut dataset.
=======
This dashboard provides a financial, operational, and anomaly detection view of government payments, vendors, departments, and long-term spending behavior.
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))

The goal of this project is to transform raw transactional data into actionable insights about spending patterns, vendor concentration, and departmental budget allocation.

<<<<<<< HEAD
---

## Key Capabilities Demonstrated

- Data modeling using a Star Schema  
- Power Query (ETL transformations)  
- DAX measures and calculations  
- KPI design and business metrics  
- Time intelligence analysis (YoY, running totals)  
- Vendor and department-level analysis  
=======
- Data modeling (Star Schema)
- Power Query transformations
- DAX measures and calculations
- KPI design and business metrics
- Time intelligence (YoY, running totals, rolling trends)
- Vendor and department analysis
- Anomaly detection and outlier analysis
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))

---

## Key KPIs

<<<<<<< HEAD
- Total Spend  
- Number of Transactions  
- Average Payment Amount  
- Largest Single Payment  
- Top Vendor by Spend  
- Spend by Department  
- Monthly and Yearly Trends  
- Year-over-Year (YoY) Growth  
- Running Total Spend  
=======
- Total Spend
- Number of Transactions
- Average Payment Amount
- Largest Single Payment
- Top Vendor by Spend
- Spend by Department
- Monthly & Yearly Trends
- Year-over-Year (YoY) Growth
- Running Total Spend
- Department Anomaly Count (>50M)
- High-Value Transaction Metrics
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))

---

## Data Model

### Fact Table
<<<<<<< HEAD
- Expenditures (amounts, dates, vendor IDs, department IDs, etc.)
=======
- Expenditures (Payment Amount, Date, Vendor Key, Department Key, etc.)
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))

### Dimension Tables
- DimVendor  
- DimDepartment  
- DimProgram  
- DimService  
- DimAccount  
- DimFund  
- DimPaymentMethod  
- DimDate  

---

## Dashboard Pages

### 1. Spend Overview
<<<<<<< HEAD
- Total spend over time  
- Payment method distribution  
- Key KPIs  
- Transaction volume  

### 2. Vendor Analysis
- Top 10 vendors by spend  
- Vendor concentration  
- Spend distribution  

### 3. Department / Program Analysis
- Budget allocation across departments  
- Fiscal year comparison  
- Spend breakdown by program  

### 4. Time Intelligence Analysis
- Monthly trends  
- Year-over-year comparison  
- Running total analysis  
=======
- Total Spend KPIs
- Number of Transactions
- Largest Single Payment
- Spend by Payment Method
- High-level spend trends

---

### 2. Vendor Analysis
- Top 10 Vendors by Spend
- Vendor Concentration (Pareto-style analysis)
- Vendor Spend Distribution
- Slicers for filtering vendor insights
- Payment distribution across vendors

---

### 3. Department / Program Analysis
- Spend allocation across departments
- Department-level breakdown of expenditures
- Fiscal year comparisons across departments
- Program-level spend distribution

---

### 4. Time Intelligence Analysis
- Monthly and yearly spending trends
- Year-over-Year (YoY) comparison by department
- YoY Change and YoY % Change metrics
- Running Total Spend (cumulative analysis)
- Fiscal Year slicer for dynamic time filtering

---

### 5. Financial Distribution & Vendor Composition
- Spend Share by Vendor Type (donut chart)
- Transaction Distribution by Amount Range (histogram / buckets)
- Payment volume analysis by value ranges
- Concentration of transactions across spend bands
- Supporting slicers for segmentation and filtering

---

### 6. Anomaly Detection & Risk Analysis
- Largest Single Payment by Fiscal Year
- Top Anomaly Concentration Table (Vendor, Department, Fiscal Year, Spend)
- Department Anomaly Count (Payments > 50M)
- High-Value Payment Distribution (≥50M histogram)
- Heatmap-style matrix for anomaly concentration
- Fiscal Year slicer for anomaly filtering
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))

---

## Key Insights

- Government spending is highly concentrated among a small number of vendors  
- Departments show uneven budget distribution  
- Clear seasonal and long-term spending trends exist  
- Payment methods significantly affect spend distribution  

---

## Tools Used

<<<<<<< HEAD
- Power BI Desktop  
- Power Query (ETL)  
- DAX (Measures & Calculations)  
- Excel / CSV data sources  
- Star Schema data modeling  

---

## Power BI Report

Download interactive dashboard:  
([https://drive.google.com/file/d/1UXhYtx8PdVvLCuNOeE541IAoQvL3Xnr6/view?usp=drive_link))

---

## Author

Radovan Tirol  
Aspiring Data Analyst | Power BI • SQL • Python
=======
- Government spending is highly concentrated among a small number of vendors
- Departments show uneven budget distribution
- Clear seasonal and long-term growth trends in expenditure
- Payment methods significantly influence total spend distribution
- A small number of departments generate the majority of high-value anomalies
- Extreme payments (>50M) are concentrated in specific fiscal years and agencies
>>>>>>> a3bbbf3 (Final Power BI dashboard update (Pages 1–6))
