import glob
import os
import war_thunder_plane_info.wt as wt
import json
from packaging import version
import shutil
# Список самолетов который нам интересен, если пусто, то обработаем все
list_plane = [
    'er-2_m105_tat'
    ]

if __name__ == "__main__":
    with open(fr'./War-Thunder-Datamine-master/version', 'r', encoding="utf-8") as file:
        datamine_version = version.parse(file.read())

    with open('wtmfd_data_version.json', 'r', encoding="utf-8") as file:
        json_version = version.parse(json.load(file)["Version"])
    # У нас новые данные по флайт модели, обновляемся
    if datamine_version > json_version:
        shutil.copy2('wtmfd_data.json', f'wtmfd_data {json_version}.json')
        shutil.copy2('wtmfd_data_version.json', f'wtmfd_data_verion {json_version}.json')

        # Каталог откуда считываем флат модели
        res = glob.glob(fr'./War-Thunder-Datamine-master/aces.vromfs.bin_u/gamedata/flightmodels/*.blkx')
        # Нет, нет и нет
        exclude = ['h_81a_2']
        result_json = {}

        plane_names = wt.WTUnitsName(fr'./War-Thunder-Datamine-master/lang.vromfs.bin_u/lang/units.csv')

        # Список файлов есть, пошли по нему
        for file in res:
            try:
                plane_id = os.path.basename(file).replace('.blkx', '')
                if plane_id not in exclude:
                    plane_datamine = wt.WTPlaneFullInfo(plane_id=plane_id, plane_name = plane_names[plane_id])
                    result_json[plane_id]=plane_datamine.get_all()
            except Exception as e:
                print(e)

        with open('wtmfd_data.json', 'w', encoding="utf-8") as file:
            json.dump(result_json, file, ensure_ascii=False, indent=4)

        result_json = {"Version":f"{datamine_version}"}
        with open('wtmfd_data_version.json', 'w', encoding="utf-8") as file:
            json.dump(result_json, file, ensure_ascii=False, indent=4)
