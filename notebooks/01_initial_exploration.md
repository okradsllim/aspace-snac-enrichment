# SNAC ID Integration Project: Initial Research & Understanding

## Project Description
The Lux team has requested that SCMS add SNAC identifiers to ArchivesSpace agent records. We have a spreadsheet from 2020 containing 18,771 SNAC IDs associated with ArchivesSpace agent URIs. The project involves:

1. Adding these identifiers to the record identifier field in ArchivesSpace agent records
2. Running a report to identify ArchivesSpace agent records with LCNAF URIs that aren't represented in our list of 18,771 records
3. Retrieving SNAC IDs for these additional records (either from Wikidata or the SNAC API) using the LCNAF URI as the match point
4. Updating ArchivesSpace with these newly retrieved SNAC IDs

## Initial Research Journey

### Understanding the Data: ARKs vs SNAC IDs
What began as a seemingly straightforward data integration project revealed itself to be more complex upon closer examination of the spreadsheet. The key discovery was that what was labeled as "SNAC ID" in the project description manifested as ARK identifiers in the actual data.

This discrepancy led to several important realizations:

1. **Terminology Clarification**:
   - SNAC ID/Constellation ID: Acts as a primary identifier within the SNAC system (analogous to a Social Security Number)
   - ARK (Archival Resource Key): Functions as a resolution mechanism pointing to SNAC constellations (analogous to a passport)

2. **Data Structure**:
   - The spreadsheet contains ARKs, not direct SNAC IDs
   - These ARKs resolve to SNAC constellation pages when accessed
   - Understanding this distinction is crucial for accurate data processing

### Deep Dive into ARK Structure

#### Pattern Analysis
A systematic examination of the spreadsheet revealed that all 18,000+ records shared a consistent pattern up to the final slash in their ARK identifiers. Most significantly, every ARK contained the string "99166".

#### NAAN Investigation
Research into the "99166" component led to several important findings:

1. **NAAN Definition**:
   - NAAN (Name Assigning Authority Number) is a unique identifier assigned to organizations creating ARK identifiers
   - "99166" is specifically reserved for People, Groups, and Institutions as Agents
   - Important: This NAAN is not exclusively assigned to SNAC

2. **Institutional Context**:
   - SNAC's status as a cooperative project rather than a traditional institution raises interesting questions about NAAN usage
   - Other non-organizational entities may also use the 99166 NAAN
   - This shared usage has important implications for API querying and data validation

### API Considerations

#### Current Understanding
Initial research suggests a pattern where all SNAC ARKs contain the 99166 NAAN, but not all 99166 ARKs necessarily belong to SNAC. This understanding needs further verification through:

1. Detailed examination of the SNAC API documentation
2. Analysis of ARK patterns within SNAC systems
3. Development of robust validation methods

#### Research Strategy
The investigation has progressed through several stages:
1. Initial pattern recognition in the spreadsheet data
2. Basic ARK structure research
3. NAAN investigation
4. Ongoing API documentation review

## Technical Implementation Considerations

### Data Processing Requirements
1. **Spreadsheet Processing**:
   - Need to handle 18,771 records systematically
   - Ensure proper mapping between ARKs and ArchivesSpace records

2. **API Integration**:
   - Develop robust query mechanisms for SNAC API
   - Include fallback to Wikidata when necessary
   - Implement proper error handling and validation

3. **ArchivesSpace Updates**:
   - Plan for systematic record updates
   - Ensure proper handling of identifier subrecords
   - Implement verification processes

### Validation Challenges
- Verify SNAC ID retrieval accuracy given shared NAAN usage
- Ensure proper mapping between different identifier systems
- Maintain data integrity during bulk updates

## Next Steps

1. **API Research**:
   - Continue investigating SNAC API documentation
   - Document specific endpoints and query parameters
   - Develop testing strategy for API interactions

2. **Data Validation**:
   - Create verification process for ARK-to-SNAC ID mappings
   - Develop quality control measures for bulk updates
   - Plan for error handling and edge cases

3. **Implementation Planning**:
   - Design systematic approach for record updates
   - Create backup and rollback procedures
   - Develop progress tracking mechanisms

## Lessons Learned
1. The importance of thorough initial research before implementation
2. The value of understanding identifier systems and their relationships
3. The need to verify assumptions about data structure and ownership
4. The benefits of systematic investigation of technical documentation

## Research Resources
- ARK Identifier System Documentation
- SNAC API Documentation
- Wikipedia ARK article
- Internal project documentation
- NAAN Registry documentation

*Note: This document will be updated as the project progresses and new insights are gained.*
