dict1 = {
    "city": "Москва",
    "temperature": "20",
}
dict1["temperature"] = 15
print(dict1.get("country", "Россия"))
dict1["date"] = "27.05.2019"
print(dict1)
print(len(dict1))