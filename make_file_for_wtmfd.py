import war_thunder_plane_info.main as wt

# Список самолетов который нам интересен, если пусто, то обработаем все
list_plane = [
    'a-20g'
    ]

if __name__ == "__main__":
    print('1')
    for plane_id in list_plane:
        plane_datamine = wt.WTPlaneFullInfo(plane_id)
        print(plane_datamine.get_all())
