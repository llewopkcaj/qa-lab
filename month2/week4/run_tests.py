import datetime
import pathlib
import subprocess


def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = pathlib.Path("/Users/jackpowell/Documents/qa-lab/month2/week4/reports")
    report_dir.mkdir(exist_ok=True)
    report_path = report_dir / f"report_{timestamp}.html"
    cmd = ["pytest", "--html", str(report_path), "--self-contained-html", "-q"]
    print(f"[INFO] Running tests -> {report_path.name}")
    subprocess.run(cmd, check=False)
    print(f"[INFO] Report saved at {report_path.resolve()}")


if __name__ == "__main__":
    main()
