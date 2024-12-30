# Cafe Bazaar Downloader
This repository contains the code for a simple script that can be used to download apps from Cafe Bazaar.
## Features

- Extracts app name, description, average rating, category, install count range, last updated date, and download link.
- Provides error handling for invalid URLs, connection errors, unexpected API responses, and abnormal API responses.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed.
- Required Python libraries: `re`, `requests`

You can install the required libraries using:

```bash
pip install requests
```

## Usage
1. Run the script
```bash
 python 'Cafe Bazaar Downloader.py'
```
2. Enter Cafe Bazaar app URL when prompted
3. App information and download link will be printed

## Example

```bash
Enter the URL: https://cafebazaar.ir/app/cars.simulator.extreme.drift.drag.bugatti.divo
App Name: رانندگی با سوپرکار باگاتی دیوو ایکس
Average Rate: 2.4
Category: رانندگی
Install Count Range: ۵۰،۰۰۰+
Last Updated: N/A
File size: 106.24 MB
Version: 23
Download link: https://arvancdn.cafebazaar.ir/arvan/apks/630637820407.apk?hash=801d135bbcfad74c763bcca64f7adfb9&expires=1735806147&a=.apk
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/EVOL-ution/Cafe-Bazaar-Downloader/blob/main/LICENSE) file for details.
