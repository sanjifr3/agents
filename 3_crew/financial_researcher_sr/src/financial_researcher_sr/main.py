#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from financial_researcher_sr.crew import FinancialResearcherSr

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {"company": "Nvidia"}

    try:
        result = FinancialResearcherSr().crew().kickoff(inputs=inputs)
        print(f"Crew finished successfully at {datetime.now()}")
        print("Final Output:", result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
