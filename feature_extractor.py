import pyshark, datetime, math, json, tqdm
import numpy as np
import pandas as pd

FILE_IN = "./output/out_file.pcap"
FILE_OUT = "./output/eps_info.csv"
MODE = 'w'
try:
    df = pd.read_csv(FILE_OUT)
    EMPTY = df.empty
except:
    EMPTY = True
    pass
OUTDOOR = True
SPAN = 60 #seconds

def start():
    cap = pyshark.FileCapture(FILE_IN)
    start = datetime.datetime.timestamp(cap[0].sniff_time)
    times,powers,vendors = [],[],[]
    tt,pp,vv,cc = [],[],[],[]
    cnt = 0
    for i,pkt in tqdm.tqdm(enumerate(cap)):
        current_t = datetime.datetime.timestamp(pkt.sniff_time)
        if SPAN != 0 and current_t - start > SPAN:
            tt.append(times[-1])
            pp.append(round(np.average(powers)))
            vv.append(np.unique(vendors)[0])
            cc.append(cnt)
            start = current_t
            cnt = 0
            times.clear()
            powers.clear()
            vendors.clear()
        cnt += 1
        times.append(pkt.sniff_time)
        powers.append(int(pkt.layers[1]._all_fields.get("wlan_radio.signal_dbm")))
        vendors.append(str(pkt.layers[3]._all_fields.get("wlan.tag.vendor.data")))

    if SPAN == 0:
        df = pd.DataFrame({
            "Times":times,
            "RSSI":powers,
            "Vendors":vendors,
            "Outdoor":[1]*len(times) if OUTDOOR is True else [0*len(times)]
            })
        df.to_csv(FILE_OUT, mode=MODE, header=True)
    else:
        df = pd.DataFrame({
            "Times":tt,
            "#Packets":cc,
            "RSSI":pp,
            "Vendors":vv,
            "Outdoor":1 if OUTDOOR is True else 0
            })
        df.to_csv(FILE_OUT, mode=MODE, header=True)
        
if __name__ == "__main__":
    start()