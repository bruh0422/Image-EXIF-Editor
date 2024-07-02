# 圖片 EXIF 編輯器
給予時間偏移秒數，批量更改資料夾內的圖片 EXIF 時間戳。

## 運作原理
使用 `exif` 變更圖片的 `datetime` `datetime_original` `datetime_digitized` 資料。

## 前置作業
### 複製儲存庫
```bash
git clone https://github.com/bruh0422/Image-EXIF-Editor.git
cd Image-EXIF-Editor
```

### 安裝必要檔案
```bash
pip install -r requirements.txt
```

## 開始使用
```bash
python run.py
```
接下來按照程式指定的步驟操作即可。\
程式會自動跳過非圖片或變更失敗的檔案。
