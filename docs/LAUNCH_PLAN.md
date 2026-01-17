# 🚀 SATOSHIS LEGACY - Fair Launch Plan

## Konzept: Fair Launch

**Ziel:** Alle starten gleichzeitig. Kein Premine. Kein Vorteil für Insider.

---

## 📅 Launch-Countdown

| Phase | Zeitraum | Status |
|-------|----------|--------|
| **Vorbereitung** | Jetzt | 🔄 In Arbeit |
| **Community Aufbau** | 2-4 Wochen | ⏳ Geplant |
| **Genesis Block** | TBD (Datum festlegen!) | ⏳ Geplant |
| **Mining Start** | Sofort nach Genesis | ⏳ Geplant |

---

## ✅ Bereits erledigt

- [x] Bitcoin Core v30.2 als Basis
- [x] Magic Bytes geändert: `SLEG` (0x53, 0x4c, 0x45, 0x47)
- [x] Port geändert: 9333
- [x] Seed Nodes geleert (frisches Netzwerk)
- [x] GitHub Repository: https://github.com/rexmarlon/satoshis-legacy

---

## 🔧 Noch zu erledigen (VOR Launch)

### Code-Änderungen

- [ ] **Genesis Block Message** festlegen
- [ ] **Genesis Timestamp** = Launch-Datum/Zeit
- [ ] **Genesis nNonce** minen (wird am Launch-Tag gemacht)
- [ ] **Bech32 Prefix** ändern: `bc` → `sleg` oder `sl`
- [ ] **Address Prefix** anpassen (optional, für eigene Adressen)
- [ ] **Build testen** auf Windows/Linux

### Infrastruktur

- [ ] **Seed Nodes** vorbereiten (mind. 2-3 Server)
- [ ] **Website** erstellen
- [ ] **Discord/Telegram** Community
- [ ] **Mining Pool** (optional für Start)
- [ ] **Block Explorer** aufsetzen

---

## 🎯 Genesis Block - Vorbereitung

### Aktuelle Werte (noch Bitcoin!)
```cpp
// Zeile 138 in chainparams.cpp
genesis = CreateGenesisBlock(1231006505, 2083236893, 0x1d00ffff, 1, 50 * COIN);

// Zeile 73-74: Timestamp Message
const char* pszTimestamp = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks";
```

### Neue Werte für Satoshis Legacy
```cpp
// PLACEHOLDER - Wird am Launch-Tag ausgefüllt!
const char* pszTimestamp = "DEINE NACHRICHT HIER - Datum des Genesis Blocks";

// Parameter:
// nTime    = Unix Timestamp des Launch-Datums
// nNonce   = Wird gemined (dauert 1-30 Minuten)
// nBits    = 0x1d00ffff (Standard Bitcoin Difficulty)
// nVersion = 1
// Reward   = 50 * COIN
```

### Genesis Message Vorschläge

Wähle eine Nachricht die für immer in der Blockchain steht:

1. `"Satoshis Legacy - Be Early Again - [DATUM]"`
2. `"The spirit of Satoshi lives on - [DATUM]"`
3. `"Fair Launch for Everyone - [DATUM]"`
4. `"Back to the roots - [DATUM]"`
5. Eigene Idee: ___________________________

---

## 🌐 Website - Struktur

### Domain-Ideen
- satoshislegacy.org
- satoshislegacy.io
- slegcoin.com
- beearlyagain.com

### Website Inhalte
```
/               - Landing Page mit Countdown
/about          - Über das Projekt
/mining         - Mining Anleitung
/download       - Wallet Download
/community      - Discord/Telegram Links
/explorer       - Block Explorer
```

### Landing Page Elemente
- [ ] **Countdown Timer** zum Genesis Block
- [ ] **"Be Early Again"** Slogan
- [ ] Kurze Erklärung was Satoshis Legacy ist
- [ ] Social Links
- [ ] Newsletter Signup

---

## 👥 Community Aufbau

### Plattformen
- [ ] **Discord** Server erstellen
- [ ] **Telegram** Gruppe
- [ ] **Twitter/X** Account
- [ ] **Reddit** Subreddit (r/satoshislegacy)
- [ ] **BitcoinTalk** Announcement Thread

### Content für Launch
- [ ] Announcement Post
- [ ] Mining Guide
- [ ] Wallet Setup Guide
- [ ] FAQ

---

## ⛏️ Mining am Launch-Tag

### Ablauf
1. **T-0:** Genesis Block wird erstellt und committed
2. **T+1min:** Binaries werden released
3. **T+5min:** Seed Nodes sind online
4. **T+10min:** Erste Miner verbinden sich
5. **Mining beginnt!**

### Seed Nodes
```
# Müssen VOR Launch konfiguriert werden
sleg-seed1.example.com:9333
sleg-seed2.example.com:9333
sleg-seed3.example.com:9333
```

---

## 📊 Tokenomics

| Parameter | Wert |
|-----------|------|
| Max Supply | 21.000.000 SLEG |
| Block Reward | 50 SLEG (Start) |
| Halving | Alle 210.000 Blocks |
| Block Time | ~10 Minuten |
| Algorithm | SHA-256 (PoW) |
| Premine | **0 (NULL!)** |

---

## 🗓️ Vorgeschlagener Zeitplan

### Option A: Schneller Launch (2 Wochen)
- Woche 1: Website + Community
- Woche 2: Testing + Genesis Block

### Option B: Gründlicher Launch (4 Wochen)
- Woche 1-2: Website + Community aufbauen
- Woche 3: Beta Testing mit Community
- Woche 4: Genesis Block + Launch

### Option C: Großer Launch (6-8 Wochen)
- Marketing Kampagne
- Influencer outreach
- Größere Community zum Start

---

## 📝 Notizen

```
Launch Datum: ________________
Launch Zeit:  ________________ UTC
Genesis Message: ________________
```

---

## Nächste Schritte

1. **Datum festlegen** für den Genesis Block
2. **Domain kaufen** für die Website  
3. **Discord Server** erstellen
4. **Website bauen** mit Countdown
5. **Community sammeln**
6. **Genesis Block** am Launch-Tag erstellen

---

*"Be Early Again"* 🚀
