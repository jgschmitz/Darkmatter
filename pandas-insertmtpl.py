"""
SETI Data Processing with Pandas
Processes multiple CSV files from SETI datasets and combines them for analysis.
"""
import pandas as pd
import glob
import os
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_seti_csv_files(file_pattern: str = "data/seti_*.csv", 
                          output_file: Optional[str] = None) -> pd.DataFrame:
    """
    Process multiple SETI CSV files and combine them into a single DataFrame.
    
    Args:
        file_pattern: Glob pattern for CSV files
        output_file: Optional output file path for combined data
    
    Returns:
        Combined DataFrame with all SETI data
    """
    try:
        files = glob.glob(file_pattern)
        
        if not files:
            logger.warning(f"No files found matching pattern: {file_pattern}")
            return pd.DataFrame()
        
        logger.info(f"Found {len(files)} files to process")
        
        # Use generator for memory efficiency with large files
        dataframes = []
        for file in files:
            try:
                df = pd.read_csv(file)
                df['source_file'] = os.path.basename(file)  # Track source
                dataframes.append(df)
                logger.info(f"Processed: {file} ({len(df)} rows)")
            except Exception as e:
                logger.error(f"Error processing {file}: {e}")
                continue
        
        if not dataframes:
            logger.error("No valid files could be processed")
            return pd.DataFrame()
        
        # Combine all DataFrames
        result = pd.concat(dataframes, ignore_index=True)
        logger.info(f"Combined dataset shape: {result.shape}")
        
        # Optional: Save combined data
        if output_file:
            result.to_csv(output_file, index=False)
            logger.info(f"Combined data saved to: {output_file}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error in process_seti_csv_files: {e}")
        return pd.DataFrame()

def analyze_seti_data(df: pd.DataFrame) -> dict:
    """
    Basic analysis of SETI data.
    
    Args:
        df: DataFrame containing SETI data
    
    Returns:
        Dictionary with analysis results
    """
    if df.empty:
        return {"error": "DataFrame is empty"}
    
    analysis = {
        "total_records": len(df),
        "columns": list(df.columns),
        "data_types": df.dtypes.to_dict(),
        "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024 / 1024,
        "missing_values": df.isnull().sum().to_dict()
    }
    
    # Add numeric column statistics if available
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        analysis["numeric_summary"] = df[numeric_cols].describe().to_dict()
    
    return analysis

if __name__ == "__main__":
    # Example usage
    combined_data = process_seti_csv_files(
        file_pattern="path/to/your/seti/files/seti_*.csv",
        output_file="combined_seti_data.csv"
    )
    
    if not combined_data.empty:
        analysis_results = analyze_seti_data(combined_data)
        print("SETI Data Analysis Results:")
        for key, value in analysis_results.items():
            print(f"{key}: {value}")
