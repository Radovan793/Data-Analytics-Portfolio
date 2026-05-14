# Government Spend Analysis – Power BI Dashboard

A full end-to-end Business Intelligence project analyzing government spending using the State of Connecticut Expenditures dataset.

---

## Project Overview

This dashboard provides a financial and operational view of government payments, vendors, departments, and long-term spending trends.

The project demonstrates:

- Data modeling (Star Schema)
- Power Query transformations
- DAX measures and calculations
- KPI design and business metrics
- Time intelligence (YoY, running totals)
- Vendor and department analysis

---

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

---

## Data Model

### Fact Table
- FactPayments (Amount, Dates, Vendor IDs, Department IDs, etc.)

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

1. **Executive Overview**
   - Total spend, KPIs, trend analysis

2. **Vendor Analysis**
   - Top vendors, concentration, payment distribution

3. **Department Analysis**
   - Spend allocation across departments

4. **Time Intelligence**
   - Monthly trends, YoY comparison, running totals

---

## 🛠 Tools Used

- Power BI Desktop
- Power Query (ETL transformations)
- DAX (Measures & Calculations)
- Excel / CSV data sources
- Star Schema Data Modeling

---

## Key Insights (Summary)

- Government spending is highly concentrated among a small number of vendors
- Departments show uneven budget distribution
- Clear seasonal and long-term growth trends in expenditure
- Payment methods significantly influence total spend distribution

---

## How to Run This Project Locally

This repository uses **Git LFS** to store large Power BI files (`.pbix`).

```bash
git clone https://github.com/Radovan793/Data-Analytics-Portfolio.git
cd Data-Analytics-Portfolio
git lfs install
git lfs pull

Open files:
.pbix → Power BI Desktop
.sql → SQL tools (SSMS, DBeaver, etc.)
.py → VS Code / Python
.pdf / .png → browser or image viewer

## Author

Radovan Tirol
Data Analyst / BI Analyst
