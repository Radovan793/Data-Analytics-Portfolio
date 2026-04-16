# Power BI Report #

## Project Assets ##

Power BI Dashboard: Analysis of Client Basis – Rado.pbix
Business Presentation: Client Base Analysis and Strategic Insights — Radovan Tirol.pdf

### Customer Segmentation & Engagement Analysis ###

## Project Overview ##

- This project analyzes a retail bank’s client base (~10,000 customers) to uncover behavioral patterns, engagement drivers, and growth opportunities.
- The goal was not only to describe the data, but to translate insights into actionable business strategies that improve customer engagement and revenue.

### Key Objectives ###

- Understand customer demographics and distribution
- Analyze segmentation and lifecycle transitions
- Evaluate account ownership vs. engagement
- Identify opportunities for growth and optimization

### Tools & Skills Used ###

- Power BI – dashboarding and visualization
- Excel / CSV analysis – data exploration

### Analytical thinking – turning data into business insights ###

Dataset Includes:

- Customer demographics (age, gender, location)
- Segmentation (MASS, STUDENT, KID)
- Account information (number of accounts, currencies)
- Activity status (active vs inactive)
- Registration history
- Data Structure Note

The dataset was provided as a single denormalized table, where each client appeared once per currency.
To ensure correct customer‑level analysis, all metrics such as activity, segmentation, and registration trends were calculated using DISTINCT client_id.

## Key Insights ##

- Engagement Problem in Core Segment
- MASS segment represents ~72% of customers
- Activity is ~50% active vs inactive

### Insight: The largest and most valuable segment has significant untapped engagement potential. ###

- Product Ownership ≠ Engagement
- Over 60% of customers hold multiple accounts
- Activity levels remain constant (~50%) regardless of account count
  
### Insight: Increasing product ownership alone does not drive user engagement. ### 

- High-Value Behavioral Segment Identified
- Customers with multiple currencies (EUR, USD, CZK, JPY) are likely to be:
- International users
- Higher‑value clients

### Insight: These users represent a high‑value segment for targeted offerings. ### 

- Strong Acquisition, Weak Activation
- Registration spike in 2024
- Activation rate remains stable (~50%)
  
### Insight: Growth in acquisition did not improve engagement, indicating onboarding inefficiencies. ### 

- Strategic Recommendations
- Activate Inactive Users in MASS Segment

#### Focus on: ####

- Targeted campaigns
- Usage incentives
- Re‑engagement strategies

#### Impact: High ROI due to low acquisition cost. ####

- Shift from Cross‑Sell → Engagement Strategy

#### Instead of pushing more products: ####

- Introduce usage‑based incentives
- Focus on customer behavior, not product count

#### Impact: Improves real engagement, not just product adoption. ####

### Target High‑Value Customers ###
#### Prioritize: ####

- Multi‑currency users
- International behavior segments

#### Impact: Higher revenue per user. ####

- Improve Onboarding Experience
- Optimize first‑user journey
- Personalize onboarding by segment

#### Impact: Increase activation rate beyond 50% without extra acquisition spend. ####

## Business Impact ##

### This analysis highlights a key gap: ###
#### The bank is successful at acquiring customers, but not at activating them. ####

By shifting focus from product expansion to customer engagement, the business can unlock significant revenue growth from existing users.

### Project Structure ###

data/          → source dataset (CSV)
sql/           → queries for analysis
dashboard/     → Power BI visuals
presentation/  → final insights

## Key Takeaway ##

- Data analysis is not just about reporting — it is about identifying what drives business value.
- This project demonstrates how data‑driven insights can directly inform strategy and decision‑making.

### Author ###
Radovan Tirol  
Aspiring Data Analyst | SQL • Power BI • Python(learning)
