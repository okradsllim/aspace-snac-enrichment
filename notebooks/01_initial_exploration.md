# SNAC ID Integration Project: Research & Development

## Initial Data Exploration

This notebook will be used for processing my thoughts, as I explore, clean up, and enrich the ArchivesSpace agent data.

### Initial Exploration of SNAC-ArchivesSpace Dataset

#### Overview
I started with a CSV file containing 18,771 records, each representing an agent in ArchivesSpace. The dataset included the following columns:
- `uri` – ArchivesSpace agent URI
- `sort_name` – Agent name, often with birth/death dates
- `authority_id` – Library of Congress authority control URL
- `created_by` – Indicates who created the record
- Two unnamed columns (later identified as `snac_arks` and `additional_authorities`)

#### Issues Identified
1. The last two columns were missing headers, making it difficult to process the data.
2. Some fields contained extraneous whitespace.
3. The CSV format wasn't properly detecting the unnamed columns.
4. I needed to ensure the dataset was correctly structured before making API queries.

#### Actions Taken
- Opened the file in Excel and **manually named the last two columns** as `snac_arks` and `additional_authorities`.
- Saved the file as `snac_uris_outfile.xlsx` to preserve the corrected structure.
- Wrote `scan_csv.py` to inspect the dataset and confirm that all columns were properly recognized.

#### Next Steps
Now that the structure is confirmed, I moved on to **cleaning and standardizing the dataset** before processing it further.

## Deeper Investigation: Understanding ARKs vs SNAC IDs

After having received the spreadsheet and paying closer attention to it, I learned that I have to do more research than I thought I would have to in order to truly bring this project to fruition. My initial data cleaning revealed a more complex conceptual challenge.

### The Conceptual Challenge

The project description uses the term "SNAC ID," but the spreadsheet contains what appear to be ARKs (Archival Resource Keys). This discovery prompted a deeper investigation into:

1. What exactly is a "SNAC ID" versus an "ARK"?
2. How do these identifiers relate to each other?
3. What are the implications for our data integration process?

### Understanding the Relationship

From my SNAC training last summer with Jerry Simmons and colleagues, I recalled information about SNAC Constellation IDs, but needed to clarify their relationship with ARKs. This research led to an illuminating analogy:

- **SNAC Constellation IDs** are like Social Security Numbers - primary identifiers within the SNAC system
- **ARKs** are like passports - resolution mechanisms that point to those identifiers

### ARK Structure Analysis

A systematic examination of the spreadsheet revealed an important pattern. Using a basic Control+F search across the "SNAC ARKs" column in Excel, I confirmed:

1. All 18,000+ records shared the same pattern up to the final slash
2. Every ARK contained the string "99166"

This consistent pattern prompted further investigation into the meaning of "99166" and its relationship to SNAC.

### NAAN Investigation

My research into ARK structure led me to investigate the "99166" component:

1. **What is a NAAN?**
   - NAAN stands for Name Assigning Authority Number
   - It's a unique identifier assigned to organizations that create ARK identifiers

2. **Significance of "99166"**
   - This specific NAAN is reserved for "People, Groups, and Institutions as Agents"
   - It is not exclusively assigned to SNAC
   - It's used by multiple non-organizational entities

This discovery raised important questions about SNAC's institutional status and the uniqueness of the identifiers in our dataset.

### Implications for API Integration

The shared usage of NAAN "99166" has significant implications for our project:

1. **Query Precision**
   - If multiple entities use 99166, how do we ensure our API queries return only SNAC-specific results?
   - What additional parameters or validation steps are needed?

2. **Pattern Confirmation**
   - Current evidence suggests all SNAC ARKs contain 99166
   - But not all 99166 ARKs necessarily belong to SNAC
   - This requires careful validation during our integration process

### Ongoing API Research

I'm continuing to research the SNAC API to understand:

1. How ARKs are represented in API documentation
2. Patterns in their example ARKs
3. Whether we can confidently assert that "all SNAC ARKs will have 99166"

Initial findings support this pattern, but further verification is necessary.

## Project Implementation Plan

### Technical Requirements
Based on the project description and my research:

1. **Data Integration**
   - Update 18,771 agent records with new record identifier subrecord containing SNAC ID
   - Ensure proper mapping between ARKs and ArchivesSpace records

2. **Reporting**
   - Run report in ArchivesSpace identifying records with LCNAF ID but no SNAC ID
   - Generate list of records requiring SNAC ID retrieval

3. **API Integration**
   - Query SNAC API or Wikidata to retrieve SNAC IDs for the subset with LCNAF IDs
   - Use LCNAF URI as the match point
   - Implement proper validation and error handling

4. **ArchivesSpace Updates**
   - Update ArchivesSpace with newly retrieved SNAC IDs
   - Ensure data integrity during bulk updates

### Validation Strategy
Given the complexities discovered:

1. **Identifier Verification**
   - Validate ARK-to-SNAC ID relationships
   - Confirm proper resolution of ARKs to SNAC constellations
   - Develop test cases for edge scenarios

2. **Data Quality**
   - Check for duplicate or conflicting identifiers
   - Ensure proper formatting and structure
   - Document any anomalies or exceptions

### Next Steps

1. **Complete API Research**
   - Finalize understanding of SNAC API endpoints and parameters
   - Document query patterns and authentication requirements
   - Test API responses with sample data

2. **Implementation Planning**
   - Design systematic approach for record updates
   - Create backup and rollback procedures
   - Develop progress tracking mechanisms

3. **Documentation**
   - Create comprehensive documentation of the integration process
   - Document lessons learned and best practices
   - Prepare knowledge transfer materials

## Conclusion

What initially appeared to be a straightforward data integration project has revealed deeper complexities around identifier systems and their relationships. This investigation has highlighted the importance of thorough research before implementation and the need to understand the nuanced relationships between different identifier systems.

The project continues to evolve as new insights are gained, and this notebook will be updated accordingly.

*Last updated: February 20, 2025*
