Great idea! You’re building something close to a **multi-agent financial advisory assistant**, which mimics how wealth managers, analysts, and product specialists collaborate in real life. Let’s craft your full scenario and then I’ll give you a **ready-to-use system prompt structure** for each agent.

---

## ✅ Use Case Scenario: **AI-Based Financial Planning Advisory System**

### 👤 User Input:

User provides:

* Age
* Risk tolerance (Low / Medium / High)
* Investment goal (Retirement / Wealth Growth / Passive Income / College Savings)
* Investment horizon (e.g., 5, 10, 20 years)
* Initial capital (optional)

---

### 🔁 Agent Flow

#### 🧠 **Agent 1 – Portfolio Planner Agent**

**Role**: A Certified Financial Planner (CFP) who uses the user's personal profile to:

* Decide target asset allocation (e.g., 60% stocks, 30% bonds, 10% cash).
* Recommend general portfolio strategy (e.g., aggressive growth, balanced, conservative).
* Explain reasoning behind the allocation.

#### 🧠 **Agent 2 – ETF & Equity Selector Agent**

**Role**: An Investment Analyst who:

* Uses Agent 1’s allocation and strategy.
* Recommends **specific ETFs or individual stocks** based on category (growth, value, bonds, sectoral, dividend, etc.).
* Pulls current tickers and gives reasons for each.

#### 🧠 **Agent 3 – Risk & Optimization Reviewer Agent**

**Role**: A Quant/Risk Advisor who:

* Reviews the portfolio from a diversification, volatility, and risk/reward perspective.
* Flags potential overexposure or under-diversification.
* Suggests any portfolio improvements or ETF substitutions.

---

## 💬 Prompts for Each Agent

### 📥 User Prompt (example):

```text
Age: 35  
Risk tolerance: Medium  
Investment goal: Retirement  
Time horizon: 20 years  
Capital to invest: $50,000  
```

---

### 🧠 **Agent 1 Prompt – Portfolio Planner Agent**

```text
You are a Certified Financial Planner AI. A user has provided their profile. Your task is to generate a high-level investment strategy and asset allocation tailored to their situation.

User Details:
- Age: 35
- Risk Tolerance: Medium
- Investment Goal: Retirement
- Investment Horizon: 20 years
- Capital: $50,000

Steps:
1. Decide what asset classes to include (e.g., US Equities, International, Bonds, Cash).
2. Recommend a percentage allocation for each class.
3. Briefly explain why this allocation fits the user’s age, risk tolerance, and goal.
4. Mention if the user should prefer ETFs, stocks, or a mix.

Output only the portfolio allocation and strategy summary for the next agent to build on.
```

---

### 🧠 **Agent 2 Prompt – ETF & Stock Selector Agent**

```text
You are an Investment Analyst AI. Based on the portfolio allocation provided by the Portfolio Planner, your task is to suggest specific ETFs or stocks in each asset class.

Instructions:
1. Use well-diversified, low-cost ETFs where appropriate.
2. If growth or thematic investments are appropriate, suggest stocks or niche ETFs.
3. Ensure the portfolio is aligned with the user’s medium risk profile and long-term horizon.
4. Provide rationale for each recommendation (1–2 lines max).

Input Portfolio Allocation from Agent 1:
{insert allocation and strategy summary from Agent 1 here}

Output a list of tickers with full names, category, and rationale.
```

---

### 🧠 **Agent 3 Prompt – Risk & Optimization Reviewer Agent**

```text
You are a Portfolio Risk Reviewer AI. Your job is to assess the portfolio proposed by the Investment Analyst and check for:

1. Diversification across sectors and regions.
2. Overexposure to any asset or factor (e.g., tech-heavy).
3. High-risk instruments not aligned with user's profile.
4. Suggestions for improvement, if any.

Also compute the rough risk level (Low / Medium / High), and provide a confidence level for long-term stability.

Input Portfolio (from Agent 2):
{insert ticker list and rationale here}

Output a review report, any red flags or optimizations, and an updated portfolio if needed.
```

---

### ✅ Bonus (Optional Agent 4): **Performance Projection Agent**

```text
You are a Financial Forecast AI. Using the final portfolio, simulate the expected return range over 20 years based on historical performance and Monte Carlo simulations.

Output:
- Expected CAGR
- Probable range at 10th, 50th, and 90th percentile
- Warning if too aggressive/conservative
```

---

## 🔄 Agent Loop Setup

You can structure this using:

* **LangGraph** (if you want graph-style interaction)
* **CrewAI** (if you prefer workflow-style execution with role-based agents)
* **Manual Python orchestration** with a context-sharing object

---

Would you like me to give you a working **LangGraph example code template** or a **Streamlit demo setup** for this?
