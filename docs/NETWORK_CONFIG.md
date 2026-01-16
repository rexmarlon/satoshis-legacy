# Satoshis Legacy - Netzwerk-Konfiguration

## Geänderte Parameter (Bitcoin → Satoshis Legacy)

Diese Änderungen wurden vorgenommen um ein separates Netzwerk zu erstellen,
das nicht mit dem echten Bitcoin-Netzwerk interagiert.

### 1. Magic Bytes (main.cpp:2045)
```cpp
// Bitcoin Original:
char pchMessageStart[4] = { 0xf9, 0xbe, 0xb4, 0xd9 };

// Satoshis Legacy:
char pchMessageStart[4] = { 0x53, 0x4c, 0x45, 0x47 }; // "SLEG" in hex
```

### 2. Default Port (net.h:15)
```cpp
// Bitcoin Original:
inline unsigned short GetDefaultPort() { return fTestNet ? htons(18333) : htons(8333); }

// Satoshis Legacy:
inline unsigned short GetDefaultPort() { return fTestNet ? htons(19333) : htons(9333); }
```

### 3. IRC Channel (irc.cpp) - Deaktiviert
Der originale Bitcoin benutzte IRC zur Node-Discovery.
Für Satoshis Legacy wird dies deaktiviert.

### 4. Seed Nodes (net.cpp:810)
Die Original Bitcoin Seed-Nodes wurden entfernt/geleert.

---

## Coin Parameter (UNVERÄNDERT - Original Satoshi!)

| Parameter | Wert | Quelle |
|-----------|------|--------|
| Block Time | 10 Minuten | main.h |
| Max Supply | 21.000.000 | main.cpp |
| Block Reward | 50 SLEG | main.cpp |
| Halving | Alle 210.000 Blocks | main.cpp |
| Difficulty Adjust | Alle 2016 Blocks | main.cpp |
| Mining Algo | SHA-256 | sha256.cpp |

Diese Parameter bleiben **exakt wie von Satoshi designed!**
