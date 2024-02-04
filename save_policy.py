import argparse
import subprocess
import argparse
import subprocess
from datetime import date
from urllib.parse import urlparse

def save_policy(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    today = date.today().strftime("%Y%m%d")
    output_file = f"Privacy Policies\{domain}_{today}.html"
    subprocess.run(["monolith", url, "-o", output_file])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI to grab a URL and save the content to a file")
    parser.add_argument("url", help="URL to grab")
    args = parser.parse_args()

    save_policy(args.url)
