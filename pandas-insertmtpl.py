"""SETI Data Processing with Pandas

Processes multiple CSV files from SETI datasets and combines them for analysis.
"""

import logging
from pathlib import Path
from typing import Optional

import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def process_seti_csv_files(
    file_pattern: str = "data/seti_*.csv",
    output_file: Optional[str] = None,
) -> pd.DataFrame:
    files = list(Path().glob(file_pattern))

    if not files:
        logger.warning("No files found matching pattern: %s", file_pattern)
        return pd.DataFrame()

    logger.info("Found %d files to process", len(files))

    dataframes = []
    for file in files:
        try:
            df = pd.read_csv(file)
            df['source_file'] = file.name
            dataframes.append(df)
            logger.info("Processed: %s (%d rows)", file, len(df))
        except Exception as e:
            logger.error("Error processing %s: %s", file, e)

    if not dataframes:
        logger.error("No valid files could be processed")
        return pd.DataFrame()

    result = pd.concat(dataframes, ignore_index=True)
    logger.info("Combined dataset shape: %s", result.shape)

    if output_file:
        result.to_csv(output_file, index=False)
        logger.info("Combined data saved to: %s", output_file)

    return result


def analyze_seti_data(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"error": "DataFrame is empty"}

    analysis = {
        "total_records": len(df),
        "columns": list(df.columns),
        "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "memory_usage_mb": df.memory_usage(deep=True).sum() / (1024 ** 2),
        "missing_values": df.isnull().sum().to_dict(),
    }

    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        analysis["numeric_summary"] = df[numeric_cols].describe().to_dict()

    return analysis


if __name__ == "__main__":
    combined_data = process_seti_csv_files(
        file_pattern="path/to/your/seti/files/seti_*.csv",
        output_file="combined_seti_data.csv",
    )

    if not combined_data.empty:
        analysis_results = analyze_seti_data(combined_data)
        print("SETI Data Analysis Results:")
        for key, value in analysis_results.items():
            print(f"{key}: {value}")

