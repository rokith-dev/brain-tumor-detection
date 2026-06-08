from pathlib import Path


def prepare_dataset(raw_dir: str, processed_dir: str) -> None:
    raw_path = Path(raw_dir)
    processed_path = Path(processed_dir)
    processed_path.mkdir(parents=True, exist_ok=True)
    _ = raw_path
