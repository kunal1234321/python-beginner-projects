# CSV Data Analyzer

A simple Python tool that analyzes customer data from a CSV file and generates a text report.

## Features

* Reads CSV files
* Counts total customers
* Displays available columns
* Calculates average age
* Generates a `report.txt` file

## Technologies

* Python
* CSV
* File handling

## How to Run

```bash
python csv_analyzer.py
```

Enter the CSV filename when prompted:

```text
customers.csv
```

## Example

Input:

```csv
name,age,city
Kunal,20,Nashik
Rahul,25,Pune
Amit,22,Mumbai
```

Output:

```text
Total customers: 3
Average age: 22.33
```
