from billboard_charts import fetch_chart
import csv
categories=['hot-100', 'pop-songs', 'r-b-hip-hop-songs', 'country-songs', 'latin-songs', 'rock-songs', 'dance-electronic-songs']
dates=['2026-01-03', '2026-02-07', '2026-03-07', '2026-04-04', '2026-05-02', '2026-06-06', '2026-07-04', '2026-08-01', '2026-09-05', '2026-10-03', '2026-11-21']
all_artists=set()
for i in dates:
    for category in categories:
        try:
            rows = fetch_chart(category, date=i)
            for row in rows:
                all_artists.add(row['Artist'])
        except Exception as e:
            print(f"{category}: {e}")
    print(len(all_artists))
with open('artists.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in all_artists:
        writer.writerow([item])
