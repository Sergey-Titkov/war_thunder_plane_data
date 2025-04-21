import glob
import os
import war_thunder_plane_info.wt as wt
import json

# Список самолетов который нам интересен, если пусто, то обработаем все
list_plane = [
    'er-2_m105_tat'
    ]

if __name__ == "__main__":
    # Каталог откуда считываем флат модели
    res = glob.glob(fr'./War-Thunder-Datamine-master/aces.vromfs.bin_u/gamedata/flightmodels/*.blkx')
    # Нет, нет и нет
    exclude = ['h_81a_2']
    result_json = {}
    # Список файлов есть, пошли по нему
    for file in res:
        plane_id = os.path.basename(file).replace('.blkx', '')
        if plane_id not in exclude:
            plane_datamine = wt.WTPlaneFullInfo(plane_id)
            result_json[plane_id]=plane_datamine.get_all()

    with open('wtmfd_data.json', 'w', encoding="utf-8") as file:
        json.dump(result_json, file, ensure_ascii=False)