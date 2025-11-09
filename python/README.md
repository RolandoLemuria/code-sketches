# Python Code Sketches

Quick Python code experiments and practice exercises. Each sketch focuses on a specific concept or technique with beginner-friendly comments to help anyone learn programming.

## Structure

- `01-basic-algorithms/` - Sorting, searching, and fundamental algorithms
- `02-file-manipulation/` - Working with files and text processing
- `03-decorators/` - Function decorators and metaprogramming
- `04-data-structures/` - Custom implementations of data structures
- `05-web-scraping/` - Simple web scraping examples
- `06-api-requests/` - HTTP requests and API interactions

## Running Sketches

Execute any sketch directly:

```bash
python python/01-basic-algorithms/bubble_sort.py
python python/02-file-manipulation/word_counter.py
python python/03-decorators/timer_decorator.py
```

Or from the python directory:

```bash
cd python
python 01-basic-algorithms/bubble_sort.py
```

## Setup

1. **Create a virtual environment** (from project root):
```bash
python -m venv venv
```

2. **Activate the virtual environment**:
```bash
# On Windows (Git Bash)
source venv/Scripts/activate

# On Windows (PowerShell)
venv\Scripts\Activate.ps1

# On Windows (CMD)
venv\Scripts\activate.bat

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r python/requirements.txt
```

4. **Deactivate when finished**:
```bash
deactivate
```

## Current Sketches

### Basic Algorithms
- **bubble_sort.py** - Simple bubble sort implementation with step-by-step comments

### File Manipulation
- **word_counter.py** - Count word frequencies in text using Counter

### Decorators
- **timer_decorator.py** - Measure function execution time with decorators

## Contributing

Feel free to add your own sketches! Guidelines:
- Keep each sketch focused on one concept
- Add detailed comments explaining the code for beginners
- Include a `if __name__ == "__main__":` test block
- Follow Python naming conventions (snake_case for files and functions)