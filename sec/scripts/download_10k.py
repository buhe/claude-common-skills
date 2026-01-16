#!/usr/bin/env python3
"""
Download SEC 10-K filings for specified companies.

This script uses secedgar to fetch and save 10-K PDF reports.
"""

from datetime import date
from pathlib import Path
from secedgar import filings, FilingType

def download_10k(tickers, save_dir, email, start_date=None, end_date=None, count=50):
    """
    Download 10-K filings for specified tickers, optionally filtered by date range.

    Args:
        tickers (list): List of stock ticker symbols (e.g., ['AAPL', 'MSFT'])
        save_dir (str or Path): Directory path to save PDFs
        email (str): Contact email required by SEC
        start_date (date, optional): Start date for filing search (YYYY-MM-DD)
        end_date (date, optional): End date for filing search (YYYY-MM-DD)
        count (int): Maximum number of filings to retrieve (default: 50)

    Returns:
        Path: The directory where files were saved
    """
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)

    f = filings(
        cik_lookup=tickers,
        filing_type=FilingType.FILING_10K,
        user_agent=email,
        count=count)

    if start_date and end_date:
        f = filings(
            start_date=start_date,
            end_date=end_date,
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
    parser.add_argument("--start-date", help="Start date for filing search (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date for filing search (YYYY-MM-DD)")
    parser.add_argument("--count", type=int, default=50, help="Maximum number of filings to retrieve")
    args = parser.parse_args()

    start_date = None
    end_date = None
    if args.start_date:
        year, month, day = map(int, args.start_date.split('-'))
        start_date = date(year, month, day)
    if args.end_date:
        year, month, day = map(int, args.end_date.split('-'))
        end_date = date(year, month, day)

    result_dir = download_10k(args.tickers, args.save_dir, args.email, start_date, end_date, args.count)
    print(f"Download complete. Files saved to: {result_dir.resolve()}")
