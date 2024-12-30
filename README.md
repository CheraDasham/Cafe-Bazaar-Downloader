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

__For Tmpermonkey you can use 'Cafe Bazaar Downloader.js'__

## Example

```bash
Enter the URL: https://cafebazaar.ir/app/cab.snapp.passenger
App Name: اسنپ | Snapp سامانه هوشمند حمل و نقل
Average Rate: 4.7
Category: رفت و آمد
Install Count Range: ۴۳،۰۰۰،۰۰۰+
Last Updated: N/A
File size: 64.43 MB
Version: 286
Download link: https://arvancdn.cafebazaar.ir/arvan/apks/300341999278.apk?hash=82d3df76d4fa66e40845b28682d4b013&expires=1735808744&a=.apk
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/EVOL-ution/Cafe-Bazaar-Downloader/blob/main/LICENSE) file for details.
