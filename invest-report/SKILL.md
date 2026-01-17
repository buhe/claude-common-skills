---
name: invest-report
description: Generate comprehensive investment research reports in markdown format. Use when user needs to analyze a company and create an investment research report based on annual report files and reference materials (markdown format) in current folder. The report includes business model analysis, business segments with revenue breakdown, profit sources, ecosystem analysis, capital allocation (dividends, buybacks, investments), profit stability, balance sheet analysis, and DCF valuation.
---

# Investment Research Report Generator

Generate comprehensive investment research reports from a company's annual report and financial data.

## Workflow

1. **Identify company** - Search current folder for annual report files (PDF) and reference materials (markdown) to determine company ticker and name
2. **Extract company info** - Read annual report to extract:
   - Company name and ticker
   - Business model
   - Business segments and revenue breakdown
   - Sources of profit
   - Ecosystem/partners
   - Recent capital allocation activities
   - Profit stability indicators
   - Balance sheet highlights
3. **Get financial data** - Use stockanalysis skill and read reference materials (markdown files in current folder) to fetch:
   - Last 10 years: revenue, net income, operating cash flow, capex, free cash flow
   - Last 10 years: dividend per share, payout ratio, share count
   - Stock price for dividend yield calculation
   - Buyback data for buyback yield calculation
   - Major investments in last 10 years
   - Debt and cash balance
4. **Generate report** - Create markdown file named `{ticker}_investment_report.md` with 8 chapters as specified below

## Report Structure

### Chapter 1: Business Model

Analyze and describe company's core business model based on annual report.

### Chapter 2: Business Segments

List all business segments with their revenue percentages.

### Chapter 3: Sources of Profit

Identify and explain main sources of profit.

### Chapter 4: Ecosystem

Describe company's ecosystem, partnerships, and competitive positioning.

### Chapter 5: Capital Allocation

Capital allocation consists of three aspects: dividends, buybacks, investments

#### Dividends
- Recent year dividend yield = annual total dividend / current stock price
- Recent year payout ratio = annual total dividend / net income

#### Buybacks
- Recent year buyback yield = buyback amount / market cap
- Compare with 5 years ago: did stock compensation versus buybacks cause share count to increase or decrease?

#### Important Investments
Table of major investments in last 10 years:

| Year | Investment | Amount | Purpose |

### Chapter 6: Profit Stability

Analyze profit stability and explain why the company can maintain stable profits based on annual report data.

### Chapter 7: Balance Sheet

#### Debt Analysis
- Analyze debt structure
- Explain how the company would repay debt if it cannot obtain financing (using operating cash flow, asset sales, etc.)

### Chapter 8: Valuation

#### Historical Financial Data Table (Last 10 years, most recent year at top)

Get data from reference materials or use stockanalysis skill:

| Year | Revenue | Net Income | Operating Cash Flow | Capex | Free Cash Flow | Revenue Growth | Net Income Growth | FCF Growth |

#### Future 10-Year Free Cash Flow Growth Estimate

Based on historical data and company analysis, estimate the possible free cash flow growth rate for the next 10 years and justify.

#### DCF Valuation

Use discount rate of 10%. Calculate fair value for 4 scenarios using the same growth rate for the entire 10-year period (no separate terminal growth rate):
- 0% growth rate
- -5% growth rate
- 5% growth rate
- Your estimated growth rate

For each scenario, show:
- Year-by-year cash flow projections (10 years)
- Present value of each year's cash flow
- Total present value of future cash flows
- Less net debt (total debt - cash)
- Equity value
- Fair value per share = equity value / shares outstanding

## Important Notes

- All financial data should be sourced from reference materials (markdown files) in current folder or using stockanalysis skill
- All financial data in tables should use most recent year at top
- Growth rates should be calculated year-over-year
- Justify all assumptions (growth rate, discount rate)
- Report should be written in Chinese
- For DCF valuation, use a single growth rate for the entire 10-year period, not separating into forecast period and terminal value
- Report should be saved as `{ticker}_investment_report.md` in the current folder
- If financial data is needed, use stockanalysis skill
