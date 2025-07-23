# MT4 Header Scanner

A lightweight Python tool to scan and decode **MetaTrader 4 FXT and HST file headers**.

---

## 🔧 Features

- Parses FXT (v405) and HST (v400) files  
- Displays key fields: Symbol, Period, Bars, Digits, Timestamps, etc.  
- Based on actual file structure and verified offset mapping  
- Developed for debugging historical data or custom testing setups

---

## 🚀 How to Use

1. Ensure [Python 3.x](https://www.python.org/downloads/) is installed on your system.
2. Place the `History_Header_Scan.py` and `ScanHeaders.bat` files into the same folder as your `.hst` or `.fxt` files.
3. Double-click `ScanHeaders.bat` or run the script from a terminal:

   ```bash
   python History_Header_Scan.py
   

📁 FXT File Header (v405)
| Field Name   | Type       | Offset (Hex) | Description                               |
| ------------ | ---------- | ------------ | ----------------------------------------- |
| FXT Version  | `int32`    | `0x000`      | FXT file format version                   |
| Copyright    | `char[64]` | `0x004`      | Copyright info (MetaQuotes)               |
| Server Name  | `char[32]` | `0x044`      | Broker/server name                        |
| Symbol       | `char[12]` | `0x0C4`      | Trading symbol (e.g. "SPX500(£)")         |
| Period       | `int32`    | `0x0D0`      | Chart timeframe in minutes (e.g. 60 = H1) |
| Model        | `int32`    | `0x0D4`      | Backtest model type (0=EveryTick, etc.)   |
| Bars         | `int32`    | `0x0D8`      | Number of bars in the file                |
| From         | `int32`    | `0x0DC`      | Start time (Unix timestamp, GMT)          |
| To           | `int32`    | `0x0E0`      | End time (Unix timestamp, GMT)            |
| Spread       | `int32`    | `0x0E4`      | Fixed spread in points                    |
| Digits       | `int32`    | `0x100`      | Number of decimal digits                  |
| Mode         | `int32`    | `0x104`      | Unknown purpose                           |
| Forward Date | `int32`    | `0x10C`      | Forward test start date (Unix timestamp)  |
| Lot Size     | `double`   | `0x180`      | Lot size (contract size, e.g. 1.0)        |
| Tick Size    | `double`   | `0x188`      | Tick size (e.g. 0.1 for SPX500)           |

📁 HST File Header (v400)
| Field Name  | Type       | Offset (Dec) | Description                           |
| ----------- | ---------- | ------------ | ------------------------------------- |
| HST Version | `int32`    | `0`          | HST file format version               |
| Copyright   | `char[64]` | `4`          | Copyright info                        |
| Symbol      | `char[12]` | `68`         | Symbol name                           |
| Period      | `int32`    | `80`         | Timeframe (e.g. 60 = H1)              |
| Digits      | `int32`    | `84`         | Number of decimal digits              |
| Timesign    | `int32`    | `88`         | File creation timestamp (Unix format) |
| Last Sync   | `int32`    | `92`         | Last sync or update timestamp         |

🖼️ Screenshot
This is an example of the script output when scanning FXT and HST files:

<img width="507" height="258" alt="image" src="https://github.com/user-attachments/assets/28604ff6-9451-4199-b325-a7beeb170b65" />


