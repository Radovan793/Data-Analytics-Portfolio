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
- Expenditures (Amount, Dates, Vendor IDs, Department IDs, etc.)

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

1. **Spend Overview**
   - Total spend over Time, Total spend by Payment Method, Number Of Transactions, KPIs, 

2. **Vendor Analysis**
   - Top 10 vendors by spend, Top N vendors, Slicers, Concentration, Payment distribution

3. **Department / Program Analysis**
   - Spend allocation across departments, Spend by Fiscal Year across Department

4. **Time Intelligence Analysis**
   - Monthly trends, YoY comparison, Running totals

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

## Power BI File

Download the interactive Power BI dashboard (.pbix):
[Download PBIX File](https://drive.google.com/file/d/1ELAZ2bCRYgWcV1vWUgnTh4AvRh3SDR_g/view?usp=drive_link)

**Author**

Radovan Tirol
Data Analyst / BI Analyst
