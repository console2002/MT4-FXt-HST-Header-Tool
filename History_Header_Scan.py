import os
import struct
import datetime
print("=" * 60)
print(" FXT & HST Header Scanner")
print(" Developed by James Higgins")
print(" Email: console_2002@yahoo.co.uk")
print("=" * 60)

def parse_hst_header(file_path):
    info = {"File": os.path.basename(file_path), "File Type": "HST"}
    try:
        with open(file_path, "rb") as f:
            data = f.read(148)
        info["HST Version"] = struct.unpack_from("<i", data, 0)[0]
        info["Copyright"] = data[4:68].decode("latin-1", errors="replace").strip("\x00")
        info["Symbol"] = data[68:80].decode("latin-1", errors="replace").strip("\x00")
        info["Period"] = struct.unpack_from("<i", data, 80)[0]
        info["Digits"] = struct.unpack_from("<i", data, 84)[0]
        ts1 = struct.unpack_from("<i", data, 88)[0]
        ts2 = struct.unpack_from("<i", data, 92)[0]
        info["Timesign"] = datetime.datetime.fromtimestamp(ts1, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        info["Last Sync"] = datetime.datetime.fromtimestamp(ts2, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        info["Error"] = str(e)
    return info

def parse_fxt_header(file_path):
    info = {"File": os.path.basename(file_path), "File Type": "FXT"}
    try:
        with open(file_path, "rb") as f:
            data = f.read(1024)

        info["FXT Version"] = struct.unpack_from("<i", data, 0x00)[0]
        info["Copyright"] = data[0x04:0x44].decode("latin-1", errors="replace").strip("\x00")
        info["Server Name"] = data[0x44:0x64].decode("latin-1", errors="replace").strip("\x00")
        info["Symbol"] = data[0xC4:0xD0].decode("latin-1", errors="replace").strip("\x00")
        info["Period"] = struct.unpack_from("<i", data, 0xD0)[0]
        info["Model"] = struct.unpack_from("<i", data, 0xD4)[0]
        info["Bars"] = struct.unpack_from("<i", data, 0xD8)[0]
        ts_from = struct.unpack_from("<i", data, 0xDC)[0]
        ts_to = struct.unpack_from("<i", data, 0xE0)[0]
        info["From"] = datetime.datetime.fromtimestamp(ts_from, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        info["To"] = datetime.datetime.fromtimestamp(ts_to, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        info["Spread"] = struct.unpack_from("<i", data, 0xE4)[0]
        info["Digits"] = struct.unpack_from("<i", data, 0x100)[0]
        info["Mode"] = struct.unpack_from("<i", data, 0x104)[0]
        ts_fwd = struct.unpack_from("<i", data, 0x10C)[0]
        info["ForwardDate"] = datetime.datetime.fromtimestamp(ts_fwd, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        info["Lot Size"] = struct.unpack_from("<d", data, 0x180)[0]
        info["Tick Size"] = struct.unpack_from("<d", data, 0x188)[0]

    except Exception as e:
        info["Error"] = str(e)

    return info

def print_summary(info):
    print(f"\n📝 {info['File']}")
    for k, v in info.items():
        if k != "File":
            print(f"   {k:15}: {v}")

def main():
    folder = os.getcwd()
    print(f"📁 Scanning .hst and .fxt files for header information...\nScanning in {folder}")
    files_found = False
    for fn in os.listdir(folder):
        if fn.lower().endswith(".hst") or fn.lower().endswith(".fxt"):
            files_found = True
            path = os.path.join(folder, fn)
            info = parse_hst_header(path) if fn.lower().endswith(".hst") else parse_fxt_header(path)
            print_summary(info)
    if not files_found:
        print("⚠️ No .hst or .fxt files found.")

if __name__ == "__main__":
    main()
