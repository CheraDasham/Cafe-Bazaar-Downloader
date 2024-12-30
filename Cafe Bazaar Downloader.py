import re
import requests

def extract_package_name(url):
    if match := re.search(r"https://cafebazaar\.ir/app/(?:\?id=)?([\w.-]+)", url):
        return match.group(1)
    raise ValueError("Invalid URL format")

def get_app_info(package_name):
    url = 'https://api.cafebazaar.ir/rest-v1/process/AppDetailsV2Request'
    payload = {"properties": {"androidClientInfo": {"sdkVersion": 22}},"singleRequest": {"appDetailsV2Request": {"packageName": package_name}}}
    
    response = requests.post(url, json=payload).json().get('singleReply', {}).get('appDetailsV2Reply', {}).get('meta', {})
    return (
        response.get('name', 'N/A'),
        response.get('reviewInfo', {}).get('averageRate', 'N/A'),
        response.get('category', {}).get('name', 'N/A'),
        response.get('installCount', {}).get('range', 'N/A'),
        response.get('lastUpdated', 'N/A')
    )

def call_download_api(pkg, sdk, retry=True, retries=3):
    url, payload = "https://api.cafebazaar.ir/rest-v1/process/AppDownloadInfoRequest", {
        "properties": {"language": 2, "clientVersionCode": 1100301, "androidClientInfo": {"sdkVersion": sdk, "cpu": "x86,armeabi-v7a,armeabi"}, "clientVersion": "11.3.1", "isKidsEnabled": False},
        "singleRequest": {"appDownloadInfoRequest": {"downloadStatus": 1, "packageName": pkg, "referrers": []}}
    }
    response = requests.post(url, json=payload).json()
    if data := response.get("singleReply", {}).get("appDownloadInfoReply"):
        return handle_response(data)
    if retry and retries: 
        return call_download_api(pkg, 25, retry=False, retries=retries-1)
    raise ValueError("API request failed or abnormal response")

def handle_response(data):
    download_urls = data.get("fullPathUrls", [])
    if not download_urls: raise ValueError("Download URLs are empty")
    return download_urls[-1], int(data.get("packageSize", 0)) / 1024 / 1024, data.get("versionCode", 0)

if __name__ == "__main__":
    try:
        url = input("Enter the URL: ")
        package_name = extract_package_name(url)
        app_name, average_rate, category, install_count_range, last_updated = get_app_info(package_name)

        print(f"App Name: {app_name}\nAverage Rate: {average_rate}\nCategory: {category}\nInstall Count Range: {install_count_range}\nLast Updated: {last_updated}")
        
        download_link, file_size, version_code = call_download_api(package_name, 33)
        
        print(f"File size: {file_size:.2f} MB\nVersion: {version_code}\n\033[1;32mDownload link: \033[0m{download_link}\033[0m")

    except Exception as e:
        print(f"There's an error here: {e}")