import os, datetime
from exif import Image

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

while True:
    try:
        offset = datetime.timedelta(seconds=int(input('輸入時間偏移秒數: ')))
    except:
        print('輸入有誤，請重新輸入。')
    else:
        break

index = 1
total = len(os.listdir(folder_path))

for img in os.listdir(folder_path):
    print(f'({index} / {total}) ', end='')
    try:
        img_path = os.path.join(folder_path, img)

        with open(img_path, 'rb') as img_file:
            img = Image(img_file)

        new_time = (datetime.datetime.strptime(img.datetime, '%Y:%m:%d %H:%M:%S')+offset).strftime('%Y:%m:%d %H:%M:%S')

        if img.datetime is not None: img.set('datetime', new_time)
        if img.datetime_original is not None: img.set('datetime_original', new_time)
        if img.datetime_digitized is not None: img.set('datetime_digitized', new_time)

        with open(img_path, 'wb') as new_image_file:
            new_image_file.write(img.get_file())

        print(f'成功更改 {img_path} 的 EXIF 時間戳。')
    except:
        print(f'失敗，跳過 {img_path}。')
    index += 1