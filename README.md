# File Analyzer

A simple Python script for analyzing log files and extracting useful information, such as:

* Number of lines
* Errors
* Warnings
* IP addresses found in the file

The analyzer uses a **limited set of keywords** to identify errors and warnings, so it may produce false positives depending on the file being analyzed.

## Usage

1. Clone the repository:
```bash
  git clone https://github.com/d4vidlinux/file_analyzer.git
  cd file_analyzer
```
    
2. Run the script by providing the file you want to analyze:

```bash
python3 file_analyzer.py FILE
```

### Example

```bash
python3 file_analyzer.py example.log
```

## Screenshots

### Log File

![Log Screenshot](log_screenshot.png)

### Script Output

![Script Screenshot](script_screenshot.png)

## Limitations

This is a simple project created for learning purposes. The analysis is based on predefined keywords and patterns, so:

* Some errors or warnings may not be detected.
* False positives may occur.
* The script is primarily intended for log files with relatively predictable formats.

## Requirements

* Python 3.x

No external libraries are required.




