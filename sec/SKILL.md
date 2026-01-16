---
name: sec
description: Retrieve SEC 10-K filings for specified companies using the secedgar Python library. Use when users want to download 10-K filings by ticker symbol(s), save SEC 10-K PDFs locally, or automate bulk retrieval of 10-K reports for multiple companies.
---

# SEC 10-K Filings

## Quick Start

Download 10-K filings by running the provided script:

```bash
python scripts/download_10k.py AAPL MSFT TSLA --email you@example.com --save-dir ./10k_pdf
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

## Script Usage

The `scripts/download_10k.py` script can be invoked directly or imported as a module:

```python
from scripts.download_10k import download_10k

download_10k(['AAPL', 'MSFT'], './filings', 'user@example.com')
```

## Notes

- Only official PDF files are downloaded (HTML filings are skipped)
- The most recent 10-K filing for each ticker is retrieved
- The save directory is created automatically if it doesn't exist
