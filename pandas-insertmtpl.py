import logging
from glob import glob
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def process_seti_csv_files(
    file_pattern: str = "data/seti_*.csv",
    output_file: str | Path | None = None,
    *,
    strict: bool = False,
) -> pd.DataFrame:
    """Combine matching CSV files, adding a source_file column.

    With strict=False, unreadable or malformed files are logged and skipped.
    With strict=True, those errors are raised instead.
    """
    output_path = Path(output_file).resolve() if output_file is not None else None

    files = sorted(
        path
        for name in glob(file_pattern, recursive=True)
        if (path := Path(name)).is_file()
        and path.resolve() != output_path
    )

    if not files:
        logger.warning("No input files found matching: %s", file_pattern)
        return pd.DataFrame()

    logger.info("Found %d input files", len(files))
    dataframes: list[pd.DataFrame] = []
    skipped = 0

    for path in files:
        try:
            df = pd.read_csv(path)
        except (OSError, UnicodeError, pd.errors.ParserError, pd.errors.EmptyDataError):
            if strict:
                raise
            logger.exception("Skipping unreadable CSV: %s", path)
            skipped += 1
            continue

        # Fail explicitly rather than silently destroying an input column.
        if "source_file" in df.columns:
            raise ValueError(
                f"{path} already contains the reserved column 'source_file'"
            )

        df["source_file"] = path.name
        dataframes.append(df)
        logger.info("Read %s: %d rows", path, len(df))

    if not dataframes:
        logger.error("No valid files could be processed")
        return pd.DataFrame()

    result = pd.concat(dataframes, ignore_index=True, sort=False)
    logger.info(
        "Combined %d files; skipped %d; shape=%s",
        len(dataframes),
        skipped,
        result.shape,
    )

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output_path, index=False)
        logger.info("Saved combined data to %s", output_path)

    return result
