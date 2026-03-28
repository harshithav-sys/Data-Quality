Data Quality Migration Validator

Overview

This project demonstrates a Data Quality Validation Framework designed to simulate the migration of legacy validation checks into a modern Python-based system.
The core objective is to ensure that migrated validation logic behaves identically to the original implementation, which is critical when transitioning legacy systems (e.g., Perl) to modern ecosystems.
This prototype reflects the core idea of LLM-assisted code migration combined with automated correctness verification.

---------------------------------------------------------------------------------
Key Features<br>

1.Data quality checks for:
Sugar validation
Salt validation
Product name validation<br>
2.Dual execution system:
Simulated legacy (Perl-style) checks
Modern Python-based checks<br>
3.Validation engine:
Compares outputs between both implementations
Detects mismatches automatically<br>
4.Structured output:
Per-check validation results
Overall validation status<br>

---------------------------------------------------------------------------------
Core Idea

Instead of blindly converting legacy code:
This system ensures functional equivalence between old and new implementations.

---------------------------------------------------------------------------------
Pipeline
## Validation Pipeline

Input Data<br>
   ↓<br>
Legacy Check (Perl Simulation)<br>
   ↓<br>
Converted Check (Python)<br>
   ↓<br>
Comparison Engine<br>
   ↓<br>
Validation Result (PASS / FAIL)<br>

-------------------------------------------------------------------------------
Project Structure
## Project Structure

Data-Quality/<br>
│<br>
├── check/<br>
│   ├── name_check.py<br>
│   ├── salt_check.py<br>
│   ├── sugar_check.py<br>
│<br>
├── data/<br>
│   ├── sample_products.json<br>
│<br>
├── validation/<br>
│   ├── validator.py<br>
│<br>
├── main.py<br>
├── README.md<br>
└── requirements.txt<br>

-------------------------------------------------------------------------------------
How It Works

Each product is validated using both:<br>

1.Perl-style validation logic<br>
2.Python-based validation logic<br>

The system compares both outputs:<br>
compare(perl_output, python_output)<br>

And produces:
Match status<br>
Individual outputs<br>
Final validation decision<br>

--------------------------------------------------------------------------------------
Example Output:

{<br>
  "product": {"name": "", "sugar": 120, "salt": 2},<br>
  "results": { <br>
    "sugar": { <br>
      "perl_output": "ERROR",<br>
      "python_output": "ERROR",<br>
      "match": true,<br>
      "status": "PASS"<br>
    },<br>
    "name": { <br>
      "perl_output": "MISSING", <br>
      "python_output": "MISSING",<br>
      "match": true,<br>
      "status": "PASS"<br>
    },<br>
    "salt": { <br>
      "perl_output": "OK",<br>
      "python_output": "OK",<br>
      "match": true,<br>
      "status": "PASS"<br>
    }<br>
  },<br>
  "overall_status": "PASS"<br>
}<br>

----------------------------------------------------------------------------------------
Why This Project Matters???<br>

Migrating legacy validation systems is risky because:<br>

Small logic differences can break data quality<br>
Manual verification is unreliable<br>

This project solves that by:<br>

Automating correctness verification<br>
Ensuring identical behavior across systems<br>
Providing a scalable validation approach<br>

-----------------------------------------------------------------------------------------
Use Case 

This prototype directly aligns with:<br>
LLM-Assisted Migration of Data Quality Checks<br>

It demonstrates how:<br>

Legacy checks can be converted into Python<br>
Outputs can be verified automatically<br>
Migration can be made safe and reliable<br>

-------------------------------------------------------------------------------------------
Key Insight<br>

LLM-based migration alone is not reliable<br>
But<br>
LLM + Validation Engine = Production-ready system<br>

-------------------------------------------------------------------------------------------
Future Improvements<br>

1.Integration with real Perl checks<br>
2.LLM-based automated code conversion<br>
3.Large-scale dataset validation<br>
4.Integration with DuckDB<br>
5.Dashboard for data quality monitoring<br>
