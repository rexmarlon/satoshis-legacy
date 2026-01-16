# Build Instructions - Satoshis Legacy

## ⚠️ Important Note

This is **Bitcoin v0.3.19** code from December 2010. It was designed for:
- Windows XP / Vista / 7
- Visual Studio 2008
- wxWidgets 2.9.0

Building this today requires some creativity!

---

## 🖥️ Option 1: Windows (Original Method)

### Prerequisites
1. Visual Studio 2008 (or compatible)
2. wxWidgets 2.9.0
3. OpenSSL 1.0.x
4. Berkeley DB 4.8
5. Boost 1.43

### Build Steps
```batch
# Set up environment variables
set WXWIN=C:\wxWidgets-2.9.0
set OPENSSL_ROOT=C:\OpenSSL
set BDB_ROOT=C:\db-4.8.30.NC

# Build with Visual Studio
devenv bitcoin.sln /build Release
```

---

## 🐧 Option 2: Linux (MinGW Cross-Compile)

### Prerequisites
```bash
sudo apt-get install build-essential mingw-w64
sudo apt-get install libssl-dev libdb++-dev libboost-all-dev
```

### Build Steps
```bash
cd src
make -f makefile.unix
```

---

## 🍎 Option 3: macOS

See `build-osx.txt` in the src directory.

---

## 🐳 Option 4: Docker (Recommended for 2024+)

Coming soon - We're working on a Docker image that replicates the 2010 build environment.

```bash
# Future:
docker build -t satoshis-legacy .
docker run satoshis-legacy
```

---

## 🔧 What Was Changed

Only **3 things** were modified from Satoshi's original code:

| File | Change | Reason |
|------|--------|--------|
| `main.cpp:2045` | Magic bytes: `0xf9,0xbe,0xb4,0xd9` → `0x53,0x4c,0x45,0x47` | Separate network |
| `net.h:15` | Ports: `8333/18333` → `9333/19333` | Separate network |
| `net.cpp:810` | Seed nodes → empty | No connection to BTC |

Everything else is **100% original Satoshi code!**

---

## 📝 First Run

After building, you can start your own genesis block:

```bash
# Start the client
./bitcoin

# Or run as daemon
./bitcoind

# Mine the genesis block (first time)
# The client will create a new blockchain!
```

---

## 🆘 Troubleshooting

### "Missing dependencies"
The original code depends on libraries from 2010. You may need to:
- Use a VM with Windows XP/7
- Find archived versions of the libraries
- Modify the makefile for modern compilers

### "Compiler errors"
The code uses C++03 standards. Modern compilers may complain about:
- `auto_ptr` (deprecated)
- `bind1st/bind2nd` (removed in C++17)
- Various other deprecations

Use compiler flags like `-std=c++03` or `-std=c++11` with compatibility flags.

---

## 📚 Original Build Docs

- [build-msw.txt](../src/build-msw.txt) - Windows build instructions
- [build-unix.txt](../src/build-unix.txt) - Linux build instructions  
- [build-osx.txt](../src/build-osx.txt) - macOS build instructions
