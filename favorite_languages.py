favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

#访问字典键值对
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#访问字典的键
for name in favorite_languages.keys():
    print(name.title())

#访问字典的值
for language in favorite_languages.values():
    print(language.title())

#访问字典的值并去重
for language in set(favorite_languages.values()):
    print(language.title())