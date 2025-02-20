# Initial Data Exploration
This notebook will be used for processing my thoughts, as I explore, clean up, and enrich the ArchivesSpace agent data.

# Initial Exploration of SNAC-ArchivesSpace Dataset

## Overview
I started with a CSV file containing 18,771 records, each representing an agent in ArchivesSpace. The dataset included the following columns:

- `uri` – ArchivesSpace agent URI
- `sort_name` – Agent name, often with birth/death dates
- `authority_id` – Library of Congress authority control URL
- `created_by` – Indicates who created the record
- Two unnamed columns (later identified as `snac_arks` and `additional_authorities`)

## Issues Identified
1. The last two columns were missing headers, making it difficult to process the data.
2. Some fields contained extraneous whitespace.
3. The CSV format wasn’t properly detecting the unnamed columns.
4. I needed to ensure the dataset was correctly structured before making API queries.

## Actions Taken
- Opened the file in Excel and **manually named the last two columns** as `snac_arks` and `additional_authorities`.
- Saved the file as `snac_uris_outfile.xlsx` to preserve the corrected structure.
- Wrote `scan_csv.py` to inspect the dataset and confirm that all columns were properly recognized.

## Next Steps
Now that the structure is confirmed, I moved on to **cleaning and standardizing the dataset** before processing it further.
