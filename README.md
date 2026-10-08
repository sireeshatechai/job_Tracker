# Job Tracker

A command-line tool, written in Python, that tracks job applications in a SQLite database. It flags applications that need a follow-up, exports data to CSV, and can email a daily summary.

## Planned commands

```
python tracker.py add --company "Acme" --role "Data Engineer" --link "https://..."
python tracker.py list --status applied
python tracker.py update 3 --status interview
python tracker.py followups      # applied 7+ days ago, no update
python tracker.py stats          # counts by status
python tracker.py export         # writes applications.csv
python tracker.py digest         # emails a daily summary
```

## Statuses

applied, screening, interview, offer, rejected, withdrawn

## Tech

Python, argparse, sqlite3, csv, smtplib

## Status

Work in progress (Week 1 of a 90-day AI automation / data engineering challenge).