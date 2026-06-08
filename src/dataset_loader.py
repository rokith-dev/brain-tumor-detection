from pathlib import Path


def load_image_paths(dataset_dir: str):
    dataset_path = Path(dataset_dir)
    if not dataset_path.exists():
        return []
    return sorted(str(path) for path in dataset_path.rglob("*.jpg"))
