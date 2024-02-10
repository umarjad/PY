sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Accessing the value of the key 'history'
history_mark = sampleDict['class']['student']['marks']['history']
print("Value of 'history':", history_mark)
