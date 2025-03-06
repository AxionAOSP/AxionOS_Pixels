# AxionOS_Pixels

[![Total Download](https://img.shields.io/github/downloads/AxionAOSP/AxionOS_Pixels/total?label=Total%20Downloads)](https://github.com/AxionAOSP/AxionOS_Pixels/releases)  

## AxionOS Pixel Releases
AxionAOSP builds for Google Pixel devices.

---

## 📌 **Installation Guide**

### ⚠️ **Important Notes:**
- Ensure your bootloader is unlocked.
- **Back up your data** before proceeding, as this process **will wipe your device**.
- Always use the latest recommended firmware for your device.
- If switching from a different **ROM/variant (GMS/VANILLA)**, a clean flash is **mandatory**.

---

### 🔹 **Clean Flash (Recommended for New Users or Switching ROMs)**
1. **Download** the ROM package and relevant files (**boot.img, dtbo.img, vendor_boot.img**).
2. Place the downloaded files in a folder (preferably your **platform-tools** folder).
3. **Reboot to bootloader** (Hold **Power + Volume Down** until Fastboot Mode appears).
4. Open a terminal/command prompt on your PC in the folder containing the files.
5. Run the following commands:

   ```sh
   fastboot flash boot boot.img
   fastboot flash dtbo dtbo.img
   fastboot flash vendor_boot vendor_boot.img
   fastboot reboot recovery
   ```
6. **Format data** via recovery (**only if flashing from another ROM**).
7. Go to **Advanced > Reboot to Recovery**.
8. Select **Apply update > Apply update via ADB**.
9. On your PC, sideload the ROM package:

   ```sh
   adb sideload rom.zip
   ```
   *(Replace `rom.zip` with the actual filename of the downloaded ROM)*
10. If flashing a **vanilla build**, reboot to recovery at 47% completion and sideload **GApps** *(Skip if using a GApps build)*:

   ```sh
   adb sideload gapps.zip
   ```

11. **(Optional)** Flash **Additional** if needed:

   ```sh
   adb sideload addon|magisk.zip
   ```
12. Reboot to system and enjoy AxionOS! 🎉

---

### 🔄 **Updating from an Existing AxionOS Build**
1. **Reboot to recovery** (**Advanced > Reboot to Recovery**).
2. Select **Apply update > Apply update via ADB**.
3. On your PC, sideload the ROM package:

   ```sh
   adb sideload rom.zip
   ```
4. If flashing a **vanilla build**, reboot to recovery at 47% completion and sideload **GApps** *(Skip if using a GApps build)*:

   ```sh
   adb sideload gapps.zip
   ```

5. **(Optional)** Flash **Additional** if needed:

   ```sh
   adb sideload addon|magisk.zip
   ```

---

### 🔄 **Local Update (Pre-1.2 builds onwards only)**
1. **Go to Settings** (**System > System Updates**).
2. Select **Local Update > Select axion package**.
3. Wait for local update to finish.
4. Reboot device once local update is complete.

---

## 🔗 **Useful Links**
- 📥 **MindTheGapps:** [Download Here](https://github.com/MindTheGapps/15.0.0-arm64/releases)
- 🛠 **AxionOS supports signature spoofing for no-root revanced MicroG service:**
  [Download Here](https://github.com/ReVanced/GmsCore/releases/download/v0.3.1.4.240913/app.revanced.android.gms-240913008-signed.apk)

---
