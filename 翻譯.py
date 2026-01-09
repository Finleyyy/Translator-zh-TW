# pip install deep-translator
from deep_translator import GoogleTranslator

# 初始化翻譯器，設定來源為自動偵測 (auto)，目標為繁體中文 (zh-TW)
translator = GoogleTranslator(source='auto', target='zh-TW')

# 待翻譯的文字
text_to_translate = "Hello, world!"

# 進行翻譯
result = translator.translate(text_to_translate)

# 輸出結果
print(result)