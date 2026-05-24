# Government Spend Analysis – Power BI Dashboard

## Project Overview

This is an end-to-end Business Intelligence project analysing government expenditure using the State of Connecticut dataset.
This dashboard provides a financial, operational, and anomaly detection view of government payments, vendors, departments, and long-term spending behaviour.
The goal of this project is to transform raw transactional data into actionable insights about spending patterns, vendor concentration, and departmental budget allocation.

## Key Capabilities Demonstrated

- Data modelling (Star Schema)
- Power Query transformations
- DAX measures and calculations
- KPI design and business metrics
- Time intelligence (YoY, running totals, rolling trends)
- Vendor and department analysis
- Anomaly detection and outlier analysis

## Key KPIs

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

## Data Model

### Fact Table

- Expenditures (Payment, Amount, Date, Vendor Key, Department Key, etc.)

### Dimension Tables

- DimVendor  
- DimDepartment  
- DimProgram  
- DimService  
- DimAccount  
- DimFund  
- DimPaymentMethod  
- DimDate  

## Dashboard Pages

### 1. Spend Overview

- Total spend over time  
- Total Spend (€) by Payment Method  
- Key KPIs  
- Transaction Volume by Amount Range  

### 2. Vendor Analysis
- Top N Vendors by Spend (Dynamic)  
- Vendor Spend Over Time 
- Spend Share by Vendor Type
- KPI

### 3. Department / Program Analysis
- Spend by Department 
- Spend by Department , Program, Service
- YoY Spend Comparison by Department
- Spend by Fiscal Year and Department

### 4. Time Intelligence Analysis
- Monthly spending trend
- Year-over-Year (YoY) comparison by department
- YoY Change and YoY % Change metrics
- Running Total Spend (cumulative analysis)
- Fiscal Year slicer for dynamic time filtering

### 5. Financial Distribution & Vendor Composition
- Spend Share by Vendor Type (donut chart)
- Transaction Distribution by Amount Range (histogram / buckets)
- Payment volume analysis by value ranges
- Concentration of transactions across spend bands
- Supporting slicers for segmentation and filtering

### 6. Anomaly Detection & Risk Analysis
- Largest Single Payment by Fiscal Year
- Top Anomaly Concentration Table (Vendor, Department, Fiscal Year, Spend)
- Department Anomaly Count (Payments > 50M)
- High-Value Payment Distribution (≥50M histogram)
- Heatmap-style matrix for anomaly concentration
- Fiscal Year slicer for anomaly filtering

## Key Insights

- Government spending is highly concentrated among a small number of vendors  
- Departments show uneven budget distribution  
- Clear seasonal and long-term spending trends exist  
- Payment methods significantly affect spend distribution  

## Tools Used

- Power BI Desktop  
- Power Query (ETL)  
- DAX (Measures & Calculations)  
- Excel / CSV data sources  
- Star Schema data modeling  

## Power BI Report

Download interactive dashboard:  
([https://drive.google.com/file/d/1UXhYtx8PdVvLCuNOeE541IAoQvL3Xnr6/view?usp=drive_link))

## Author

Radovan Tirol  
Aspiring Data Analyst | Power BI • SQL • Python

- Government spending is highly concentrated among a small number of vendors
- Departments show uneven budget distribution
- Clear seasonal and long-term growth trends in expenditure
- Payment methods significantly influence total spend distribution
- A small number of departments generate the majority of high-value anomalies
- Extreme payments (>50M) are concentrated in specific fiscal years and agencies

