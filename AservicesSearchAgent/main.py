from servicesSearchAgent import search_microservices

query_dict = {
    "name": "课题一",
    "description": "",
    "role": "",
    "function": "",
    "requirement": ""
}

result = search_microservices(query_dict)
print(result)

