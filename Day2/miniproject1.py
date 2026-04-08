import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Set random seed for reproducibility
np.random.seed(42)


# Generate synthetic sales data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
n_days = len(dates)


# Create dataset
data = {
    'Date': dates,
    'Product_A': np.random.randint(20, 100, n_days),
    'Product_B': np.random.randint(15, 80, n_days),
    'Product_C': np.random.randint(5, 50, n_days),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n_days),
    'Discount': np.random.choice([0, 5, 10, 15, 20], n_days, p=[0.6, 0.2, 0.1, 0.05, 0.05])
}


df = pd.DataFrame(data)


# Calculate total sales and revenue
df['Total_Units'] = df['Product_A'] + df['Product_B'] + df['Product_C']
df['Revenue'] = (df['Product_A'] * 50 + df['Product_B'] * 75 + df['Product_C'] * 100) * (1 - df['Discount']/100)


# Calculate cost and profit
df['Cost'] = (df['Product_A'] * 30 + df['Product_B'] * 45 + df['Product_C'] * 60)  # Assuming costs
df['Profit'] = df['Revenue'] - df['Cost']


# Extract time features
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Quarter'] = df['Date'].dt.quarter


print("="*60)
print("SALES DATA ANALYSIS DASHBOARD")
print("="*60)
print(f"Dataset Shape: {df.shape}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Units Sold: {df['Total_Units'].sum():,}")
print("="*60)


# MONTH-WISE STATISTICS
print("\n" + "="*60)
print("MONTH-WISE PERFORMANCE STATISTICS")
print("="*60)


monthly_stats = df.groupby('Month').agg({
    'Revenue': ['sum', 'mean', 'std'],
    'Profit': ['sum', 'mean', 'std'],
    'Total_Units': ['sum', 'mean'],
    'Cost': 'sum'
}).round(2)


# Flatten column names
monthly_stats.columns = ['Total_Revenue', 'Avg_Revenue', 'Std_Revenue',
                         'Total_Profit', 'Avg_Profit', 'Std_Profit',
                         'Total_Units', 'Avg_Units', 'Total_Cost']


# Add profit margin
monthly_stats['Profit_Margin_%'] = (monthly_stats['Total_Profit'] / monthly_stats['Total_Revenue'] * 100).round(2)


# Add month names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_stats.index = month_names


print("\nMonthly Statistics Summary:")
print(monthly_stats.to_string())


# Find best and worst months
best_month = monthly_stats['Total_Profit'].idxmax()
worst_month = monthly_stats['Total_Profit'].idxmin()
best_growth = monthly_stats['Total_Profit'].pct_change().max() * 100


print(f"\n📈 KEY INSIGHTS:")
print(f"🏆 Best Month for Profit: {best_month} (${monthly_stats.loc[best_month, 'Total_Profit']:,.2f})")
print(f"📉 Worst Month for Profit: {worst_month} (${monthly_stats.loc[worst_month, 'Total_Profit']:,.2f})")
print(f"💹 Highest Month-over-Month Growth: {best_growth:.1f}%")
print(f"💰 Average Monthly Profit: ${monthly_stats['Total_Profit'].mean():,.2f}")


# PROFIT GROWTH BAR CHART
fig, axes = plt.subplots(2, 2, figsize=(16, 10))


# 1. Profit Growth Bar Chart (Main)
months = monthly_stats.index
profits = monthly_stats['Total_Profit']
colors = ['#2ECC71' if p > 0 else '#E74C3C' for p in profits.diff().fillna(0)]
bars = axes[0, 0].bar(months, profits, color=colors, edgecolor='black', linewidth=1.5)
axes[0, 0].set_title('Monthly Profit Growth Analysis', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Profit ($)')
axes[0, 0].grid(True, alpha=0.3, axis='y')


# Add value labels on bars
for bar, profit in zip(bars, profits):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                   f'${profit:,.0f}', ha='center', fontweight='bold', fontsize=9)


# Add growth percentage arrows
for i in range(1, len(profits)):
    growth = ((profits.iloc[i] - profits.iloc[i-1]) / profits.iloc[i-1]) * 100
    y_pos = max(profits.iloc[i], profits.iloc[i-1]) + 5000
    axes[0, 0].annotate(f'▲ {growth:.1f}%' if growth > 0 else f'▼ {abs(growth):.1f}%',
                       xy=(i, profits.iloc[i]), xytext=(i, y_pos),
                       ha='center', fontsize=8, color='green' if growth > 0 else 'red')


# 2. Revenue vs Profit Comparison
x = np.arange(len(months))
width = 0.35
axes[0, 1].bar(x - width/2, monthly_stats['Total_Revenue'], width, label='Revenue', color='#3498DB', alpha=0.8)
axes[0, 1].bar(x + width/2, monthly_stats['Total_Profit'], width, label='Profit', color='#2ECC71', alpha=0.8)
axes[0, 1].set_title('Revenue vs Profit by Month', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Amount ($)')
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(months)
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3, axis='y')


# 3. Profit Margin Trend
axes[1, 0].plot(months, monthly_stats['Profit_Margin_%'], marker='o', linewidth=2,
                markersize=8, color='#E67E22')
axes[1, 0].fill_between(months, monthly_stats['Profit_Margin_%'], alpha=0.2, color='#E67E22')
axes[1, 0].set_title('Monthly Profit Margin Trend', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Profit Margin (%)')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].axhline(y=monthly_stats['Profit_Margin_%'].mean(), color='red',
                   linestyle='--', label=f'Avg: {monthly_stats["Profit_Margin_%"].mean():.1f}%')
axes[1, 0].legend()


# Add value labels on points
for i, (month, margin) in enumerate(zip(months, monthly_stats['Profit_Margin_%'])):
    axes[1, 0].annotate(f'{margin:.1f}%', xy=(i, margin), xytext=(0, 10),
                       textcoords='offset points', ha='center', fontsize=8)


# 4. Month-over-Month Profit Growth Rate
growth_rates = monthly_stats['Total_Profit'].pct_change() * 100
growth_colors = ['green' if x > 0 else 'red' for x in growth_rates]
axes[1, 1].bar(months[1:], growth_rates[1:], color=growth_colors[1:], edgecolor='black')
axes[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=1)
axes[1, 1].set_title('Month-over-Month Profit Growth Rate', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Growth Rate (%)')
axes[1, 1].grid(True, alpha=0.3, axis='y')


# Add value labels
for i, (month, rate) in enumerate(zip(months[1:], growth_rates[1:])):
    axes[1, 1].text(i, rate + (2 if rate > 0 else -8), f'{rate:.1f}%',
                   ha='center', fontsize=8, fontweight='bold')


plt.suptitle('MONTH-WISE PROFIT ANALYSIS DASHBOARD', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# DETAILED MONTHLY REPORT
print("\n" + "="*60)
print("DETAILED MONTHLY PERFORMANCE REPORT")
print("="*60)


# Create a detailed summary table
summary_table = pd.DataFrame({
    'Month': month_names,
    'Total_Profit ($)': monthly_stats['Total_Profit'].values,
    'Total_Revenue ($)': monthly_stats['Total_Revenue'].values,
    'Profit_Margin (%)': monthly_stats['Profit_Margin_%'].values,
    'Total_Units': monthly_stats['Total_Units'].values,
    'Avg_Profit_per_Unit ($)': (monthly_stats['Total_Profit'] / monthly_stats['Total_Units']).round(2).values
})


print("\n", summary_table.to_string(index=False))


# Identify growth patterns
print("\n" + "="*60)
print("GROWTH PATTERN ANALYSIS")
print("="*60)


# Calculate cumulative profit
monthly_stats['Cumulative_Profit'] = monthly_stats['Total_Profit'].cumsum()


print(f"\n📊 Cumulative Profit Growth:")
for month, cum_profit in zip(month_names, monthly_stats['Cumulative_Profit']):
    print(f"   {month}: ${cum_profit:,.2f}")


# Best 3 months for profit
top_3_months = monthly_stats.nlargest(3, 'Total_Profit')
print(f"\n🏆 TOP 3 PROFITABLE MONTHS:")
for month in top_3_months.index:
    profit = top_3_months.loc[month, 'Total_Profit']
    margin = top_3_months.loc[month, 'Profit_Margin_%']
    print(f"   {month}: ${profit:,.2f} (Margin: {margin:.1f}%)")


print("\n" + "="*60)

