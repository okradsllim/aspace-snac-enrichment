# Cleaning Steps for SNAC-ArchivesSpace Dataset

## Goal
To ensure the dataset is structured correctly and ready for API queries.

## Cleaning Actions
1. **Scanned the dataset (`scan_csv.py`)**
   - Verified that all six expected columns were present.
   - Logged dataset structure to `logs/scan_csv.log`.

2. **Cleaned the dataset (`clean_csv.py`)**
   - Read `snac_uris_outfile.xlsx` into Pandas.
   - Stripped extra whitespace from all string fields.
   - Saved the cleaned version as `snac_uris_outfile_cleaned.csv`.

## Challenges & Solutions
- **Unnamed Columns Not Recognized in Pandas**  
  - Solution: Opened the file manually in Excel, assigned names, and resaved as `.xlsx`.

- **FutureWarning: `applymap()` Deprecated**  
  - Solution: Replaced `.applymap()` with `.map()` for string cleaning.

## Logs & Outputs
- Log file: `logs/clean_csv.log`
- Cleaned dataset: `src/data/snac_uris_outfile_cleaned.csv`

## Next Steps
Now that the data is cleaned, I will start querying the **ArchivesSpace API** to retrieve existing agent records.
