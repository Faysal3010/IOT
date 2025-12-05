# IOT
### usb bridge :
https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads
### Firmware হচ্ছে device boot করার আগে যা কাজ করে, যেন হার্ডওয়্যার সচল হয়।
download firmware : https://micropython.org/download/ESP32_GENERIC/





1. Write → Flush → Sync

```
def ota_update(url):
    print("Checking OTA...")
    try:
        r = urequests.get(url)
        if r.status_code == 200:
            with open("main.py", "wb") as f:
                f.write(r.content)
                f.flush()
                os.sync()   # <-- important
            print("OTA Update Done!")
            machine.reset()
    except Exception as e:
        print("OTA Error:", e)

```
os.sync() = flash write নিশ্চিত করে
এটা ajout করার পর update 100% proper write হবে।



2. Safer method (temporary file → replace)

Best practice OTA:
```
import os

tmp = "main_tmp.py"
new = r.content

# write new file
with open(tmp, "wb") as f:
    f.write(new)
    f.flush()
    os.sync()

# replace old file
os.remove("main.py")
os.rename(tmp, "main.py")

machine.reset()

```
🎯 Guarantee:

corrupt file risk zero

partial update হলে পুরাতন কোড safe থাকে
