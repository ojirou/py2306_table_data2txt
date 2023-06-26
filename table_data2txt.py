import csv
csv_list_file = ".\\files_list_日記csv.txt"
# CSVファイルのリストを読み込む
with open(csv_list_file, 'r') as list_file:
    csv_files = list_file.read().splitlines()
# 各CSVファイルに対して処理を実行
for csv_file_path in csv_files:
    # CSVファイルを読み込み、日付ごとにテキストファイルを作成
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            date_str = row[0].replace('日', '').replace('月', '').replace('火', '').replace('水', '').replace('木', '').replace('金', '').replace('土', '')
            date = ''.join(filter(str.isdigit, date_str))  # 数字のみを抽出して日付形式に変換
            diary = row[1]
            # テキストファイルを作成してテキストを書き込む
            file_name = f'【Daily】{date[:4]}年{date[4:6]}月{date[6:]}日Jogno日記.txt'
            with open(file_name, 'w', encoding='utf-8') as output_file:
                output_file.write(f'【Daily】{date[:4]}年{date[4:6]}月{date[6:]}日\n')
                output_file.write(diary)