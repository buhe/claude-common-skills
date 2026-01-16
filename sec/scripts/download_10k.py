#!/usr/bin/env python3
"""
Download SEC 10-K filings for specified companies.

This script uses secedgar to fetch and save 10-K PDF reports.
"""

from pathlib import Path
from secedgar import filings, FilingType

def download_10k(tickers, save_dir, email):
    """
    Download the most recent 10-K filings for specified tickers.

    Args:
        tickers (list): List of stock ticker symbols (e.g., ['AAPL', 'MSFT'])
        save_dir (str or Path): Directory path to save PDFs
        email (str): Contact email required by SEC

    Returns:
        Path: The directory where files were saved
    """
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)

    f = filings(
        cik_lookup=tickers,
        filing_type=FilingType.FILING_10K,
        user_agent=email)

    f.save(save_dir)
    return save_dir

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download SEC 10-K filings")
    parser.add_argument("tickers", nargs="+", help="Stock ticker symbols (e.g., AAPL MSFT)")
    parser.add_argument("--save-dir", default="./10k_pdf", help="Directory to save PDFs")
    parser.add_argument("--email", required=True, help="Contact email for SEC (required)")
    args = parser.parse_args()

    result_dir = download_10k(args.tickers, args.save_dir, args.email)
    print(f"Download complete. Files saved to: {result_dir.resolve()}")
