#!/usr/bin/env python3
"""
KWEB Weighted PE Calculator

Fetches KWEB top 10 holdings, retrieves individual stock PEs, and calculates
the weighted average PE for the entire KWEB ETF.

Note: This skill uses agent-browser for web automation.
"""

import re
import sys
from typing import List, Dict, Tuple, Optional

# When using this skill, invoke the agent-browser skill to:
# 1. Navigate to https://hk.finance.yahoo.com/quote/KWEB/
# 2. Extract the top 10 holdings from the holdings table
# 3. For each holding, navigate to https://hk.finance.yahoo.com/quote/{SYMBOL}/
# 4. Extract the PE ratio from each stock page


def parse_weight(weight_text: str) -> float:
    """Parse weight percentage from text like '12.34%'."""
    match = re.search(r'(\d+\.?\d*)%', weight_text)
    return float(match.group(1)) if match else 0


def parse_pe(pe_text: str) -> Optional[float]:
    """Parse PE ratio from text."""
    if not pe_text or pe_text.lower() in ['n/a', '-', 'na']:
        return None
    match = re.search(r'[-+]?\d*\.?\d+', pe_text)
    return float(match.group()) if match else None


def calculate_weighted_pe(holdings: List[Dict[str, any]], default_pe: float = 20) -> float:
    """
    Calculate weighted PE for KWEB.

    Args:
        holdings: List of dicts with keys: name, symbol, weight, pe
        default_pe: Default PE for stocks where PE is unavailable

    Returns:
        Weighted PE ratio
    """
    print("\n=== Weighted PE Calculation ===\n")

    total_weight = 0
    weighted_sum = 0

    for i, holding in enumerate(holdings):
        name = holding.get('name', '')
        symbol = holding.get('symbol', '')
        weight = holding.get('weight', 0)
        pe = holding.get('pe')

        if pe is None:
            pe = default_pe
            print(f"{i+1}. {name} ({symbol}): PE=N/A (using {default_pe}), Weight={weight}%")
        else:
            print(f"{i+1}. {name} ({symbol}): PE={pe}, Weight={weight}%")

        weighted_contribution = weight * pe
        weighted_sum += weighted_contribution
        total_weight += weight
        print(f"   Contribution: {weighted_contribution:.2f}")

    print(f"\n=== Summary ===")
    print(f"Top 10 total weight: {total_weight}%")
    print(f"Top 10 weighted PE contribution: {weighted_sum:.2f}")

    # Remaining weight for other holdings (assumed PE = default_pe)
    remaining_weight = 100 - total_weight
    remaining_contribution = remaining_weight * default_pe

    print(f"Remaining weight (assumed PE={default_pe}): {remaining_weight}%, Contribution={remaining_contribution:.2f}")

    total_weighted_pe = weighted_sum + remaining_contribution

    print(f"\n=== Final Result ===")
    print(f"Total weighted PE for KWEB: {total_weighted_pe:.2f}")

    return total_weighted_pe


def main():
    """
    Main function to orchestrate the KWEB PE calculation.

    This function is a guide for the agent-browser workflow:
    1. Use agent-browser to visit https://hk.finance.yahoo.com/quote/KWEB/
    2. Extract holdings table data (name, symbol, weight)
    3. For each stock, visit its page and extract PE
    4. Call calculate_weighted_pe() with the collected data
    """
    print("=== KWEB Weighted PE Calculator ===")
    print("\nInstructions:")
    print("1. Use agent-browser to fetch KWEB holdings from https://hk.finance.yahoo.com/quote/KWEB/")
    print("2. Extract top 10 holdings with name, symbol, and weight")
    print("3. For each stock, fetch PE from https://hk.finance.yahoo.com/quote/{SYMBOL}/")
    print("4. Call calculate_weighted_pe() with the collected data")

    # Example of expected data structure:
    holdings = [
        {'name': 'Alibaba Group', 'symbol': 'BABA', 'weight': 25.5, 'pe': 12.3},
        {'name': 'JD.com', 'symbol': 'JD', 'weight': 10.2, 'pe': 18.5},
        # ... more holdings
    ]

    # weighted_pe = calculate_weighted_pe(holdings)
    # print(f"\nFinal weighted PE: {weighted_pe:.2f}")


if __name__ == "__main__":
    main()
