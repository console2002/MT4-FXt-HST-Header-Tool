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
The script will scan and print readable headers for all .hst and .fxt files in the folder.

📁 FXT File Header (v405)
Offset (Hex)	Field Name	Type	Description
0x000	FXT Version	int32	FXT file format version
0x004	Copyright	char[64]	Copyright info (MetaQuotes)
0x044	Server Name	char[32]	Broker/server name
0x0C4	Symbol	char[12]	Trading symbol (e.g. "SPX500(£)")
0x0D0	Period	int32	Chart timeframe in minutes (e.g. 60 = H1)
0x0D4	Model	int32	Backtest model type (0=EveryTick, etc.)
0x0D8	Bars	int32	Number of bars in the file
0x0DC	From	int32	Start time (Unix timestamp, GMT)
0x0E0	To	int32	End time (Unix timestamp, GMT)
0x0E4	Spread	int32	Fixed spread in points
0x100	Digits	int32	Number of decimal digits
0x104	Mode	int32	Unknown purpose
0x10C	Forward Date	int32	Forward test start date (Unix timestamp)
0x180	Lot Size	double	Lot size (contract size, e.g. 1.0)
0x188	Tick Size	double	Tick size (e.g. 0.1 for SPX500)

📁 HST File Header (v400)
Offset (Dec)	Field Name	Type	Description
0	HST Version	int32	HST file format version
4	Copyright	char[64]	Copyright info
68	Symbol	char[12]	Symbol name
80	Period	int32	Timeframe (e.g. 60 = H1)
84	Digits	int32	Number of decimal digits
88	Timesign	int32	File creation timestamp (Unix format)
92	Last Sync	int32	Last sync or update timestamp



📜 License
This project is licensed under the MIT License.
