# Power BI Report – Client Base Analysis

## Project Assets

- Power BI Dashboard: Analysis of Client Base – Rado.pbix  
- Business Presentation: Client Base Analysis and Strategic Insights – Radovan Tirol.pdf  

---

## Customer Segmentation & Engagement Analysis

## Project Overview

This project analyzes a retail bank’s client base (~10,000 customers) to uncover behavioral patterns, engagement drivers, and growth opportunities.

The goal is not only to describe the data, but to translate insights into actionable business strategies that improve customer engagement and revenue.

---

## Key Objectives

- Understand customer demographics and distribution  
- Analyze segmentation and lifecycle transitions  
- Evaluate account ownership vs. engagement  
- Identify opportunities for growth and optimization  

---

## Tools & Skills Used

- Power BI – dashboarding and visualization  
- Excel / CSV analysis – data exploration  
- Analytical thinking – turning data into business insights  

---

## Dataset Overview

The dataset consists of customer demographics, segmentation (MASS, STUDENT, KID), account information, activity status, and registration history.

The data was provided as a **single denormalized table**, where each client appears once per currency.

To ensure correct customer-level analysis, all metrics such as activity, segmentation, and registration trends were calculated using `DISTINCT client_id`.

---

## Key Insights

### Engagement gap in core segment
- MASS segment represents ~72% of customers  
- Activity rate is ~50% (active vs inactive)  

**Insight:** The largest customer segment has significant untapped engagement potential.

---

### Product ownership does not drive engagement
- Over 60% of customers hold multiple accounts  
- Activity remains ~50% regardless of account count  

**Insight:** Increasing product ownership alone does not improve engagement.

---

### High-value behavioral segment identified
- Multi-currency customers (EUR, USD, CZK, JPY)  
- Likely international / higher-value users  

**Insight:** This group represents a premium target segment.

---

### Acquisition vs activation gap
- Strong registration growth in 2024  
- Stable activation rate (~50%)  

**Insight:** Onboarding and activation are not keeping pace with acquisition.

---

## Strategic Recommendations

### Improve engagement in MASS segment
- Targeted campaigns  
- Usage-based incentives  
- Re-engagement strategies  

---

### Shift focus from cross-sell to engagement
- Focus on usage behavior instead of product count  
- Introduce behavioral incentives  

---

### Target high-value users
- Multi-currency customers  
- International segments  

---

### Improve onboarding experience
- Personalize onboarding by segment  
- Optimize first-user journey  

---

## Business Impact

This analysis highlights a key gap:

**The bank is strong in customer acquisition but weak in activation.**

Shifting focus from product expansion to engagement can unlock significant revenue growth from existing customers.

---

## Project Structure

- `data/` – source dataset (CSV)  
- `sql/` – analysis queries  
- `dashboard/` – Power BI visuals  
- `presentation/` – final insights  

---

## Interactive Report

View dashboard:  
https://drive.google.com/file/d/1Kcrl45oRPYYfjjLqX5q0ldD-g_msP3-x/view?usp=drive_link  

---

## Author

Radovan Tirol  
Aspiring Data Analyst | SQL • Power BI • Python (learning)
