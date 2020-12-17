try:
    print(float('abc'))
except Exception as e:
    print("type error: " + str(e))