---
name: sec
description: Retrieve SEC 10-K filings for specified companies using the secedgar Python library. Use when users want to download 10-K filings by ticker symbol(s), save SEC 10-K PDFs locally, or automate bulk retrieval of 10-K reports for multiple companies.
---

# SEC 10-K Filings

## Quick Start

Download 10-K filings by running the provided script:

```bash
# Download most recent 10-K filings
python scripts/download_10k.py AAPL MSFT TSLA --email you@example.com --save-dir ./10k_pdf

# Download 10-K filings within a date range
python scripts/download_10k.py AAPL --email you@example.com --start-date 2020-12-10 --end-date 2020-12-15
```

## Prerequisites

Install the secedgar library:

```bash
pip install secedgar
```

## Required Parameters

- `tickers`: List of stock ticker symbols (e.g., `['AAPL', 'MSFT', 'TSLA']`)
- `email`: Contact email required by SEC for API access
- `save_dir`: Directory path where PDFs will be saved (default: `./10k_pdf`)

## Optional Parameters

- `start_date`: Start date for filing search in YYYY-MM-DD format
- `end_date`: End date for filing search in YYYY-MM-DD format
- `count`: Maximum number of filings to retrieve (default: 50)

## Script Usage

The `scripts/download_10k.py` script can be invoked directly or imported as a module:

```python
from scripts.download_10k import download_10k
from datetime import date

# Download most recent filings
download_10k(['AAPL', 'MSFT'], './filings', 'user@example.com')

# Download filings within a date range
download_10k(
    ['AAPL'],
    './filings',
    'user@example.com',
    start_date=date(2020, 12, 10),
    end_date=date(2020, 12, 15),
    count=50
)
```

## Notes

- Only official PDF files are downloaded (HTML filings are skipped)
- The most recent 10-K filing for each ticker is retrieved (when no date range is specified)
- When `start_date` and `end_date` are provided, filings are retrieved from the entire SEC database within that range
- The save directory is created automatically if it doesn't exist
