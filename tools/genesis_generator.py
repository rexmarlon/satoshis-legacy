#!/usr/bin/env python3
"""
Satoshis Legacy - Genesis Block Generator
==========================================

Dieses Script generiert den Genesis Block für Satoshis Legacy.
Es berechnet den korrekten nNonce durch Mining.

VERWENDUNG AM LAUNCH-TAG:
1. Nachricht und Timestamp anpassen
2. Script ausführen
3. Ausgabe in chainparams.cpp einfügen
4. Kompilieren und releasen!

"""

import hashlib
import struct
import time
from datetime import datetime

# =============================================================================
# KONFIGURATION - VOR DEM LAUNCH ANPASSEN!
# =============================================================================

# Deine Genesis Block Nachricht (max ~100 Zeichen empfohlen)
GENESIS_MESSAGE = "Satoshis Legacy - Be Early Again - 17/Jan/2026"

# Unix Timestamp für den Genesis Block (Launch-Zeit)
# Verwende: int(datetime(2026, 1, 17, 12, 0, 0).timestamp())
GENESIS_TIMESTAMP = 1737111600  # Beispiel: 17. Jan 2026, 12:00 UTC

# Difficulty Bits (Standard Bitcoin)
GENESIS_BITS = 0x1d00ffff

# Block Version
GENESIS_VERSION = 1

# Block Reward (in Satoshis)
GENESIS_REWARD = 50 * 100000000  # 50 SLEG

# =============================================================================
# GENESIS BLOCK GENERATOR - NICHT ÄNDERN!
# =============================================================================

def sha256d(data):
    """Double SHA256 Hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def compact_to_target(bits):
    """Convert compact bits to target"""
    exponent = bits >> 24
    mantissa = bits & 0x007fffff
    if exponent <= 3:
        target = mantissa >> (8 * (3 - exponent))
    else:
        target = mantissa << (8 * (exponent - 3))
    return target

def create_coinbase_script(message):
    """Create coinbase script with message"""
    # Standard Bitcoin genesis coinbase format
    # 04ffff001d0104 + len + message
    msg_bytes = message.encode('utf-8')
    script = bytes([
        0x04, 0xff, 0xff, 0x00, 0x1d,  # bits
        0x01, 0x04,                      # OP_PUSHDATA
        len(msg_bytes)                   # message length
    ]) + msg_bytes
    return script

def create_pubkey_script():
    """Create output script (unspendable for genesis)"""
    # Standard Bitcoin genesis pubkey
    pubkey = bytes.fromhex(
        "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6"
        "49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f"
    )
    return bytes([0x41]) + pubkey + bytes([0xac])  # PUSH65 + pubkey + OP_CHECKSIG

def create_coinbase_tx(timestamp_msg, reward):
    """Create the coinbase transaction"""
    # Version (4 bytes)
    tx = struct.pack('<I', 1)
    
    # Input count
    tx += bytes([1])
    
    # Previous output (null for coinbase)
    tx += bytes(32)  # prev hash
    tx += struct.pack('<I', 0xffffffff)  # prev index
    
    # Coinbase script
    coinbase_script = create_coinbase_script(timestamp_msg)
    tx += bytes([len(coinbase_script)])
    tx += coinbase_script
    
    # Sequence
    tx += struct.pack('<I', 0xffffffff)
    
    # Output count
    tx += bytes([1])
    
    # Output value
    tx += struct.pack('<Q', reward)
    
    # Output script
    pubkey_script = create_pubkey_script()
    tx += bytes([len(pubkey_script)])
    tx += pubkey_script
    
    # Locktime
    tx += struct.pack('<I', 0)
    
    return tx

def calculate_merkle_root(tx):
    """Calculate merkle root from single transaction"""
    return sha256d(tx)

def create_block_header(version, prev_hash, merkle_root, timestamp, bits, nonce):
    """Create block header"""
    header = struct.pack('<I', version)
    header += prev_hash
    header += merkle_root
    header += struct.pack('<I', timestamp)
    header += struct.pack('<I', bits)
    header += struct.pack('<I', nonce)
    return header

def mine_genesis_block(message, timestamp, bits, version, reward):
    """Mine the genesis block by finding valid nonce"""
    
    print("=" * 60)
    print("SATOSHIS LEGACY - GENESIS BLOCK MINER")
    print("=" * 60)
    print(f"\nMessage: {message}")
    print(f"Timestamp: {timestamp} ({datetime.fromtimestamp(timestamp)})")
    print(f"Bits: 0x{bits:08x}")
    print(f"Reward: {reward / 100000000} SLEG")
    print("\n" + "=" * 60)
    
    # Create coinbase transaction
    coinbase_tx = create_coinbase_tx(message, reward)
    merkle_root = calculate_merkle_root(coinbase_tx)
    
    print(f"\nMerkle Root: {merkle_root[::-1].hex()}")
    
    # Previous block hash (null for genesis)
    prev_hash = bytes(32)
    
    # Calculate target from bits
    target = compact_to_target(bits)
    
    print(f"Target: {target:064x}")
    print("\nMining genesis block... (this may take a while)")
    print("-" * 60)
    
    nonce = 0
    start_time = time.time()
    last_update = start_time
    
    while True:
        # Create header with current nonce
        header = create_block_header(version, prev_hash, merkle_root, timestamp, bits, nonce)
        
        # Hash the header
        block_hash = sha256d(header)
        hash_int = int.from_bytes(block_hash, 'little')
        
        # Check if valid
        if hash_int < target:
            elapsed = time.time() - start_time
            print(f"\n{'=' * 60}")
            print("GENESIS BLOCK FOUND!")
            print(f"{'=' * 60}")
            print(f"\nTime elapsed: {elapsed:.2f} seconds")
            print(f"Nonce: {nonce}")
            print(f"Block Hash: {block_hash[::-1].hex()}")
            print(f"Merkle Root: {merkle_root[::-1].hex()}")
            
            return {
                'nonce': nonce,
                'hash': block_hash[::-1].hex(),
                'merkle_root': merkle_root[::-1].hex(),
                'timestamp': timestamp,
                'bits': bits,
                'message': message
            }
        
        nonce += 1
        
        # Progress update every 10 seconds
        if time.time() - last_update > 10:
            elapsed = time.time() - start_time
            hashrate = nonce / elapsed
            print(f"  Nonce: {nonce:,} | Hashrate: {hashrate:.0f} H/s | Time: {elapsed:.0f}s")
            last_update = time.time()
        
        # Safety limit (shouldn't be reached with standard difficulty)
        if nonce > 0xffffffff:
            print("ERROR: Nonce overflow! Check your parameters.")
            return None

def generate_cpp_code(result):
    """Generate C++ code for chainparams.cpp"""
    
    code = f'''
// =============================================================================
// SATOSHIS LEGACY - GENESIS BLOCK
// Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
// =============================================================================

// Zeile ~73 in chainparams.cpp - CreateGenesisBlock Funktion anpassen:
static CBlock CreateGenesisBlock(uint32_t nTime, uint32_t nNonce, uint32_t nBits, int32_t nVersion, const CAmount& genesisReward)
{{
    const char* pszTimestamp = "{result['message']}";
    const CScript genesisOutputScript = CScript() << "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f"_hex << OP_CHECKSIG;
    return CreateGenesisBlock(pszTimestamp, genesisOutputScript, nTime, nNonce, nBits, nVersion, genesisReward);
}}

// Zeile ~138 in chainparams.cpp - CMainParams Konstruktor:
genesis = CreateGenesisBlock({result['timestamp']}, {result['nonce']}, 0x{result['bits']:08x}, 1, 50 * COIN);
consensus.hashGenesisBlock = genesis.GetHash();
assert(consensus.hashGenesisBlock == uint256{{"{result['hash']}"}});
assert(genesis.hashMerkleRoot == uint256{{"{result['merkle_root']}"}});

// =============================================================================
'''
    return code

def main():
    print("\n" + "=" * 60)
    print(" SATOSHIS LEGACY - GENESIS BLOCK GENERATOR")
    print("=" * 60)
    print(f"\n WARNUNG: Dieses Script wird den Genesis Block minen!")
    print(" Stelle sicher, dass alle Parameter korrekt sind!")
    print("\n Aktuelle Konfiguration:")
    print(f"   Message:   {GENESIS_MESSAGE}")
    print(f"   Timestamp: {GENESIS_TIMESTAMP}")
    print(f"             ({datetime.fromtimestamp(GENESIS_TIMESTAMP)})")
    print(f"   Bits:      0x{GENESIS_BITS:08x}")
    print(f"   Reward:    {GENESIS_REWARD / 100000000} SLEG")
    
    confirm = input("\n Fortfahren? (ja/nein): ")
    if confirm.lower() not in ['ja', 'yes', 'y', 'j']:
        print(" Abgebrochen.")
        return
    
    # Mine the genesis block
    result = mine_genesis_block(
        GENESIS_MESSAGE,
        GENESIS_TIMESTAMP,
        GENESIS_BITS,
        GENESIS_VERSION,
        GENESIS_REWARD
    )
    
    if result:
        # Generate C++ code
        cpp_code = generate_cpp_code(result)
        
        print("\n" + "=" * 60)
        print(" C++ CODE FÜR chainparams.cpp:")
        print("=" * 60)
        print(cpp_code)
        
        # Save to file
        with open("genesis_block_output.txt", "w") as f:
            f.write(cpp_code)
        
        print("\n Code wurde auch in 'genesis_block_output.txt' gespeichert!")
        print("\n" + "=" * 60)
        print(" NÄCHSTE SCHRITTE:")
        print("=" * 60)
        print(" 1. Kopiere den Code in src/kernel/chainparams.cpp")
        print(" 2. Kompiliere das Projekt neu")
        print(" 3. Starte die Seed Nodes")
        print(" 4. Release die Binaries")
        print(" 5. MINING KANN BEGINNEN! 🚀")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
