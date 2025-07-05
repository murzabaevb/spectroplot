# Purpose

`spectrum_plot.py` allows to create 
1. Plots of overlapped sub-bands of the same category, and 
2. Combine adjacent or overlapped sub-bands into contiguous sub-bands.

## Input data structure
It reads data from pre-formated Excel file named `categories and sub-bands.xlsx`.
It is also expected that there is a sheet named `categories and sub-bands` 
in the Excel file. The Excel file must be in the same folder as the 
`spectrum_plot.py` file. Example of such a file is provided in `docs` folder.

It is expected that the data is organized in columns:

| Column name      | Description                       |
|------------------|-----------------------------------|
| `category`       | filter applies for grouping       |
| `start_freq_mhz` | start frequency, MHz              |
| `end_freq_mhz`   | end frequency, MHz                |
| `excluded`       | `yes`= not counted, `no`= counted |


## Data export
Contiguous ranges made of overlapped and adjacent sub-bands of the same
category is stored in a separate Excel file 
`frequency_overlap_data_DATE_TIME.xlsx`. This data is presented
for all categories found in the `category` column. 
Example of such a file is provided in `docs` folder.

## Frequency overlap diagram
The overlap diagram is created and stored as 
`CATEGORY_overlap_chart.png` file for each category. 
All diagram files are stored in the same folder
as the `spectrum_plot.py` file.

![Example diagram](docs/FSS_overlap_chart.png)



 