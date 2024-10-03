marks = {"ram": 33,
           "rahul": 45,
            "devesh": 30,
            "jayul": 34,
            "anjali": 42,
            "vivek": 29,
            "neha": 48,
            "simran": 31,
            "rohit": 40,
            "sakshi": 36,
            "amit": 37,
            "kavya": 41,
            "manish": 32,
            "sneha": 44 }

key=input("Enter key for search :>")

if key in marks.keys():
    print("key is exists")
else:
    print("doesn't exsist key")