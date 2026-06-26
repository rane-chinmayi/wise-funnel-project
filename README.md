# Wise Onboarding Funnel Analysis

A product analytics case study diagnosing drop-off in Wise's 
onboarding and KYC verification flow.

## Summary
Identified KYC ID submission as the primary drop-off point 
(32.9% abandonment) across a 10,000-user simulated dataset, 
and designed a data-backed A/B experiment targeting a 7-point 
lift in verification completion rate.

## Tools
- Python (pandas, numpy) — data generation
- SQLite + DB Browser — funnel analysis
- Looker Studio — dashboard visualisation

## Files
- `data/generate_data.py` — generates 10,000-user dataset
- `data/sample_size.py` — calculates A/B test sample size
- `sql-results/` — screenshots of all 5 SQL query results
- `screenshots/` — Wise onboarding flow documentation

## Full Case Study
[View on Notion](https://app.notion.com/p/Diagnosing-and-Fixing-Wise-s-KYC-Drop-Off-A-Funnel-Analysis-38bc82f6c8a880ecb5b6f75acebd4e2b?source=copy_link)

