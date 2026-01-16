---
name: javbus-scraper
description: "Access and navigate https://javbus.com using agent-browser, handling age verification checks with AI assistance if present, and extract video links. Use when user wants to: 1) Access javbus.com and pass age verification, 2) Extract video links from the site, 3) Navigate and interact with the website programmatically."
---

# Javbus Scraper

## Overview

This skill enables accessing javbus.com, navigating through age verification challenges using AI, and extracting video links from the site.

## Workflow

### Step 1: Open Website

Navigate to the target URL using agent-browser:

```bash
agent-browser open https://javbus.com
```

### Step 2: Check for Age Verification

Take a snapshot to see the current page state:

```bash
agent-browser snapshot
```

Look for age verification elements such as:
- "I am 18+" buttons
- Age entry forms
- "Enter" or "Confirm" buttons
- Warning text about adult content

### Step 3: Handle Age Verification

**If age verification is present:**

1. Analyze the page content from the snapshot
2. For age entry questions, use AI to determine the correct response:
   - If asked "Are you 18 or older?", click the "Yes" option
   - If asked to enter age, input 18 or above
   - Look for buttons like "Enter", "I Agree", "Confirm"

Use appropriate agent-browser commands:
```bash
agent-browser click <selector>     # For buttons
agent-browser fill <selector> "18" # For age entry fields
agent-browser press Enter          # Submit the form
```

2. Take another snapshot to verify success:
```bash
agent-browser snapshot
```

**If no age verification is present:**

Skip to Step 4.

### Step 4: Extract First Video Link

After successfully passing age verification (or if no verification was needed):

1. Take a snapshot of the main page:
```bash
agent-browser snapshot
```

2. Look for video link elements, typically with:
   - `<a>` tags pointing to video pages
   - Video thumbnails or titles
   - Classes or attributes containing "movie", "video", "item"

3. Extract the first video link using:
```bash
agent-browser get attr href <selector>
```

4. Print the first video link to verify successful navigation

## Tips

- Use `agent-browser snapshot -i` for a compact view of interactive elements only
- The `@ref` system in snapshots allows you to reference elements (e.g., `@e2` refers to element #2)
- Use `agent-browser get text` to read page content if needed for analysis
- If age verification fails, take a snapshot and analyze what went wrong
