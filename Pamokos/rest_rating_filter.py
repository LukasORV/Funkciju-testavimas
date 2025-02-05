rest_list = []
rest_count = int(input("Enter the number of restorants:" ))
for i in range(rest_count):
    rest_name = input("Restorant name: ")
    rest_rating = float(input("Restorant rating "))
    rest_list.append({"name": rest_name, "rating": rest_rating}) 
min_search_rating = float(input("Enter the minimum rating: "))
if min_search_rating < 4.0:
    min_search_rating = 4.0
def rest_filter(rest_list, min_search_rating):
    filtered_list = []
    for r in rest_list:
     if r["rating"] >= min_search_rating:
        filtered_list.append(r["name"])
    return  filtered_list
result = rest_filter(rest_list, min_search_rating)
print(f"Minimun rating is {min_search_rating} , restorants with rating higher than {min_search_rating} are: {result} , ")
