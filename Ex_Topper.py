#set of students with name and score
students = [
    {
        "name": "ram",
        "score": 95
    },
    {
        "name": "shyam",
        "score": 85
    }
]
#add student
students.append({
    "name": "akshay",
    "score": 90
})
#print(students)
for s in students:
    print(s["name"], s["score"])
#find topper
topper = max(students, key = lambda s: s["score"])
print("topper :", topper["name"], topper["score"])