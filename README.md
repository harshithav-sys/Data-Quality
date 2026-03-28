Data Quality Migration Validator

Overview

This project demonstrates a Data Quality Validation Framework designed to simulate the migration of legacy validation checks into a modern Python-based system.
The core objective is to ensure that migrated validation logic behaves identically to the original implementation, which is critical when transitioning legacy systems (e.g., Perl) to modern ecosystems.
This prototype reflects the core idea of LLM-assisted code migration combined with automated correctness verification.

---------------------------------------------------------------------------------
Key Features

1.Data quality checks for:
Sugar validation
Salt validation
Product name validation
2. Dual execution system:
Simulated legacy (Perl-style) checks
Modern Python-based checks
3. Validation engine:
Compares outputs between both implementations
Detects mismatches automatically
4. Structured output:
Per-check validation results
Overall validation status
---------------------------------------------------------------------------------
Core Idea

Instead of blindly converting legacy code:
This system ensures functional equivalence between old and new implementations.
---------------------------------------------------------------------------------
Pipeline

Input Data
   ↓
Legacy Check (Perl Simulation)
   ↓
Converted Check (Python)
   ↓
Comparison Engine
   ↓
Validation Result (PASS / FAIL)

-------------------------------------------------------------------------------
Project Structure

Data-Quality/
│
├── check/
│   ├── name_check.py
│   ├── salt_check.py
│   ├── sugar_check.py
│
├── data/
│   ├── sample_products.json
│
├── validation/
│   ├── validator.py
│
├── main.py
├── README.md
└── requirements.txt

-------------------------------------------------------------------------------------
How It Works

Each product is validated using both:

1.Perl-style validation logic
2.Python-based validation logic

The system compares both outputs:
compare(perl_output, python_output)

And produces:
Match status
Individual outputs
Final validation decision

--------------------------------------------------------------------------------------
Example Output:

{
  "product": {"name": "", "sugar": 120, "salt": 2},
  "results": {
    "sugar": {
      "perl_output": "ERROR",
      "python_output": "ERROR",
      "match": true,
      "status": "PASS"
    },
    "name": {
      "perl_output": "MISSING",
      "python_output": "MISSING",
      "match": true,
      "status": "PASS"
    },
    "salt": {
      "perl_output": "OK",
      "python_output": "OK",
      "match": true,
      "status": "PASS"
    }
  },
  "overall_status": "PASS"
}
----------------------------------------------------------------------------------------
Why This Project Matters???

Migrating legacy validation systems is risky because:

Small logic differences can break data quality
Manual verification is unreliable

This project solves that by:

✔ Automating correctness verification
✔ Ensuring identical behavior across systems
✔ Providing a scalable validation approach
-----------------------------------------------------------------------------------------
Use Case 

This prototype directly aligns with:
LLM-Assisted Migration of Data Quality Checks

It demonstrates how:

Legacy checks can be converted into Python
Outputs can be verified automatically
Migration can be made safe and reliable
-------------------------------------------------------------------------------------------
Key Insight

LLM-based migration alone is not reliable
But
LLM + Validation Engine = Production-ready system
-------------------------------------------------------------------------------------------
Future Improvements

1.Integration with real Perl checks
2.LLM-based automated code conversion
3.Large-scale dataset validation
4.Integration with DuckDB
5.Dashboard for data quality monitoring
