from deep_translator import GoogleTranslator
language_list = GoogleTranslator().get_supported_languages()
translator = GoogleTranslator(source='en', target='persian')
translation = translator.translate("Good Morning")
print(translation)