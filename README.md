# Python Practice Repository

This repository contains my daily Python practice problems and solutions.  
Each script demonstrates a programming concept and connects it to Business Analyst thinking.

## Contents

### Day 1
- **day1_hello_world.py** – Prints "Hello World" as a first program.
- **day1_largest_of_three.py** – Finds the largest of three numbers.
- **day1_positive_negative_zero.py** – Checks if a number is positive, negative, or zero.
- **day1_simple_calculator.py** – Implements a simple calculator for basic operations.

### Day 2
- **day2_factorial_printer.py** – Calculates factorial of a number.
- **day2_largest_in_list.py** – Finds the largest number in a list using built‑in functions.
- **day2_largest_in_list_manual.py** – Finds the largest number in a list manually with loops.

### Day 3
* **day3_sales_analysis.py** – Calculates total, average, highest, and lowest monthly sales figures.
* **day3_analyze_performance.py** – Custom function tracking team performance metrics and low-score indexing.

### Day 4
* **day4_dictionary_practice.py** – Safe product lookup system demonstrating dictionary key-value validation.
* **day4_employee_db.py** – Dynamically constructs an employee database with safe sentinel looping and nested assignments.
* **day4_ultimate_analyst.py** – Capstone project integrating dictionaries, sequential user logic, aggregation functions, and conditional roster outputs.

### Day 5
* **day5_inventory_value.py** – E-commerce inventory valuation script utilizing dictionary item unpacking, list indexing, and out-of-stock conditional checks.
* **day5_fraud_filter.py** – Risk prototype parsing dictionary transaction arrays to dynamically flag fraud accounts using multi-conditional logical operators.
* **day5_file_handling.py** – Implements contextual context managers to stream and strip raw external flat-file datasets line-by-line.
## 📅 Day 6: Python File Handling Fundamentals

Mastered managing external files—a critical skill for any Business Analyst tracking data streams, system logs, and flat data files.

### Key Learnings:
* **Read Mode (`"r"`)**: Using `with open()` blocks to safely open and extract data without memory leaks.
* **Write Mode (`"w"`)**: Understanding how write mode completely overwrites existing file content.
* **Append Mode (`"a"`)**: Learning to position the stream pointer at the end of a file to log data continuously using `.write()` without destroying existing information.

### Scripts Developed:
* **day6_read_passcode.py**: Initial blueprint for opening, reading, and storing text stream variables.
* **day6_logs_management.py**: Core simulation of a continuous business logging pipeline tracking system error states.

---

## 📅 Day 7: Memory-Efficient Data Streaming & Counter Metrics

Advanced to handling files line-by-line using loops, focusing on processing large-scale business logs and building operational KPI aggregates.

### Key Learnings:
* **Line-by-Line Loops**: Using `for line in file:` to pull individual data rows into memory sequentially, preventing memory overflow on massive datasets.
* **Data Cleansing (`.strip()`)**: Shaving off trailing white spaces and embedded newline flags (`\n`) from raw file records.
* **State Counters**: Initializing external tracking metrics and using conditional logic blocks (`if/else`) to isolate data segments and generate calculated KPIs.
* **Defensive Error Structures (`try/except/finally`)**: Implementing multi-stage safety networks to intercept file system crashes gracefully, allowing backend pipelines to remain continuous.
* **Universal Catch-All Shield (`Exception as e`)**: Deploying global error tracking targets to log unexpected hardware failures or script context corruptions.
* **Guaranteed Cleanup Routines (`finally`)**: Securing system resource lifecycles by executing vital pipeline logging and memory frame flushes under any termination scenario.

### Scripts Developed (Updated):
* **day7_revision_challenge.py**: Consolidation script applying multiple concurrent file stream modalities.
* **day7_line_reader.py**: Practical blueprint for clean streaming data layout using string manipulation.
* **day7_audit_filter.py**: Target-specific data extraction utilizing substring membership queries.
* **day7_metric_analyzer.py**: Executive summary calculator utilizing dual-state counter variables.
* **day7_error_handler.py**: Advanced 4-stage enterprise-grade exception handling matrix.
* **day7_multi_layer_defense.py**: Independent tracking module exploring custom error stream catch mechanics.
* **day7_column_parser.py**: Programmatic flat table file parsing module applying next-stream interception and mathematical element transformations.
* **day7_numerical_filter.py**: Core data auditing script demonstrating programmatic range filtering metrics utilizing mathematical thresholds and native f-string presentation templates.
* **day7_mini_project.py**: Capstone transaction auditing application combining data cleaning, multi-file appending, nested exception handling networks, and macro KPI aggregates.



## Day 8: Sales Report Generator 📈

### Concepts Practiced
* **File Handling**: Reading raw tracking items line-by-line and generating an automated output text file (`sales_summary.txt`).
* **String Processing**: Striping whitespaces and parsing comma-separated variables using `.split()`.
* **Dictionary Aggregation**: Implementing logic to uniquely map and accumulate sales values per customer without overwriting existing data keys.
* **Custom Functions**: Abstracting revenue formulas into scalable functions.

### Key Takeaway
Learned that dictionary keys must remain unique, requiring custom conditional lookups (`if key in dict:`) to accumulate business values over time rather than overwriting historical records.


## Day 9: Portfolio Expense Tracker 📊

### Concepts Practiced
* **Dynamic List Manipulation**: Populating an empty array from a raw file and appending new items explicitly using `.append()`.
* **Data Cleansing Loop**: Running a robust lookup conditional while statement (`while target in list:`) to thoroughly scrub out anomalies or duplicate minor transactions.
* **Array Aggregation**: Extracting absolute values efficiently using built-in methods like `sum()`, `max()`, and `len()`.
* **Array Slicing**: Sorting data arrays in descending order using `.sort(reverse=True)` and extracting key metric segments using clean bracket slicing (`[:2]`) instead of error-prone manual index counters.

### Key Takeaway
Slicing arrays using standard position brackets handles varying dataset lengths seamlessly, preventing `IndexError` vulnerabilities during automated report production.

# Underwriting Data Analytics Pipeline

A collection of Python scripts designed to clean, process, and analyze risk assessment data for commercial credit portfolios.

## Day 10: The Risk-Pool Cleanse (`day10_risk_cleanse.py`)

### 📋 Scenario
An automated system pulled a raw, unformatted list of credit risk scores for a commercial loan pool. The raw dataset contained non-numeric strings, duplicate applications, and negative values representing system errors. 

### 🛠️ Implementation Details
This script implements a strict data-cleansing pipeline using fundamental Python list structures:
1. **Validation & Extraction**: Utilizes string methods (`.isdigit()`) to safely drop invalid characters and negative values while converting clean strings to integers.
2. **Deduplication**: Filters out duplicate profiles to ensure independent applicant evaluations.
3. **Sorting**: Orders the final validated risk pool in descending order (highest creditworthiness first).
4. **Statistical Analysis**: Accurately extracts the **median score** of the pool using mathematical floor division (`//`) to identify the true center of the risk profile.


## 📅 Day 11: Modular Programming & Function Integration

### 🎯 Learning Focus
* Transferred development environment to **Google Colab** for zero-configuration, cloud-based data processing.
* Mastered the integration of **functions, loops, and lists** to simulate production-level data wrangling pipelines.
* Practiced advanced list traversal and indexing techniques essential for Business Analyst workflows.

### 💻 Challenges Completed

#### 1. Premium Pricing Engine (`day11_premium_calculator.py`)
* **Problem**: Designed a functional core engine to calculate insurance premium risk adjustments dynamically.
* **Skills**: Function definitions (`def`), argument handling, floating-point arithmetic, and value returns.

#### 2. Portfolio Premium Processor (`day11_portfolio_processor.py`)
* **Problem**: Scaled the core calculation engine to process an entire collection of corporate policy profiles simultaneously.
* **Skills**: Sequence bounds mapping via `range(len())`, list element indexing extraction, and loop-driven automation.

### 📈 Business Analyst Relevance
* Developed functional logic frameworks that mirror how risk adjustments are computed in live underwriting portfolios.
* Transitioned from single-value execution to automated batch array processing, a critical prerequisite for SQL and Power BI algorithmic automation.


# 📊 Business Analyst Python Preparation

Welcome to my repository tracking my core technical milestones as I prepare to transition into a Business Analyst role. This repository showcases my data manipulation scripts, clean pipelines, and structural automation workflows.

## 🚀 Day 12 Milestone: Data Aggregation & Safety Networks
Today's focus was mastering Python dictionary optimization methods to replace heavy control flow blocks, clean data anomalies, and engineering comprehensive exception handling frameworks to make scripts completely crash-proof.

### 📁 Core Project: `day12_call_analytics.py`
This script simulates processing raw log streams from a customer service platform. It addresses three vital operational questions:
1. **Data Aggregation**: Efficiently builds a data summary map using the `.get()` method to avoid logical structural overhead.
2. **Metric Filtering**: Scans through live profiles using the `.items()` method unpacking pattern to isolate team members matching performance criteria.
3. **Reverse Data Lookup**: Executes conditional matching to index specific entities based on direct transactional value thresholds.

### 📁 Safety Architecture: Exception Handling Frameworks
To guarantee script resilience when scraping web files or loading server databases, I engineered four custom exception handling blueprints:
1. **`day12_error_handling.py`**: Intercepts calculation math traps (`ZeroDivisionError`) to establish data fallback constraints without stopping dashboard processing.
2. **`day12_multiple_errors.py`**: Deploys a stacked multi-except architecture capable of screening distinct structural threats (`ValueError` vs. calculation faults) inside a dynamic list iteration loop.
3. **`day12_file_safety.py`**: Restricts systemic file IO dependency risks (`FileNotFoundError`) to route data streams dynamically to backup repositories.
4. **`day12_pipeline_complete.py`**: Implements the ultimate 4-stage processing matrix (`try / except / else / finally`) to guarantee safe remote database handshakes, performance notifications, and memory clean-ups.


### 📆 Day 13: Dictionary Operations & Exception Handling Flow
*   **Focus**: Mastered flat dictionary operations and implemented an explicit, 4-part control flow safety net.
*   **Concepts Covered**:
    *   Accessing, updating, and adding elements inside dictionaries dynamically.
    *   Key existence validation checks (`if "Key" in dict:`).
    *   Structured error mitigation utilizing `try`, `except KeyError`, `else`, and `finally` blocks to intercept messy data exceptions without crashing scripts.
*   **Business Context**: Simulated an automated corporate device tracker capable of reporting records dynamically or flagging missing department data lines gracefully.



---
*Follow along as I continue deploying technical automation models daily!*





---

## Next Steps
Future scripts will expand into:
- Data analysis with CSV files and pandas.
- SQL query practice.
- Business case exercises with insights and recommendations.

---

## Purpose
This repo is part of my journey to transition into a **Business Analyst role**.  
It shows not just coding skills, but also the ability to turn raw numbers into clear business insights.

