# Библиотека для работы с датой и временем
import datetime
# Библиотека для работы с числами
import numpy as np


# Класс записей прочтённых из .csv файла
class Record():
    # Конструктор в котором мы передаём данные из каждой строки .csv файла
    def __init__(self,
                 subs_id, month,
                 SMS_in_CNT, SMS_out_CNT,
                 calls_in_CNT, calls_out_CNT,
                 duration_in_min, duration_out_min,
                 data_traffic_MB, sim_LTE,
                 tariff_id, support_3G,
                 support_4G, subs_home_region,
                 charge, recharge,
                 recharge_CNT, life_time,
                 MNP_out
                ):

        self.subs_id = subs_id
        self.date = month
        self.SMS_in_CNT = SMS_in_CNT
        self.SMS_out_CNT = SMS_out_CNT
        self.calls_in_CNT = calls_in_CNT
        self.calls_out_CNT = calls_out_CNT
        self.duration_in_min = duration_in_min
        self.duration_out_min = duration_out_min
        self.data_traffic_MB = data_traffic_MB
        self.sim_LTE = sim_LTE
        self.tariff_id = tariff_id
        self.support_3G = support_3G
        self.support_4G = support_4G
        self.subs_home_region = subs_home_region
        self.charge = charge
        self.recharge = recharge
        self.recharge_CNT = recharge_CNT
        self.life_time = life_time
        self.MNP_out = MNP_out

    def get_filds_to_index(self):
        self.filds_to_index = []
        self.filds_to_index.append(self.SMS_in_CNT)
        self.filds_to_index.append(self.SMS_out_CNT)
        self.filds_to_index.append(self.calls_in_CNT)
        self.filds_to_index.append(self.calls_out_CNT)
        self.filds_to_index.append(self.duration_in_min)
        self.filds_to_index.append(self.duration_out_min)
        self.filds_to_index.append(self.data_traffic_MB)
        self.filds_to_index.append(self.sim_LTE)
        self.filds_to_index.append(self.support_3G)
        self.filds_to_index.append(self.support_4G)
        self.filds_to_index.append(self.subs_home_region)
        self.filds_to_index.append(self.charge)
        self.filds_to_index.append(self.recharge)
        self.filds_to_index.append(self.recharge_CNT)
        self.filds_to_index.append(self.life_time)
        return  len(self.filds_to_index)


    def check_if_not_null(self):
        return False if np.isnan(self.subs_id) \
                        or np.isnan(self.SMS_in_CNT) \
                        or np.isnan(self.SMS_out_CNT) \
                        or np.isnan(self.calls_in_CNT) \
                        or np.isnan(self.calls_out_CNT) \
                        or np.isnan(self.duration_in_min) \
                        or np.isnan(self.duration_out_min) \
                        or np.isnan(self.data_traffic_MB) \
                        or np.isnan(self.sim_LTE) \
                        or np.isnan(self.tariff_id) \
                        or np.isnan(self.support_3G) \
                        or np.isnan(self.support_4G) \
                        or np.isnan(self.subs_home_region) \
                        or np.isnan(self.charge) \
                        or np.isnan(self.recharge) \
                        or np.isnan(self.recharge_CNT) \
                        or np.isnan(self.life_time) \
                        or np.isnan(self.MNP_out) \
            else True