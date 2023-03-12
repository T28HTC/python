import json
# f = open("data.json", 'w', encoding="utf-8")
# text = [False, None, 3.14, (1,2,3), 1]
# json.dump(text, f, ensure_ascii=False) # записывает файлы
# print(json.dumps(text))
# f.close()

# import json
# f = open("data.json", 'w', encoding="utf-8")
# salad = {
#     "Tomato": [5, "Cut"],
#     "Cucumber": [3, "Check cucumbers for bitterness", "Cut"],
#     "Salt": "add to taste",
#     "Sugar": False
# }
# json.dump(salad, f) # записывает файлы
# print(json.dumps(salad))
# f.close()

# f = open("data.json", 'r', encoding="unf-8")
# content = json.loads(f)
# f.close()
# print(content)


# 1
# f = open('file.txt', "r", encoding="utf-8")
# content = f.readlines()
# f.close()
#
# print(content)
#
# dame = {}
# for i in content:
#     k = i.split(': ')
#    dame[k[0]] = k[1].rstrip()
# print(k)
#
# f = open('data.json', 'w', encoding='utf-8')
# json.dump(dame, f,ensure_ascii=False)
# f.close()


# 2
# f = open('data.json', "r", encoding="utf-8")
# content = json.load(f)
# f.close()
#
#
# for i, elem in enumerate(content):
#     a = type(elem)
#     if a == str():
#         content[i]+="!"
#     elif a in (int, float):
#         content[i]+=1
#     elif a == bool:
#         content[i] = not content[i]
#     # elif elem == None:
#     #     content.pop(4)
#     elif a == list:
#         content[i] = content[i] + content[i]
#     elif a == dict:
#         content[i]["newkey"] = None
# print(content)


# import requests
# resp = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = resp.json()['iss_position']
# print(data)
# print(f"Широта: {data['latitude']}, Долгота: {data['longitude']}")


