// ==UserScript==
// @name         Bazaar APK Downloader
// @version      2.0
// @description  Download APK without installing Cafe Bazar app
// @author       Legendaryking
// @match        https://cafebazaar.ir/*
// @grant        none
// @icon         https://s.cafebazaar.ir/images/icons/com.farsitel.bazaar-b413fb72-5dc4-4a2d-b2a3-7cf567cb6650_512x512.png
// ==/UserScript==

const showMessage = message => {
    const notification = document.createElement('div');
    notification.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,0.8);color:white;padding:10px 20px;border-radius:5px;';
    notification.innerText = message;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
};

const handleApiResponse = (data) => {
    const urls = data.singleReply?.appDownloadInfoReply?.fullPathUrls;
    if (!urls?.length) return showMessage("Error: Invalid data");
    const { packageSize } = data.singleReply.appDownloadInfoReply;
    const fileSize = (packageSize / 1024 / 1024).toFixed(2);
    if (confirm(`Download this app?\n\nSize: ${fileSize}MB`)) window.location.href = urls[urls.length - 1];
};

const fetchData = (pkg, sdk = 33) => {
    if (!pkg) return showMessage("Invalid package");
    fetch("https://api.cafebazaar.ir/rest-v1/process/AppDownloadInfoRequest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ properties: { language: 2, clientVersionCode: 1100301, androidClientInfo: { sdkVersion: sdk, cpu: "x86,armeabi-v7a,armeabi" }, clientVersion: "11.3.1" }, singleRequest: { appDownloadInfoRequest: { packageName: pkg, downloadStatus: 1 } } })
    }).then(res => res.ok ? res.json() : Promise.reject())
      .then(handleApiResponse)
      .catch(() => sdk === 25 ? showMessage("Error fetching data") : fetchData(pkg, 25));
};

const observer = new MutationObserver(() => {
    const downloadSheet = document.querySelector(".DownloadSheet");
    if (downloadSheet) downloadSheet.remove();
    document.querySelectorAll('a').forEach(a => a.addEventListener("click", handleClick));
});

observer.observe(document.body, { childList: true, subtree: true });

const handleClick = () => setTimeout(() => fetchData(window.location.pathname.split('/')[2]), 2000);
