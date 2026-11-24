import os
from pathlib import Path

LINE = (
    "We broke it: during a 'quick cleanup' we deleted the very table your account "
    "lives in — your data is backed up and restoring now; our dignity was not "
    "backed up anywhere."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
