
## ArchivesSpace-SNAC Enrichment Project  

### **Project Overview**  
This project enriches **ArchivesSpace agent records** by integrating **SNAC (Social Networks and Archival Context) identifiers** to enhance metadata interoperability across archival and library systems.  

### **Scope of the Project**  
- Standardizing and validating **SNAC ARKs (Archival Resource Keys)** for ArchivesSpace agent records  
- Querying and processing data via the **ArchivesSpace API** and **SNAC API**  
- Handling **record reconciliation** and **tracking SNAC merges**  
- Logging and documenting updates for future maintenance  

### **Out of Scope**  
- Bulk migration of all agent records (current focus is structured enrichment)  
- Broader integration beyond SNAC (e.g., VIAF, Wikidata, BnF are future considerations)  
- Manual edits—this project relies on **automated processing** via scripts  

### **Technical Details**  
- **Python-based** processing with `requests`, `pandas`, and `json`  
- **Batch API querying & caching** to manage large datasets efficiently  
- **Automated error tracking & logging** for debugging  
- **Modular script structure** for future expansion  

### **Current Status**  
This is an **ongoing project**, currently focused on:  
1. **Data Cleaning & Standardization**  
2. **API Querying & Record Reconciliation**  
3. **Updating Agent Records in ArchivesSpace**  

### **Project Structure**  
```
ASPACE-SNAC-ENRICHMENT
├── logs/                    # Logs for tracking errors and processing results
├── src/                     # Core scripts for data processing and API interactions
│   ├── api/                 # Scripts for querying ArchivesSpace & SNAC APIs
│   ├── data/                # Cached API responses
├── notebooks/               # Research and analysis notes (not included in repo)
├── README.md                # Project documentation (this file)
├── .gitignore               # Specifies excluded files and directories
├── requirements.txt         # Dependencies for the project
```
