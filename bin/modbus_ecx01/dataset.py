class DataSet:
    def __init__(self, _start_address, _end_address):
        self.start_address = _start_address
        self.end_address = _end_address
        self.val = 0

    def setval(self, _val):
        self.val =  _val

    def val_str(self):
        try:
            result = ''
            for x in self.val:
                if x != '':
                    result += f' {x}'
            return result.strip()
        except:
            return self.val
    
    def val_hex(self):
        try:
            result = '0x'
            for x in self.val:
                if x != '':
                    result += hex(x).lstrip('0x')
            
            if(result == '0x'):
                return '0x0'

            return result
        except:
            return hex(self.val)
    
    def val_num(self):
        return int(self.val_str())

class DataMap:
    Inverter = {}
    Packs = [{}, {}, {}, {}]

    def __init__(self):
        self.Inverter = {}
        self.Packs = [{}, {}, {}, {}]
        self.init_inverter()
        self.init_catl_pack()

    def init_catl_pack(self):
        for i in range(4):
            self.Packs[i]["Protocol_Type"] = DataSet(0x0001, 0x0001)
            self.Packs[i]["Protocol_Version"] = DataSet(0x0002, 0x0002)
            self.Packs[i]["BMS_Firmware_Version1"] = DataSet(0x0003, 0x0003)
            self.Packs[i]["BMS_Firmware_Version2"] = DataSet(0x0004, 0x0004)
            self.Packs[i]["BMS_Hardware_Version1"] = DataSet(0x0005, 0x0005)
            self.Packs[i]["BMS_Hardware_Version2"] = DataSet(0x0006, 0x0006)
            self.Packs[i]["Cell_Num"] = DataSet(0x0010, 0x0010)
            self.Packs[i]["Cell1_Volt"] = DataSet(0x0011, 0x0011)
            self.Packs[i]["Cell2_Volt"] = DataSet(0x0012, 0x0012)
            self.Packs[i]["Cell3_Volt"] = DataSet(0x0013, 0x0013)
            self.Packs[i]["Cell4_Volt"] = DataSet(0x0014, 0x0014)
            self.Packs[i]["Cell5_Volt"] = DataSet(0x0015, 0x0015)
            self.Packs[i]["Cell6_Volt"] = DataSet(0x0016, 0x0016)
            self.Packs[i]["Cell7_Volt"] = DataSet(0x0017, 0x0017)
            self.Packs[i]["Cell8_Volt"] = DataSet(0x0018, 0x0018)
            self.Packs[i]["Cell9_Volt"] = DataSet(0x0019, 0x0019)
            self.Packs[i]["Cell10_Volt"] = DataSet(0x001A, 0x001A)
            self.Packs[i]["Cell11_Volt"] = DataSet(0x001B, 0x001B)
            self.Packs[i]["Cell12_Volt"] = DataSet(0x001C, 0x001C)
            self.Packs[i]["Cell13_Volt"] = DataSet(0x001D, 0x001D)
            self.Packs[i]["Cell14_Volt"] = DataSet(0x001E, 0x001E)
            self.Packs[i]["Cell15_Volt"] = DataSet(0x001F, 0x001F)
            self.Packs[i]["Cell16_Volt"] = DataSet(0x0020, 0x0020)
            self.Packs[i]["Cell17_Volt"] = DataSet(0x0021, 0x0021)
            self.Packs[i]["Cell18_Volt"] = DataSet(0x0022, 0x0022)
            self.Packs[i]["Cell19_Volt"] = DataSet(0x0023, 0x0023)
            self.Packs[i]["Cell20_Volt"] = DataSet(0x0024, 0x0024)
            self.Packs[i]["Temp_Num"] = DataSet(0x0025, 0x0025)
            self.Packs[i]["Temp1"] = DataSet(0x0026, 0x0026)
            self.Packs[i]["Temp2"] = DataSet(0x0027, 0x0027)
            self.Packs[i]["Temp3"] = DataSet(0x0028, 0x0028)
            self.Packs[i]["Temp4"] = DataSet(0x0029, 0x0029)
            self.Packs[i]["Temp5"] = DataSet(0x002A, 0x002A)
            self.Packs[i]["Temp6"] = DataSet(0x002B, 0x002B)
            self.Packs[i]["Temp7"] = DataSet(0x002C, 0x002C)
            self.Packs[i]["Temp8"] = DataSet(0x002D, 0x002D)
            self.Packs[i]["Temp9"] = DataSet(0x002E, 0x002E)
            self.Packs[i]["Temp10"] = DataSet(0x002F, 0x002F)

            self.Packs[i]["Module_Charge_Current"] = DataSet(0x0030, 0x0030)
            self.Packs[i]["Module_Discharge_Current"] = DataSet(0x0031, 0x0031)
            self.Packs[i]["Module_Volt"] = DataSet(0x0032, 0x0032)
            self.Packs[i]["SOC"] = DataSet(0x0033, 0x0033)
            self.Packs[i]["Module_Total_Capacity"] = DataSet(0x0034, 0x0034)

            self.Packs[i]["State_Cell_Num"] = DataSet(0x0040, 0x0040)
            self.Packs[i]["State_1_2_Volt"] = DataSet(0x0041, 0x0041)
            self.Packs[i]["State_3_4_Volt"] = DataSet(0x0042, 0x0042)
            self.Packs[i]["State_5_6_Volt"] = DataSet(0x0043, 0x0043)
            self.Packs[i]["State_7_8_Volt"] = DataSet(0x0044, 0x0044)
            self.Packs[i]["State_9_10_Volt"] = DataSet(0x0045, 0x0045)
            self.Packs[i]["State_11_12_Volt"] = DataSet(0x0046, 0x0046)
            self.Packs[i]["State_13_14_Volt"] = DataSet(0x0047, 0x0047)
            self.Packs[i]["State_15_16_Volt"] = DataSet(0x0048, 0x0048)
            self.Packs[i]["State_17_18_Volt"] = DataSet(0x0049, 0x0049)
            self.Packs[i]["State_19_20_Volt"] = DataSet(0x004A, 0x004A)

            self.Packs[i]["State_Temp_Num"] = DataSet(0x0050, 0x0050)
            self.Packs[i]["State_1_2_Temp"] = DataSet(0x0051, 0x0051)
            self.Packs[i]["State_3_4_Temp"] = DataSet(0x0052, 0x0052)
            self.Packs[i]["State_5_6_Temp"] = DataSet(0x0053, 0x0053)
            self.Packs[i]["State_7_8_Temp"] = DataSet(0x0054, 0x0054)
            self.Packs[i]["State_9_10_Temp"] = DataSet(0x0055, 0x0055)

            self.Packs[i]["Module_Charge_Volt_State"] = DataSet(0x0060, 0x0060)
            self.Packs[i]["Module_DisCharge_Volt_State"] = DataSet(0x0061, 0x0061)
            self.Packs[i]["Cell_Charge_Volt_State"] = DataSet(0x0062, 0x0062)
            self.Packs[i]["Cell_Discharge_Volt_State"] = DataSet(0x0063, 0x0063)
            self.Packs[i]["Module_Charge_Current_State"] = DataSet(0x0064, 0x0064)
            self.Packs[i]["Module_Discharge_Current_State"] = DataSet(0x0065, 0x0065)
            self.Packs[i]["Module_Charge_Temp_State"] = DataSet(0x0066, 0x0066)
            self.Packs[i]["Module_Discharge_Temp_State"] = DataSet(0x0067, 0x0067)
            self.Packs[i]["Cell_Charge_Temp_State"] = DataSet(0x0068, 0x0068)
            self.Packs[i]["Cell_Discharge_Temp_State"] = DataSet(0x0069, 0x0069)
            self.Packs[i]["Charge_Volt_Limit"] = DataSet(0x0070, 0x0070)
            self.Packs[i]["Disharge_Volt_Limit"] = DataSet(0x0071, 0x0071)
            self.Packs[i]["Charge_Current_Limit"] = DataSet(0x0072, 0x0072)
            self.Packs[i]["Discharge_Current_Limit"] = DataSet(0x0073, 0x0073)
            self.Packs[i]["Charge_Discharge_Status"] = DataSet(0x0074, 0x0074)

    def init_etica_pack(self):
        for i in range(4):
            self.Packs[i]["CELL_1"] = DataSet(0x0000, 0x0000)
            self.Packs[i]["CELL_2"] = DataSet(0x0001, 0x0001)
            self.Packs[i]["CELL_3"] = DataSet(0x0002, 0x0002)
            self.Packs[i]["CELL_4"] = DataSet(0x0003, 0x0003)
            self.Packs[i]["CELL_5"] = DataSet(0x0004, 0x0004)
            self.Packs[i]["CELL_6"] = DataSet(0x0005, 0x0005)
            self.Packs[i]["CELL_7"] = DataSet(0x0006, 0x0006)
            self.Packs[i]["CELL_8"] = DataSet(0x0007, 0x0007)
            self.Packs[i]["CELL_9"] = DataSet(0x0008, 0x0008)
            self.Packs[i]["CELL_10"] = DataSet(0x0009, 0x0009)
            self.Packs[i]["CELL_11"] = DataSet(0x000A, 0x000A)
            self.Packs[i]["CELL_12"] = DataSet(0x000B, 0x000B)
            self.Packs[i]["CELL_13"] = DataSet(0x000C, 0x000C)
            self.Packs[i]["CELL_14"] = DataSet(0x000D, 0x000D)
            self.Packs[i]["CELL_15"] = DataSet(0x000E, 0x000E)
            self.Packs[i]["PACK_MV"] = DataSet(30, 30)
            self.Packs[i]["I_C"] = DataSet(31, 31)
            self.Packs[i]["CAPACITY_SPEC"] = DataSet(31, 32)
            self.Packs[i]["DIE_TEMP_01"] = DataSet(33, 33)
            self.Packs[i]["DIE_TEMP_02"] = DataSet(34, 34)
            self.Packs[i]["DIE_EXT_TEMP_01"] = DataSet(35, 35)
            self.Packs[i]["DIE_EXT_TEMP_02"] = DataSet(35, 36)
            self.Packs[i]["DIE_EXT_TEMP_03"] = DataSet(35, 37)
            self.Packs[i]["DIE_EXT_TEMP_04"] = DataSet(35, 38)
            self.Packs[i]["SOC"] = DataSet(40, 40)
            self.Packs[i]["CAPACITY_REAL"] = DataSet(41, 41)
            self.Packs[i]["STATUS"] = DataSet(42, 42)
            self.Packs[i]["PROTECTION"] = DataSet(44, 44)
            self.Packs[i]["MOSS"] = DataSet(45, 45)
            self.Packs[i]["RTC_YEAR"] = DataSet(92, 92)
            self.Packs[i]["RTC_MTH"] = DataSet(93, 93)
            self.Packs[i]["RTC_DATE"] = DataSet(94, 94)
            self.Packs[i]["RTC_HOUR"] = DataSet(95, 95)
            self.Packs[i]["RTC_MIN"] = DataSet(96, 96)
            self.Packs[i]["RTC_SEC"] = DataSet(97, 97)
            self.Packs[i]["SOH"] = DataSet(133, 133)
            self.Packs[i]["PROTECTION_02"] = DataSet(152, 152)
            self.Packs[i]["BAT_MV"] = DataSet(187, 187)

    def init_inverter(self):
        self.Inverter["Model_Name"] = DataSet(0x1000, 0x100F)
        self.Inverter["Serial_Number"] = DataSet(0x1010, 0x101F)
        self.Inverter["Modbus_Protocol_Type"] = DataSet(0x1020, 0x1020)

        self.Inverter["Logger_Version"] = DataSet(0x1028, 0x102F)
        self.Inverter["Primary_CPU_Version"] = DataSet(0x1030, 0x1037)
        self.Inverter["Secondary_CPU_Version"] = DataSet(0x1038, 0x103F)

        self.Inverter["Set_The_Battery_Parameter"] = DataSet(0x0300, 0x0309)

        self.Inverter["Number_For_Battery_String"] = DataSet(0x0302, 0x0302)
        self.Inverter["Battery_Charge_Max_Current_For_One_String "] = DataSet(0x0303, 0x0303)
        self.Inverter["Battery_Charge_Voltage_Max"] = DataSet(0x0304, 0x0304)
        self.Inverter["Battery_Charge_Float_Voltage"] = DataSet(0x0305, 0x0305)

        self.Inverter["Battery_Over_Voltage"] = DataSet(0x0308, 0x0308)
        self.Inverter["Battery_Low_Voltage"] = DataSet(0x0309, 0x0309)
        self.Inverter["Battery_Cut_OFF_Voltage"] = DataSet(0x030A, 0x030A)

        self.Inverter["Battery_Temperature_Compensation_Type"] = DataSet(0x0312, 0x0312)

        self.Inverter["Main_Voltage_AC"] = DataSet(0x1200, 0x1200)
        self.Inverter["Main_Current_AC"] = DataSet(0x1201, 0x1201)

        self.Inverter["Main_Watt_AC_High_Word"] = DataSet(0x1202, 0x1202)
        self.Inverter["Main_Watt_AC_Low_Word"] = DataSet(0x1203, 0x1203)
        self.Inverter["Main_Watt_AC"] = DataSet(0x1202, 0x1203)

        self.Inverter["Main_Frequency"] = DataSet(0x1204, 0x1204)
        self.Inverter["Local_Load_Phase_Voltage"] = DataSet(0x1205, 0x1205)
        self.Inverter["Local_Load_Phase_Current"] = DataSet(0x1206, 0x1206)
        self.Inverter["Local_Load_Phase_High_Word"] = DataSet(0x1207, 0x1207)
        self.Inverter["Local_Load_Phase_Low_Word"] = DataSet(0x1208, 0x1208)
        self.Inverter["Local_Load_Phase_Frequency"] = DataSet(0x1209, 0x1209)


        self.Inverter["1st_Input_Voltage_DC"] = DataSet(0x120F, 0x120F)
        self.Inverter["1st_Input_Current_DC"] = DataSet(0x1210, 0x1210)
        self.Inverter["1st_Input_Power_High_Word"] = DataSet(0x1211, 0x1211)
        self.Inverter["1st_Input_Power_Low_Word"] = DataSet(0x1212, 0x1212)

        self.Inverter["2nd_Input_Voltage_DC"] = DataSet(0x1213, 0x1213)
        self.Inverter["2nd_Input_Current_DC"] = DataSet(0x1214, 0x1214)
        self.Inverter["2nd_Input_Power_High_Word"] = DataSet(0x1215, 0x1215)
        self.Inverter["2nd_Input_Power_Low_Word"] = DataSet(0x1216, 0x1216)

        self.Inverter["3rd_Input_Voltage_DC"] = DataSet(0x1217, 0x1217)
        self.Inverter["3rd_Input_Current_DC"] = DataSet(0x1218, 0x1218)
        self.Inverter["3rd_Input_Power_High_Word"] = DataSet(0x1219, 0x1219)
        self.Inverter["3rd_Input_Power_Low_Word"] = DataSet(0x121A, 0x121A)

        self.Inverter["Inverter_Internal_Temperature"] = DataSet(0x121B, 0x121B)
        self.Inverter["Working_Mode"] = DataSet(0x121C, 0x121C)
        self.Inverter["System_Error_Date_For_Year_Month"] = DataSet(0x121D, 0x121D)
        self.Inverter["System_Error_Date_For_Day_Hour"] = DataSet(0x121E, 0x121E)
        self.Inverter["System_Error_Date_For_Min_Sec"] = DataSet(0x121F, 0x121F)
        self.Inverter["Error_Code"] = DataSet(0x1220, 0x1223)

        self.Inverter["Local_Load"] = DataSet(0x1224, 0x1224)
        self.Inverter["Local_Load_Today_High_Word"] = DataSet(0x1225, 0x1225)
        self.Inverter["Local_Load_Today_Low_Word"] = DataSet(0x1226, 0x1226)
        self.Inverter["Main_Power_Today_High_Word"] = DataSet(0x1227, 0x1227)
        self.Inverter["Main_Power_Today_Low_Word"] = DataSet(0x1228, 0x1228)
        self.Inverter["PV_Power_Today_High_Word"] = DataSet(0x1229, 0x1229)
        self.Inverter["PV_Power_Today_Low_Word"] = DataSet(0x122A, 0x122A)


        self.Inverter["Battery_Voltage"] = DataSet(0x1230, 0x1230)
        self.Inverter["Battery_Temperature"] = DataSet(0x1231, 0x1231)
        self.Inverter["Battery_Charging_Current"] = DataSet(0x1232, 0x1232)
        self.Inverter["Battery_Discharging_Current"] = DataSet(0x1233, 0x1233)
        self.Inverter["Battery_Status"] = DataSet(0x1234, 0x1234)

        self.Inverter["Grid_CT_Voltage_AC"] = DataSet(0x1235, 0x1235)
        self.Inverter["Grid_CT_Current_AC"] = DataSet(0x1236, 0x1236)
        self.Inverter["Grid_CT_Watt_AC_High_Word"] = DataSet(0x1237, 0x1237)
        self.Inverter["Grid_CT_Watt_AC_Low_Word"] = DataSet(0x1238, 0x1238)
        self.Inverter["Grid_CT_Frequency"] = DataSet(0x1239, 0x1239)
        self.Inverter["Grid_CT_Power_Today_High_Word"] = DataSet(0x123A, 0x123A)
        self.Inverter["Grid_CT_Power_Today_Low_Word"] = DataSet(0x123B, 0x123B)


        self.Inverter["Main2_Voltage_AC"] = DataSet(0x1240, 0x1240)
        self.Inverter["Main2_Current_AC"] = DataSet(0x1241, 0x1241)

        self.Inverter["Main2_Watt_AC_High_Word"] = DataSet(0x1242, 0x1242)
        self.Inverter["Main2_Watt_AC_Low_Word"] = DataSet(0x1243, 0x1243)
        self.Inverter["Main2_Watt_AC"] = DataSet(0x1242, 0x1243)

        self.Inverter["Main2_Frequency"] = DataSet(0x1244, 0x1244)
        self.Inverter["Local_Load_Phase2_Voltage"] = DataSet(0x1245, 0x1245)
        self.Inverter["Local_Load_Phase2_Current"] = DataSet(0x1246, 0x1246)
        self.Inverter["Local_Load_Phase2_High_Word"] = DataSet(0x1247, 0x1247)
        self.Inverter["Local_Load_Phase2_Low_Word"] = DataSet(0x1248, 0x1248)
        self.Inverter["Local_Load_Phase2_Frequency"] = DataSet(0x1249, 0x1249)

        self.Inverter["Local_Inv_Phase2_Voltage"] = DataSet(0x124A, 0x124A)
        self.Inverter["Local_Inv_Phase2_Current"] = DataSet(0x124B, 0x124B)
        self.Inverter["Local_Inv_Phase2_Watt_High_Word"] = DataSet(0x124C, 0x124C)
        self.Inverter["Local_Inv_Phase2_Watt_Low_Word"] = DataSet(0x124D, 0x124D)
        self.Inverter["Local_Inv_Phase2_Frequency"] = DataSet(0x124E, 0x124E)

        self.Inverter["Grid2_CT_Current_AC"] = DataSet(0x1250, 0x1250)
        self.Inverter["Grid2_CT_Watt_AC_High_Word"] = DataSet(0x1251, 0x1251)
        self.Inverter["Grid2_CT_Watt_AC_Low_Word"] = DataSet(0x1252, 0x1252)
        self.Inverter["Grid2_CT_Frequency"] = DataSet(0x1253, 0x1253)

        '''
        self.Inverter["Grid3_CT_Current_AC"] = DataSet(0x1255, 0x1255)
        self.Inverter["Grid3_CT_Watt_AC_High_Word"] = DataSet(0x1256, 0x1256)
        self.Inverter["Grid3_CT_Watt_AC_Low_Word"] = DataSet(0x1257, 0x1257)

        
        self.Inverter["Main3_Voltage_AC"] = DataSet(0x1259, 0x1259)
        self.Inverter["Main3_Current_AC"] = DataSet(0x125A, 0x125A)
        self.Inverter["Main3_Watt_AC_High_Word"] = DataSet(0x125B, 0x125B)
        self.Inverter["Main3_Watt_AC_Low_Word"] = DataSet(0x125C, 0x125C)
        self.Inverter["Main3_Frequency"] = DataSet(0x125D, 0x125D)
        self.Inverter["Local_Load_Phase3_Voltage"] = DataSet(0x125E, 0x125E)
        self.Inverter["Local_Load_Phase3_Current"] = DataSet(0x125F, 0x125F)
        self.Inverter["Local_Load_Phase3_High_Word"] = DataSet(0x1260, 0x1260)
        self.Inverter["Local_Load_Phase3_Low_Word"] = DataSet(0x1261, 0x1261)
        self.Inverter["Local_Load_Phase3_Frequency"] = DataSet(0x1262, 0x1262)
        

        self.Inverter["Local_Inv_Phase3_Voltage"] = DataSet(0x1263, 0x1263)
        self.Inverter["Local_Inv_Phase3_Current"] = DataSet(0x1264, 0x1264)
        self.Inverter["Local_Inv_Phase3_Watt_High_Word"] = DataSet(0x1265, 0x1265)
        self.Inverter["Local_Inv_Phase3_Watt_Low_Word"] = DataSet(0x1266, 0x1266)
        self.Inverter["Local_Inv_Phase3_Frequency"] = DataSet(0x1267, 0x1267)
        


        self.Inverter["Grid3_CT_Current_AC_2"] = DataSet(0x1269, 0x1269)
        self.Inverter["Grid3_CT_Watt_AC_High_Word_2"] = DataSet(0x126A, 0x126A)
        self.Inverter["Grid3_CT_Watt_AC_Low_Word_2"] = DataSet(0x126B, 0x126B)
        self.Inverter["Grid3_CT_Frequency_2"] = DataSet(0x126C, 0x126C)
        

        self.Inverter["Phase_Control_Mode"] = DataSet(0x1270, 0x1270)

        self.Inverter["Total_Power_To_Grid_CAN_High_Word) "] = DataSet(0x1272, 0x1272)
        self.Inverter["Total_Power_To_Grid_CAN_Low_Word) "] = DataSet(0x1273, 0x1273)
        self.Inverter["Total_Power_To_Load_CAN_High_Word) "] = DataSet(0x1274, 0x1274)
        self.Inverter["Total_Power_To_Load_CAN_Low_Word) "] = DataSet(0x1275, 0x1275)
        '''

        self.Inverter["AC_Max_Output_Power"] = DataSet(0x0101, 0x0101)
        self.Inverter["AC_Charge_Mode"] = DataSet(0x0102, 0x0102)
        self.Inverter["PF_Control"] = DataSet(0x0103, 0x0103)
        self.Inverter["Hybird_Operation_Mode"] = DataSet(0x010D, 0x010D)
        self.Inverter["Parallel_Mode"] = DataSet(0x010E, 0x010E)
        self.Inverter["Remote_Power_ON_OFF"] = DataSet(0x010F, 0x010F)

        self.Inverter["Schedule1_AC_Charge_Mask"] = DataSet(0x0110, 0x0110)
        self.Inverter["Schedule1_AC_Charge_Start_Time"] = DataSet(0x0111, 0x0111)
        self.Inverter["Schedule1_AC_Charge_End_Time"] = DataSet(0x0112, 0x0112)

        self.Inverter["Schedule2_AC_Charge_Mask"] = DataSet(0x0113, 0x0113)
        self.Inverter["Schedule2_AC_Charge_Start_Time"] = DataSet(0x0114, 0x0114)
        self.Inverter["Schedule2_AC_Charge_End_Time"] = DataSet(0x0115, 0x0115)

        self.Inverter["Schedule3_AC_Charge_Mask"] = DataSet(0x0116, 0x0116)
        self.Inverter["Schedule3_AC_Charge_Start_Time"] = DataSet(0x0117, 0x0117)
        self.Inverter["Schedule3_AC_Charge_End_Time"] = DataSet(0x0118, 0x0118)

        self.Inverter["Schedule4_AC_Charge_Mask"] = DataSet(0x0119, 0x0119)
        self.Inverter["Schedule4_AC_Charge_Start_Time"] = DataSet(0x011A, 0x011A)
        self.Inverter["Schedule4_AC_Charge_End_Time"] = DataSet(0x011B, 0x011B)

        self.Inverter["Schedule5_AC_Charge_Mask"] = DataSet(0x011C, 0x011C)
        self.Inverter["Schedule5_AC_Charge_Start_Time"] = DataSet(0x011D, 0x011D)
        self.Inverter["Schedule5_AC_Charge_End_Time"] = DataSet(0x011E, 0x011E)

        self.Inverter["Schedule1_BatToLoad_Mask"] = DataSet(0x011F, 0x011F)
        self.Inverter["Schedule1_BatToLoad_Start_Time"] = DataSet(0x0120, 0x0120)
        self.Inverter["Schedule1_BatToLoad_End_Time"] = DataSet(0x0121, 0x0121)
        self.Inverter["Schedule1_Out_Power"] = DataSet(0x0122, 0x0122)

        self.Inverter["Schedule2_BatToLoad_Mask"] = DataSet(0x0123, 0x0123)
        self.Inverter["Schedule2_BatToLoad_Start_Time"] = DataSet(0x0124, 0x0124)
        self.Inverter["Schedule2_BatToLoad_End_Time"] = DataSet(0x0125, 0x0125)
        self.Inverter["Schedule2_Out_Power"] = DataSet(0x0126, 0x0126)

        self.Inverter["Schedule3_BatToLoad_Mask"] = DataSet(0x0127, 0x0127)
        self.Inverter["Schedule3_BatToLoad_Start_Time"] = DataSet(0x0128, 0x0128)
        self.Inverter["Schedule3_BatToLoad_End_Time"] = DataSet(0x0129, 0x0129)
        self.Inverter["Schedule3_Out_Power"] = DataSet(0x012A, 0x012A)

        self.Inverter["Schedule4_BatToLoad_Mask"] = DataSet(0x012B, 0x012B)
        self.Inverter["Schedule4_BatToLoad_Start_Time"] = DataSet(0x012C, 0x012C)
        self.Inverter["Schedule4_BatToLoad_End_Time"] = DataSet(0x012D, 0x012D)
        self.Inverter["Schedule4_Out_Power"] = DataSet(0x012E, 0x012E)

        self.Inverter["Schedule5_BatToLoad_Mask"] = DataSet(0x012F, 0x012F)
        self.Inverter["Schedule5_BatToLoad_Start_Time"] = DataSet(0x0130, 0x0130)
        self.Inverter["Schedule5_BatToLoad_End_Time"] = DataSet(0x0131, 0x0131)
        self.Inverter["Schedule5_Out_Power"] = DataSet(0x0132, 0x0132)

        self.Inverter["Schedule1_Power_OFF_Mask"] = DataSet(0x0133, 0x0133)
        self.Inverter["Schedule1_Power_OFF_Start_Time"] = DataSet(0x0134, 0x0134)
        self.Inverter["Schedule1_Power_OFF_End_Time"] = DataSet(0x0135, 0x0135)

        self.Inverter["Stand_Alone_Volt"] = DataSet(0x013A, 0x013A)

        '''
        self.Inverter["AC_Phase1_Max_Output_Power"] = DataSet(0x0140, 0x0140)
        self.Inverter["AC_Phase2_Max_Output_Power"] = DataSet(0x0141, 0x0141)
        self.Inverter["AC_Phase3_Max_Output_Power"] = DataSet(0x0142, 0x0142)
        

        self.Inverter["Main_Max_Output_Power"] = DataSet(0x0144, 0x0144)
        self.Inverter["Main1_Max_Output_Power"] = DataSet(0x0145, 0x0145)
        self.Inverter["Main2_Max_Output_Power"] = DataSet(0x0146, 0x0146)
        self.Inverter["Main3_Max_Output_Power"] = DataSet(0x0147, 0x0147)
        self.Inverter["PV_Charge_To_Battery"] = DataSet(0x0148, 0x0148)
        self.Inverter["Load_ON_OFF"] = DataSet(0x0149, 0x0149)
        self.Inverter["Max_Battery_Discharge_Current"] = DataSet(0x014A, 0x014A)
        '''

        self.Inverter["BMS_Version1"] = DataSet(0x1400, 0x1400)
        self.Inverter["BMS_Version2"] = DataSet(0x1401, 0x1401)
        self.Inverter["Pack_Voltage"] = DataSet(0x1230, 0x1230)
        self.Inverter["Pack_Capacity"] = DataSet(0x1403, 0x1403)
        self.Inverter["RSOC"] = DataSet(0x1404, 0x1404)
        self.Inverter["Pack_Cycle"] = DataSet(0x1405, 0x1405)
        self.Inverter["Temp"] = DataSet(0x121B, 0x121B)
        self.Inverter["OC"] = DataSet(0x1407, 0x1407)
        self.Inverter["CC"] = DataSet(0x1408, 0x1408)
        self.Inverter["Error_Status1"] = DataSet(0x1409, 0x1409)
        self.Inverter["Error_Status2"] = DataSet(0x140A, 0x140A)
        self.Inverter["Max_Temp"] = DataSet(0x140B, 0x140B)
        self.Inverter["Min_Temp"] = DataSet(0x140C, 0x140C)

        '''
        self.Inverter["Pack_1_Cell_1_Voltage"] = DataSet(0x1410, 0x1410)
        self.Inverter["Pack_1_Cell_2_Voltage"] = DataSet(0x1411, 0x1411)
        self.Inverter["Pack_1_Cell_3_Voltage"] = DataSet(0x1412, 0x1412)
        self.Inverter["Pack_1_Cell_4_Voltage"] = DataSet(0x1413, 0x1413)
        self.Inverter["Pack_1_Cell_5_Voltage"] = DataSet(0x1414, 0x1414)
        self.Inverter["Pack_1_Cell_6_Voltage"] = DataSet(0x1415, 0x1415)
        self.Inverter["Pack_1_Cell_7_Voltage"] = DataSet(0x1416, 0x1416)
        self.Inverter["Pack_1_Cell_8_Voltage"] = DataSet(0x1417, 0x1417)
        self.Inverter["Pack_1_Cell_9_Voltage"] = DataSet(0x1418, 0x1418)
        self.Inverter["Pack_1_Cell_10_Voltage"] = DataSet(0x1419, 0x1419)
        self.Inverter["Pack_1_Cell_11_Voltage"] = DataSet(0x141A, 0x141A)
        self.Inverter["Pack_1_Cell_12_Voltage"] = DataSet(0x141B, 0x141B)
        self.Inverter["Pack_1_Cell_13_Voltage"] = DataSet(0x141C, 0x141C)
        self.Inverter["Pack_1_Cell_14_Voltage"] = DataSet(0x141D, 0x141D)
        self.Inverter["Pack_1_Cell_15_Voltage"] = DataSet(0x141E, 0x141E)
        self.Inverter["Pack_1_Cell_16_Voltage"] = DataSet(0x141F, 0x141F)

        self.Inverter["Pack_2_Cell_1_Voltage"] = DataSet(0x1420, 0x1420)
        self.Inverter["Pack_2_Cell_2_Voltage"] = DataSet(0x1421, 0x1421)
        self.Inverter["Pack_2_Cell_3_Voltage"] = DataSet(0x1422, 0x1422)
        self.Inverter["Pack_2_Cell_4_Voltage"] = DataSet(0x1423, 0x1423)
        self.Inverter["Pack_2_Cell_5_Voltage"] = DataSet(0x1424, 0x1424)
        self.Inverter["Pack_2_Cell_6_Voltage"] = DataSet(0x1425, 0x1425)
        self.Inverter["Pack_2_Cell_7_Voltage"] = DataSet(0x1426, 0x1426)
        self.Inverter["Pack_2_Cell_8_Voltage"] = DataSet(0x1427, 0x1427)
        self.Inverter["Pack_2_Cell_9_Voltage"] = DataSet(0x1428, 0x1428)
        self.Inverter["Pack_2_Cell_10_Voltage"] = DataSet(0x1429, 0x1429)
        self.Inverter["Pack_2_Cell_11_Voltage"] = DataSet(0x142A, 0x142A)
        self.Inverter["Pack_2_Cell_12_Voltage"] = DataSet(0x142B, 0x142B)
        self.Inverter["Pack_2_Cell_13_Voltage"] = DataSet(0x142C, 0x142C)
        self.Inverter["Pack_2_Cell_14_Voltage"] = DataSet(0x142D, 0x142D)
        self.Inverter["Pack_2_Cell_15_Voltage"] = DataSet(0x142E, 0x142E)
        self.Inverter["Pack_2_Cell_16_Voltage"] = DataSet(0x142F, 0x142F)

        self.Inverter["Pack_3_Cell_1_Voltage"] = DataSet(0x1430, 0x1430)
        self.Inverter["Pack_3_Cell_2_Voltage"] = DataSet(0x1431, 0x1431)
        self.Inverter["Pack_3_Cell_3_Voltage"] = DataSet(0x1432, 0x1432)
        self.Inverter["Pack_3_Cell_4_Voltage"] = DataSet(0x1433, 0x1433)
        self.Inverter["Pack_3_Cell_5_Voltage"] = DataSet(0x1434, 0x1434)
        self.Inverter["Pack_3_Cell_6_Voltage"] = DataSet(0x1435, 0x1435)
        self.Inverter["Pack_3_Cell_7_Voltage"] = DataSet(0x1436, 0x1436)
        self.Inverter["Pack_3_Cell_8_Voltage"] = DataSet(0x1437, 0x1437)
        self.Inverter["Pack_3_Cell_9_Voltage"] = DataSet(0x1438, 0x1438)
        self.Inverter["Pack_3_Cell_10_Voltage"] = DataSet(0x1439, 0x1439)
        self.Inverter["Pack_3_Cell_11_Voltage"] = DataSet(0x143A, 0x143A)
        self.Inverter["Pack_3_Cell_12_Voltage"] = DataSet(0x143B, 0x143B)
        self.Inverter["Pack_3_Cell_13_Voltage"] = DataSet(0x143C, 0x143C)
        self.Inverter["Pack_3_Cell_14_Voltage"] = DataSet(0x143D, 0x143D)
        self.Inverter["Pack_3_Cell_15_Voltage"] = DataSet(0x143E, 0x143E)
        self.Inverter["Pack_3_Cell_16_Voltage"] = DataSet(0x143F, 0x143F)

        self.Inverter["Pack_4_Cell_1_Voltage"] = DataSet(0x1440, 0x1440)
        self.Inverter["Pack_4_Cell_2_Voltage"] = DataSet(0x1441, 0x1441)
        self.Inverter["Pack_4_Cell_3_Voltage"] = DataSet(0x1442, 0x1442)
        self.Inverter["Pack_4_Cell_4_Voltage"] = DataSet(0x1443, 0x1443)
        self.Inverter["Pack_4_Cell_5_Voltage"] = DataSet(0x1444, 0x1444)
        self.Inverter["Pack_4_Cell_6_Voltage"] = DataSet(0x1445, 0x1445)
        self.Inverter["Pack_4_Cell_7_Voltage"] = DataSet(0x1446, 0x1446)
        self.Inverter["Pack_4_Cell_8_Voltage"] = DataSet(0x1447, 0x1447)
        self.Inverter["Pack_4_Cell_9_Voltage"] = DataSet(0x1448, 0x1448)
        self.Inverter["Pack_4_Cell_10_Voltage"] = DataSet(0x1449, 0x1449)
        self.Inverter["Pack_4_Cell_11_Voltage"] = DataSet(0x144A, 0x144A)
        self.Inverter["Pack_4_Cell_12_Voltage"] = DataSet(0x144B, 0x144B)
        self.Inverter["Pack_4_Cell_13_Voltage"] = DataSet(0x144C, 0x144C)
        self.Inverter["Pack_4_Cell_14_Voltage"] = DataSet(0x144D, 0x144D)
        self.Inverter["Pack_4_Cell_15_Voltage"] = DataSet(0x144E, 0x144E)
        self.Inverter["Pack_4_Cell_16_Voltage"] = DataSet(0x144F, 0x144F)

        self.Inverter["Pack_5_Cell_1_Voltage"] = DataSet(0x1450, 0x1450)
        self.Inverter["Pack_5_Cell_2_Voltage"] = DataSet(0x1451, 0x1451)
        self.Inverter["Pack_5_Cell_3_Voltage"] = DataSet(0x1452, 0x1452)
        self.Inverter["Pack_5_Cell_4_Voltage"] = DataSet(0x1453, 0x1453)
        self.Inverter["Pack_5_Cell_5_Voltage"] = DataSet(0x1454, 0x1454)
        self.Inverter["Pack_5_Cell_6_Voltage"] = DataSet(0x1455, 0x1455)
        self.Inverter["Pack_5_Cell_7_Voltage"] = DataSet(0x1456, 0x1456)
        self.Inverter["Pack_5_Cell_8_Voltage"] = DataSet(0x1457, 0x1457)
        self.Inverter["Pack_5_Cell_9_Voltage"] = DataSet(0x1458, 0x1458)
        self.Inverter["Pack_5_Cell_10_Voltage"] = DataSet(0x1459, 0x1459)
        self.Inverter["Pack_5_Cell_11_Voltage"] = DataSet(0x145A, 0x145A)
        self.Inverter["Pack_5_Cell_12_Voltage"] = DataSet(0x145B, 0x145B)
        self.Inverter["Pack_5_Cell_13_Voltage"] = DataSet(0x145C, 0x145C)
        self.Inverter["Pack_5_Cell_14_Voltage"] = DataSet(0x145D, 0x145D)
        self.Inverter["Pack_5_Cell_15_Voltage"] = DataSet(0x145E, 0x145E)
        self.Inverter["Pack_5_Cell_16_Voltage"] = DataSet(0x145F, 0x145F)

        self.Inverter["Pack_1_Temp"] = DataSet(0x1460, 0x1460)
        self.Inverter["Pack_2_Temp"] = DataSet(0x1461, 0x1461)
        self.Inverter["Pack_3_Temp"] = DataSet(0x1462, 0x1462)
        self.Inverter["Pack_4_Temp"] = DataSet(0x1463, 0x1463)
        self.Inverter["Pack_5_Temp"] = DataSet(0x1464, 0x1464)
        '''
    