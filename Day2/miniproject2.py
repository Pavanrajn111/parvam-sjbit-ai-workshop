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


miniproject2.py:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Set random seed for reproducibility
np.random.seed(42)


# Generate synthetic student data
num_students = 200
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'English']
departments = ['Computer Science', 'Engineering', 'Medicine', 'Business', 'Humanities']


# Create student data
student_data = {
    'Student_ID': [f'STU{str(i).zfill(3)}' for i in range(1, num_students + 1)],
    'Name': [f'Student_{i}' for i in range(1, num_students + 1)],
    'Department': np.random.choice(departments, num_students, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    'Year': np.random.choice([1, 2, 3, 4], num_students, p=[0.3, 0.3, 0.25, 0.15]),
    'Attendance_%': np.random.normal(75, 15, num_students).clip(30, 100).round(1),
    'Assignments_Submitted': np.random.randint(5, 15, num_students),
    'Total_Assignments': 15,
}


df = pd.DataFrame(student_data)


# Generate subject-wise marks (0-100)
for subject in subjects:
    # Different difficulty levels for different subjects
    if subject in ['Mathematics', 'Physics']:
        mean = np.random.normal(65, 15, num_students)
    elif subject in ['Chemistry', 'Biology']:
        mean = np.random.normal(70, 12, num_students)
    elif subject == 'Computer Science':
        mean = np.random.normal(75, 15, num_students)
    else:
        mean = np.random.normal(72, 10, num_students)
   
    df[f'{subject}_Marks'] = mean.clip(0, 100).round(2)


# Calculate derived metrics
df['Total_Marks'] = df[[f'{subj}_Marks' for subj in subjects]].sum(axis=1)
df['Average_Percentage'] = (df['Total_Marks'] / (len(subjects) * 100) * 100).round(2)
df['Assignment_Completion_%'] = (df['Assignments_Submitted'] / df['Total_Assignments'] * 100).round(1)


# Assign grades
def assign_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'


df['Grade'] = df['Average_Percentage'].apply(assign_grade)


# Calculate CGPA (scale 0-4)
df['CGPA'] = (df['Average_Percentage'] / 25).round(2)
df['CGPA'] = df['CGPA'].clip(0, 4)


# Performance categories
def performance_category(percentage):
    if percentage >= 80:
        return 'Excellent'
    elif percentage >= 70:
        return 'Good'
    elif percentage >= 60:
        return 'Satisfactory'
    elif percentage >= 50:
        return 'Needs Improvement'
    else:
        return 'Poor'


df['Performance'] = df['Average_Percentage'].apply(performance_category)


print("="*70)
print("STUDENT PROGRESS REPORT DASHBOARD")
print("="*70)
print(f"Total Students: {len(df)}")
print(f"Total Departments: {len(departments)}")
print(f"Subjects: {', '.join(subjects)}")
print(f"Overall Class Average: {df['Average_Percentage'].mean():.2f}%")
print(f"Overall Class CGPA: {df['CGPA'].mean():.2f}")
print("="*70)


# ============================================
# USE CASE 1: Department-wise Performance Analysis
# ============================================
print("\n" + "="*70)
print("USE CASE 1: DEPARTMENT-WISE PERFORMANCE ANALYSIS")
print("="*70)


dept_stats = df.groupby('Department').agg({
    'Average_Percentage': ['mean', 'std', 'min', 'max'],
    'CGPA': 'mean',
    'Attendance_%': 'mean',
    'Assignment_Completion_%': 'mean'
}).round(2)


dept_stats.columns = ['Avg_%', 'Std_%', 'Min_%', 'Max_%', 'Avg_CGPA', 'Avg_Attendance', 'Avg_Assignment']
print("\nDepartment Statistics:")
print(dept_stats)


# Best and worst departments
best_dept = dept_stats['Avg_%'].idxmax()
worst_dept = dept_stats['Avg_%'].idxmin()
print(f"\n🏆 Best Performing Department: {best_dept} ({dept_stats.loc[best_dept, 'Avg_%']:.2f}%)")
print(f"📉 Needs Improvement: {worst_dept} ({dept_stats.loc[worst_dept, 'Avg_%']:.2f}%)")


# Visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 10))


# Department performance bar chart
depts = dept_stats.index
avg_scores = dept_stats['Avg_%']
colors_bar = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars = axes[0, 0].bar(depts, avg_scores, color=colors_bar[:len(depts)], edgecolor='black', linewidth=1.5)
axes[0, 0].set_title('Department-wise Average Performance', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Average Percentage (%)')
axes[0, 0].set_ylim([0, 100])
axes[0, 0].grid(True, alpha=0.3, axis='y')
axes[0, 0].axhline(y=df['Average_Percentage'].mean(), color='red', linestyle='--',
                   label=f'Overall Avg: {df["Average_Percentage"].mean():.1f}%')
axes[0, 0].legend()


# Add value labels
for bar, score in zip(bars, avg_scores):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                   f'{score:.1f}%', ha='center', fontweight='bold')


# Attendance vs Performance correlation
axes[0, 1].scatter(df['Attendance_%'], df['Average_Percentage'], alpha=0.5, c='#45B7D1', s=50)
axes[0, 1].set_title('Attendance vs Academic Performance', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Attendance (%)')
axes[0, 1].set_ylabel('Average Percentage (%)')
axes[0, 1].grid(True, alpha=0.3)


# Add trend line
z = np.polyfit(df['Attendance_%'], df['Average_Percentage'], 1)
p = np.poly1d(z)
axes[0, 1].plot(sorted(df['Attendance_%']), p(sorted(df['Attendance_%'])),
                "r--", linewidth=2, label=f'Trend (r={np.corrcoef(df["Attendance_%"], df["Average_Percentage"])[0,1]:.2f})')
axes[0, 1].legend()


# Assignment completion impact - FIXED: Added observed=False
completion_bins = pd.cut(df['Assignment_Completion_%'], bins=[0, 50, 70, 85, 100],
                         labels=['<50%', '50-70%', '70-85%', '85-100%'])
assignment_perf = df.groupby(completion_bins, observed=False)['Average_Percentage'].mean()
axes[1, 0].bar(assignment_perf.index, assignment_perf.values, color='#FF6B6B', edgecolor='black')
axes[1, 0].set_title('Assignment Completion Impact on Grades', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Assignment Completion Rate')
axes[1, 0].set_ylabel('Average Percentage (%)')
axes[1, 0].grid(True, alpha=0.3, axis='y')


# Department-wise grade distribution - FIXED: Only use grades that exist
grade_order = ['A+', 'A', 'B+', 'B', 'C', 'D', 'F']
grade_counts = pd.crosstab(df['Department'], df['Grade'])
# Only keep grades that actually exist in the data
existing_grades = [g for g in grade_order if g in grade_counts.columns]
grade_counts = grade_counts[existing_grades] if existing_grades else grade_counts
grade_counts_percent = grade_counts.div(grade_counts.sum(axis=1), axis=0) * 100


grade_counts_percent.T.plot(kind='barh', ax=axes[1, 1], stacked=True,
                            color=['#2ECC71', '#39D98A', '#FFD166', '#FF9F1C', '#FF6B6B', '#C44569', '#A55D35'][:len(existing_grades)])
axes[1, 1].set_title('Grade Distribution by Department', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Percentage of Students (%)')
axes[1, 1].legend(title='Grade', bbox_to_anchor=(1.05, 1), loc='upper left')


plt.suptitle('STUDENT PROGRESS DASHBOARD - Part 1', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# ============================================
# USE CASE 2: Subject-wise Performance Analysis
# ============================================
print("\n" + "="*70)
print("USE CASE 2: SUBJECT-WISE PERFORMANCE ANALYSIS")
print("="*70)


subject_stats = pd.DataFrame()
for subject in subjects:
    subject_stats.loc[subject, 'Average'] = df[f'{subject}_Marks'].mean()
    subject_stats.loc[subject, 'Median'] = df[f'{subject}_Marks'].median()
    subject_stats.loc[subject, 'Std_Dev'] = df[f'{subject}_Marks'].std()
    subject_stats.loc[subject, 'Pass_%'] = (df[f'{subject}_Marks'] >= 40).mean() * 100
    subject_stats.loc[subject, 'Distinction_%'] = (df[f'{subject}_Marks'] >= 75).mean() * 100


print("\nSubject Statistics:")
print(subject_stats.round(2))


# Identify strong and weak subjects
strongest_subj = subject_stats['Average'].idxmax()
weakest_subj = subject_stats['Average'].idxmin()
print(f"\n📚 Strongest Subject: {strongest_subj} (Avg: {subject_stats.loc[strongest_subj, 'Average']:.2f})")
print(f"📚 Weakest Subject: {weakest_subj} (Avg: {subject_stats.loc[weakest_subj, 'Average']:.2f})")


# Visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 10))


# Subject performance bar chart
subjects_list = subject_stats.index
avg_marks = subject_stats['Average']
std_marks = subject_stats['Std_Dev']
bars = axes[0, 0].bar(subjects_list, avg_marks, yerr=std_marks, capsize=5,
                      color='#3498DB', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Subject-wise Average Performance', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Average Marks (out of 100)')
axes[0, 0].set_ylim([0, 100])
axes[0, 0].grid(True, alpha=0.3, axis='y')
axes[0, 0].axhline(y=40, color='red', linestyle='--', label='Passing Mark (40)')
axes[0, 0].legend()


# Add value labels
for bar, score in zip(bars, avg_marks):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                   f'{score:.1f}', ha='center', fontweight='bold')


# Pass percentage by subject
pass_rates = subject_stats['Pass_%']
colors_pass = ['green' if rate >= 90 else 'orange' if rate >= 75 else 'red' for rate in pass_rates]
axes[0, 1].barh(subjects_list, pass_rates, color=colors_pass, edgecolor='black')
axes[0, 1].set_title('Subject-wise Pass Percentage', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Pass Rate (%)')
axes[0, 1].axvline(x=75, color='orange', linestyle='--', alpha=0.7)
axes[0, 1].axvline(x=90, color='green', linestyle='--', alpha=0.7)
axes[0, 1].grid(True, alpha=0.3, axis='x')


# Box plot for all subjects
subject_data = [df[f'{subj}_Marks'] for subj in subjects]
bp = axes[1, 0].boxplot(subject_data, labels=subjects, patch_artist=True,
                        boxprops=dict(facecolor='#FFD166', alpha=0.7))
axes[1, 0].set_title('Subject-wise Marks Distribution', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Marks (out of 100)')
axes[1, 0].axhline(y=40, color='red', linestyle='--', label='Passing Mark')
axes[1, 0].grid(True, alpha=0.3, axis='y')
axes[1, 0].legend()
plt.setp(axes[1, 0].xaxis.get_majorticklabels(), rotation=45, ha='right')


# Correlation heatmap of subjects
corr_matrix = df[[f'{subj}_Marks' for subj in subjects]].corr()
im = axes[1, 1].imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
axes[1, 1].set_xticks(range(len(subjects)))
axes[1, 1].set_yticks(range(len(subjects)))
axes[1, 1].set_xticklabels(subjects, rotation=45, ha='right')
axes[1, 1].set_yticklabels(subjects)
axes[1, 1].set_title('Subject Correlation Heatmap', fontsize=12, fontweight='bold')


# Add correlation values
for i in range(len(subjects)):
    for j in range(len(subjects)):
        text = axes[1, 1].text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                               ha="center", va="center", color="black", fontsize=8)
plt.colorbar(im, ax=axes[1, 1])


plt.suptitle('STUDENT PROGRESS DASHBOARD - Part 2', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# ============================================
# USE CASE 3: Year-wise Progress & Risk Analysis
# ============================================
print("\n" + "="*70)
print("USE CASE 3: YEAR-WISE PROGRESS & RISK ANALYSIS")
print("="*70)


year_stats = df.groupby('Year').agg({
    'Average_Percentage': ['mean', 'std'],
    'CGPA': 'mean',
    'Attendance_%': 'mean',
    'Assignment_Completion_%': 'mean'
}).round(2)


year_stats.columns = ['Avg_%', 'Std_%', 'Avg_CGPA', 'Avg_Attendance', 'Avg_Assignment']
print("\nYear-wise Statistics:")
print(year_stats)


# Identify at-risk students
df['At_Risk'] = (df['Average_Percentage'] < 50) | (df['Attendance_%'] < 60)
df['Academic_Alert'] = df['Average_Percentage'] < 40


at_risk_count = df['At_Risk'].sum()
alert_count = df['Academic_Alert'].sum()


print(f"\n⚠️ STUDENT RISK ANALYSIS:")
print(f"Students at Risk (Avg < 50% or Attendance < 60%): {at_risk_count} ({at_risk_count/len(df)*100:.1f}%)")
print(f"Academic Alert (Avg < 40%): {alert_count} ({alert_count/len(df)*100:.1f}%)")


# Yearly performance trend
fig, axes = plt.subplots(2, 2, figsize=(15, 10))


# Yearly average trend
years = sorted(df['Year'].unique())
avg_by_year = [df[df['Year'] == y]['Average_Percentage'].mean() for y in years]
std_by_year = [df[df['Year'] == y]['Average_Percentage'].std() for y in years]


axes[0, 0].plot(years, avg_by_year, marker='o', linewidth=2, markersize=10, color='#E74C3C')
axes[0, 0].fill_between(years, [avg - std for avg, std in zip(avg_by_year, std_by_year)],
                        [avg + std for avg, std in zip(avg_by_year, std_by_year)], alpha=0.2)
axes[0, 0].set_title('Year-wise Academic Performance Trend', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Average Percentage (%)')
axes[0, 0].grid(True, alpha=0.3)
for i, (year, avg) in enumerate(zip(years, avg_by_year)):
    axes[0, 0].annotate(f'{avg:.1f}%', xy=(year, avg), xytext=(5, 5),
                       textcoords='offset points', fontweight='bold')


# Risk distribution by year
risk_by_year = df.groupby('Year')['At_Risk'].mean() * 100
bars = axes[0, 1].bar(risk_by_year.index, risk_by_year.values, color='#FF6B6B', edgecolor='black')
axes[0, 1].set_title('At-Risk Students by Year', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('At-Risk Students (%)')
axes[0, 1].grid(True, alpha=0.3, axis='y')
for bar, pct in zip(bars, risk_by_year.values):
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{pct:.1f}%', ha='center', fontweight='bold')


# Performance distribution histogram
axes[1, 0].hist(df['Average_Percentage'], bins=20, color='#4ECDC4', edgecolor='black', alpha=0.7)
axes[1, 0].axvline(x=df['Average_Percentage'].mean(), color='red', linestyle='--',
                   label=f'Mean: {df["Average_Percentage"].mean():.1f}%')
axes[1, 0].axvline(x=50, color='orange', linestyle='--', label='Passing Threshold')
axes[1, 0].set_title('Overall Performance Distribution', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Average Percentage (%)')
axes[1, 0].set_ylabel('Number of Students')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3, axis='y')


# CGPA distribution pie chart
cgpa_ranges = pd.cut(df['CGPA'], bins=[0, 1.5, 2.5, 3.5, 4.0],
                     labels=['Poor (0-1.5)', 'Satisfactory (1.5-2.5)',
                            'Good (2.5-3.5)', 'Excellent (3.5-4.0)'])
cgpa_dist = cgpa_ranges.value_counts()
colors_pie = ['#E74C3C', '#F39C12', '#3498DB', '#2ECC71']
axes[1, 1].pie(cgpa_dist.values, labels=cgpa_dist.index, autopct='%1.1f%%',
               colors=colors_pie[:len(cgpa_dist)], startangle=90, explode=(0.05, 0.05, 0.05, 0.05))
axes[1, 1].set_title('CGPA Distribution', fontsize=12, fontweight='bold')


plt.suptitle('STUDENT PROGRESS DASHBOARD - Part 3', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# ============================================
# USE CASE 4: Individual Student Report & Recommendations
# ============================================
print("\n" + "="*70)
print("USE CASE 4: INDIVIDUAL STUDENT REPORT & RECOMMENDATIONS")
print("="*70)


# Top 5 performers
top_5 = df.nlargest(5, 'Average_Percentage')[['Student_ID', 'Name', 'Department', 'Year',
                                               'Average_Percentage', 'CGPA', 'Grade']]
print("\n🏆 TOP 5 PERFORMERS:")
print(top_5.to_string(index=False))


# Bottom 5 performers
bottom_5 = df.nsmallest(5, 'Average_Percentage')[['Student_ID', 'Name', 'Department', 'Year',
                                                  'Average_Percentage', 'CGPA', 'Grade']]
print("\n📉 BOTTOM 5 PERFORMERS (Need Intervention):")
print(bottom_5.to_string(index=False))


# Generate individual recommendations
def generate_recommendations(row):
    recommendations = []
    if row['Average_Percentage'] < 50:
        recommendations.append("⚠️ Academic probation - Immediate intervention required")
    if row['Attendance_%'] < 75:
        recommendations.append("📊 Improve attendance - Attend at least 90% of classes")
    if row['Assignment_Completion_%'] < 80:
        recommendations.append("📝 Submit pending assignments on time")
   
    # Subject-specific recommendations
    weak_subjects = []
    for subject in subjects:
        if row[f'{subject}_Marks'] < 50:
            weak_subjects.append(subject)
   
    if weak_subjects:
        recommendations.append(f"📚 Focus on weak subjects: {', '.join(weak_subjects[:3])}")
   
    if row['Average_Percentage'] >= 85:
        recommendations.append("🎯 Maintain excellence - Consider research opportunities")
    elif row['Average_Percentage'] >= 70:
        recommendations.append("💪 Good performance - Aim for distinction in all subjects")
   
    return recommendations


df['Recommendations'] = df.apply(generate_recommendations, axis=1)


# Show sample recommendations
print("\n💡 SAMPLE STUDENT RECOMMENDATIONS:")
sample_students = df.sample(3)
for _, student in sample_students.iterrows():
    print(f"\n📌 Student: {student['Name']} ({student['Student_ID']})")
    print(f"   Performance: {student['Average_Percentage']:.1f}% (Grade: {student['Grade']})")
    print(f"   Attendance: {student['Attendance_%']:.1f}%")
    for rec in student['Recommendations']:
        print(f"   • {rec}")


# Visualization for final summary
fig, axes = plt.subplots(1, 3, figsize=(15, 5))


# Grade distribution
grade_dist = df['Grade'].value_counts().sort_index()
colors_grades = ['#2ECC71', '#39D98A', '#FFD166', '#FF9F1C', '#FF6B6B', '#C44569', '#A55D35']
axes[0].pie(grade_dist.values, labels=grade_dist.index, autopct='%1.1f%%',
            colors=colors_grades[:len(grade_dist)], startangle=90)
axes[0].set_title('Overall Grade Distribution', fontsize=12, fontweight='bold')


# Performance categories
perf_dist = df['Performance'].value_counts()
colors_perf = {'Excellent': '#2ECC71', 'Good': '#39D98A', 'Satisfactory': '#FFD166',
               'Needs Improvement': '#FF9F1C', 'Poor': '#FF6B6B'}
axes[1].bar(perf_dist.index, perf_dist.values, color=[colors_perf[p] for p in perf_dist.index],
            edgecolor='black')
axes[1].set_title('Student Performance Categories', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Performance Level')
axes[1].set_ylabel('Number of Students')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True, alpha=0.3, axis='y')


# Add value labels
for i, (cat, count) in enumerate(zip(perf_dist.index, perf_dist.values)):
    axes[1].text(i, count + 1, str(count), ha='center', fontweight='bold')


# Correlation between attendance, assignments, and performance
metrics = df[['Attendance_%', 'Assignment_Completion_%', 'Average_Percentage']].corr()
im = axes[2].imshow(metrics, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
axes[2].set_xticks(range(3))
axes[2].set_yticks(range(3))
axes[2].set_xticklabels(['Attendance', 'Assignments', 'Performance'], rotation=45)
axes[2].set_yticklabels(['Attendance', 'Assignments', 'Performance'])
axes[2].set_title('Key Metrics Correlation', fontsize=12, fontweight='bold')


for i in range(3):
    for j in range(3):
        text = axes[2].text(j, i, f'{metrics.iloc[i, j]:.2f}',
                           ha="center", va="center", color="black", fontsize=10)
plt.colorbar(im, ax=axes[2])


plt.suptitle('STUDENT PROGRESS SUMMARY DASHBOARD', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# FINAL SUMMARY REPORT
print("\n" + "="*70)
print("FINAL SUMMARY REPORT & ACTIONABLE INSIGHTS")
print("="*70)


print("\n📊 KEY STATISTICS:")
print(f"   • Class Average: {df['Average_Percentage'].mean():.2f}%")
print(f"   • Class CGPA: {df['CGPA'].mean():.2f}")
print(f"   • Average Attendance: {df['Attendance_%'].mean():.1f}%")
print(f"   • Average Assignment Completion: {df['Assignment_Completion_%'].mean():.1f}%")


print("\n🎯 RECOMMENDATIONS FOR IMPROVEMENT:")
print(f"   • Focus on {weakest_subj} - Lowest performing subject")
print(f"   • Improve attendance - Correlation with performance: {np.corrcoef(df['Attendance_%'], df['Average_Percentage'])[0,1]:.2f}")
print(f"   • Increase assignment completion - Current average: {df['Assignment_Completion_%'].mean():.1f}%")
print(f"   • Provide extra support to {worst_dept} department")
print(f"   • Academic alert for {alert_count} students")


print("\n✅ SUCCESS INDICATORS:")
print(f"   • Excellent students (80%+): {(df['Average_Percentage'] >= 80).sum()} ({(df['Average_Percentage'] >= 80).mean()*100:.1f}%)")
print(f"   • Pass rate: {(df['Average_Percentage'] >= 40).mean()*100:.1f}%")
print(f"   • Distinction rate (75%+): {(df['Average_Percentage'] >= 75).mean()*100:.1f}%")


print("\n" + "="*70)