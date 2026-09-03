from config import API_UPLOAD, API_ALERT, DEVICE_SN, DEVICE_PN
import requests
import json
import time

def twos_complement(hexstr,bits):
    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

def get_watt(data_map, target):
    if target == 'watt_mainc':
        watt_main = twos_complement(data_map.Inverter['Main_Watt_AC'].val_hex(), 32) * 0.1  + twos_complement(data_map.Inverter['Main2_Watt_AC'].val_hex(), 32) * 0.1
        if(watt_main <= 0):
            return watt_main
        else:
            return 0
    
    if target == 'watt_maind':

        watt_main = twos_complement(data_map.Inverter['Main_Watt_AC'].val_hex(), 32) * 0.1  + twos_complement(data_map.Inverter['Main2_Watt_AC'].val_hex(), 32) * 0.1
        if(watt_main >= 0):
            return watt_main
        else:
            return 0
    
    if target == 'watt_bmsc':
        return data_map.Inverter['Pack_Voltage'].val_num() * 0.01 * data_map.Inverter['Battery_Charging_Current'].val_num() * 0.01

    if target == 'watt_bmsd':
        return data_map.Inverter['Pack_Voltage'].val_num() * 0.01 * data_map.Inverter['Battery_Discharging_Current'].val_num() * 0.01
    
    if target == 'watt_load':
        return data_map.Inverter['Local_Load'].val_num()
    
    if target == 'watt_pv':
        return 0
        return data_map.Inverter['1st_Input_Power_High_Word'].val_num() + data_map.Inverter['1st_Input_Power_Low_Word'].val_num() * 0.1 \
             + data_map.Inverter['2nd_Input_Power_High_Word'].val_num() + data_map.Inverter['2nd_Input_Power_Low_Word'].val_num() * 0.1
    return 0

def upload_data(data_map, end_time):
    time_delta = (end_time - time.time())
    time_factor = (time_delta / 3600)

    wc_mainc = get_watt(data_map, 'watt_mainc')
    wc_maind = get_watt(data_map, 'watt_maind')
    wc_bmsc = get_watt(data_map, 'watt_bmsc')
    wc_bmsd = get_watt(data_map, 'watt_bmsd')
    wc_load = get_watt(data_map, 'watt_load')
    wc_pv = get_watt(data_map, 'watt_pv')

    wd_mainc = wc_mainc * time_factor
    wd_maind = wc_maind * time_factor
    wd_bmsc = wc_bmsc * time_factor
    wd_bmsd = wc_bmsd * time_factor
    wd_load = wc_load * time_factor
    wd_pv = wc_pv * time_factor

    soc = int((data_map.Packs[0]['SOC'].val_num() + data_map.Packs[1]['SOC'].val_num()
    + data_map.Packs[2]['SOC'].val_num() + data_map.Packs[3]['SOC'].val_num())/4)
    
    meta = {}
    for name, data in data_map.Inverter.items():
        meta[name] = data.val_str()

    packs = []
    for i in range(4):
        pack_i = {}
        for name, data in data_map.Packs[i].items():
            pack_i[name] = data.val_str()
        packs.append(pack_i)

    #print(json.dumps(meta))

    obj = {
        'SN': DEVICE_SN,
        'PN': DEVICE_PN,
        'WC_MainC': abs(wc_mainc),
        'WC_MainD': abs(wc_maind),
        'WC_BMSC': abs(wc_bmsc),
        'WC_BMSD': abs(wc_bmsd),
        'WC_Load': abs(wc_load),
        'WC_PV': abs(wc_pv),
        
        'WD_MainC': abs(wd_mainc),
        'WD_MainD': abs(wd_maind),
        'WD_BMSC': abs(wd_bmsc),
        'WD_BMSD': abs(wd_bmsd),
        'WD_Load': abs(wd_load),
        'WD_PV': abs(wd_pv),

        'TEMP': data_map.Inverter['Temp'].val_str(),
        'Work_Mode': data_map.Inverter['Working_Mode'].val_str(),
        'Raised_Flags': '{}',
        'SOC': soc,
        'Meta': meta,
        'Packs': packs
        }

    try:
        print(json.dumps(obj))
        x = requests.post(API_UPLOAD, data = json.dumps(obj), timeout = 10)
        print(x.status_code)
        print(x.text)
    except:
        print('API upload failed!')

def upload_alert(msg):
    obj = {
        'SN': DEVICE_SN,
        'MSG': msg
    }
    try:
        print(json.dumps(obj))
        x = requests.post(API_ALERT, data = json.dumps(obj, timeout = 10))
        print(x.status_code)
        print(x.text)
    except:
        print('API alert failed!')