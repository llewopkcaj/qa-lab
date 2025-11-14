import datetime
import pathlib


def pytest_configure(config):
    """Auto-generate timestamped HTML reports for every run."""
    # Create reports/ folder at project root
    reports_dir = pathlib.Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"report_{timestamp}.html"

    # Apply it unless user already set --html
    if not any("--html" in arg for arg in config.invocation_params.args):
        config.option.htmlpath = str(report_path)
        config.option.self_contained_html = True
