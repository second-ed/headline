import argparse

from headline.process import main_process


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cwd", type=str)
    parser.add_argument("src_dir", nargs="?", type=str, default="src")
    parser.add_argument("tests_dir", nargs="?", type=str, default="tests")
    parser.add_argument("sort_type", nargs="?", type=str, default="newspaper")
    parser.add_argument("tests_only", nargs="?", type=bool, default=False)
    parser.add_argument("rename", nargs="?", type=bool, default=False)
    parser.add_argument("suffix", nargs="?", type=str, default="")

    args = parser.parse_args()

    main_process(
        args.cwd,
        args.src_dir,
        args.tests_dir,
        args.sort_type,
        args.tests_only,
        args.rename,
        args.suffix,
    )


if __name__ == "__main__":
    main()
