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

for image in os.listdir(folder_path):
    print(f'({index} / {total}) ', end='')
    try:
        image_path = os.path.join(folder_path, image)
        if not os.path.isfile(image_path): raise TypeError

        with open(image_path, 'rb') as image_file:
            image = Image(image_file)

        new_time = (datetime.datetime.strptime(image.datetime, '%Y:%m:%d %H:%M:%S')+offset).strftime('%Y:%m:%d %H:%M:%S')

        if image.datetime is not None: image.set('datetime', new_time)
        if image.datetime_original is not None: image.set('datetime_original', new_time)
        if image.datetime_digitized is not None: image.set('datetime_digitized', new_time)

        with open(image_path, 'wb') as new_image_file:
            new_image_file.write(image.get_file())

        print(f'成功更改 {image_path} 的 EXIF 時間戳。')
    except TypeError:
        print(f'{image_path} 並非一個檔案。')
    except Exception as e:
        print(f'錯誤，跳過 {image_path} - {e}')
    index += 1