# ORBITIQ iOS App — Build Guide
### From this folder to running on your iPhone in ~15 minutes

---

## Prerequisites (check these first)

| Tool | Check | Install |
|------|-------|---------|
| Node.js 18+ | `node -v` | https://nodejs.org |
| Xcode 15+ | Mac App Store | App Store → Xcode |
| Xcode CLI tools | `xcode-select --install` | Run in Terminal |
| CocoaPods | `pod --version` | `sudo gem install cocoapods` |
| Apple Developer account | Free account works for device testing | https://developer.apple.com |

---

## Step 1 — Install dependencies

```bash
cd /path/to/orbitiq-ios
npm install
```

---

## Step 2 — Add iOS platform

```bash
npx cap add ios
```

This creates the `ios/` folder with a full Xcode project inside.

---

## Step 3 — Sync web assets to iOS

```bash
npx cap sync ios
```

This copies `www/index.html` into the Xcode project and installs CocoaPods.

---

## Step 4 — Open in Xcode

```bash
npx cap open ios
```

Xcode will open automatically with `App.xcworkspace`.

---

## Step 5 — Configure signing in Xcode

1. In Xcode, click **App** in the left sidebar (the top-level project)
2. Go to **Signing & Capabilities** tab
3. Under **Team**, select your Apple ID (add one in Xcode → Settings → Accounts if needed)
4. Change **Bundle Identifier** to: `com.yourname.orbitiq`
   (must be unique — use your name, e.g. `com.mahinaeroai.orbitiq`)
5. Xcode will auto-manage provisioning profiles

---

## Step 6 — App icon (optional but recommended)

Replace the default icon with a space-themed one:
1. In Xcode, open `Assets.xcassets` → `AppIcon`
2. Drag your 1024×1024 PNG icon into the slot
3. Xcode auto-generates all required sizes

**Quick icon idea:** Dark background (#050810) with the 🛰 emoji or a white orbit ring SVG

---

## Step 7 — Run on your iPhone

**On simulator:**
- Select any iPhone simulator from the device dropdown in Xcode
- Press ▶ (Cmd+R)

**On real iPhone:**
1. Connect your iPhone via USB
2. On iPhone: Settings → Privacy & Security → Developer Mode → ON
3. Trust your Mac when prompted on the iPhone
4. Select your iPhone from the device dropdown in Xcode
5. Press ▶ (Cmd+R)
6. First run: on iPhone go to Settings → General → VPN & Device Management → trust your developer certificate

---

## Step 8 — After any HTML changes

When you edit `www/index.html`, re-sync and reopen:

```bash
npx cap sync ios
npx cap open ios
```

Then rebuild in Xcode (Cmd+R).

---

## Step 9 — App Store submission (optional)

1. In Xcode: Product → Archive
2. In Organizer window: Distribute App → App Store Connect
3. Fill in metadata from `ios-config/AppStore_Metadata.md`
4. Submit for review (~24 hours)

**Note:** App Store requires a paid Apple Developer account ($99/year).
For personal use and TestFlight, a free account is enough.

---

## Troubleshooting

**CocoaPods error during `cap sync`:**
```bash
cd ios/App && pod install --repo-update && cd ../..
```

**"Untrusted Developer" on iPhone:**
Settings → General → VPN & Device Management → your email → Trust

**White screen on launch:**
- Check that `www/index.html` exists
- Run `npx cap sync ios` again
- In Xcode: Clean Build Folder (Cmd+Shift+K) then rebuild

**Fonts not loading (offline):**
The app uses Google Fonts via CDN. Add these to your `www/` folder for offline use:
```bash
# Download fonts locally
curl -o www/fonts.css "https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700&family=Rajdhani:wght@400;500;600;700&display=swap"
```
Then update the `@import` in `index.html` to `./fonts.css`.

---

## Project Structure After `cap add ios`

```
orbitiq-ios/
├── www/
│   └── index.html          ← Your ORBITIQ app (edit this)
├── ios/
│   ├── App/
│   │   ├── App/
│   │   │   ├── Info.plist  ← Add keys from ios-config/Info.plist.additions.xml
│   │   │   └── Assets.xcassets/AppIcon.appiconset/
│   │   └── App.xcworkspace ← Open THIS in Xcode (not .xcodeproj)
│   └── Podfile
├── capacitor.config.ts
├── package.json
└── ios-config/
    ├── BUILD_GUIDE.md      ← This file
    ├── Info.plist.additions.xml
    └── AppStore_Metadata.md
```

---

*Built with Capacitor 6 · Targets iOS 14+ · Compatible with iPhone and iPad*
