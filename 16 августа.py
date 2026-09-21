import requests

url = "https://api.opendota.com/api/heroStats"
response = requests.get(url)

if response.status_code == 200:
    heroes = response.json()

    # Фильтруем героев с минимум 100 играми (суммарно pro + public)
    valid_heroes = [
        h for h in heroes
        if (h.get('pro_pick', 0) + h.get('pick', 0)) >= 100
    ]

    if not valid_heroes:
        print("❌ Нет героев с 100+ играми")
    else:
        # Сортируем по общему винрейту
        sorted_heroes = sorted(
            valid_heroes,
            key=lambda h: (h.get('pro_win', 0) + h.get('win', 0)) / (h.get('pro_pick', 0) + h.get('pick', 0)),
            reverse=True
        )

        best = sorted_heroes[0]
        total_wins = best.get('pro_win', 0) + best.get('win', 0)
        total_picks = best.get('pro_pick', 0) + best.get('pick', 0)
        winrate = (total_wins / total_picks) * 100

        print("🏆 Герой с самым высоким винрейтом (100+ игр):")
        print(f"   {best['localized_name']}")
        print(f"   Побед: {total_wins} из {total_picks} игр")
        print(f"   Винрейт: {winrate:.1f}%")
else:
    print("Ошибка загрузки данных")