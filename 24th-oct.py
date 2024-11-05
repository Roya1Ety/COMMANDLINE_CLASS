import requests
import numpy as np
import pandas as pd

# data = {
#     "name": ["Alice", "Jerry", "Bola", "victor", "John", "Grace"],
#     "age": [15, 18, 16, 20, 12, 13]
# }

# data_frame = pd.DataFrame(data)
# print(data_frame)

import pandas as pd

data = {
    "name": ["Alice", "Jerry", "Bola", "Victor", "John", "Grace"],
    "age": [15, 18, 16, 20, 12, 13]
}

data_frame = pd.DataFrame(data)

# Modify the index to start from 1
data_frame.index = data_frame.index + 1

print(data_frame)


# arr = np.array([1, 2, 3, 4, 5])
# print(arr ** 2)

# url = "https://api.github.com"

# res = requests.get(url)
# if res.status_code !="200":
#     print ("Bad request")
# else:
#     status = requests.status_codes()
#     json_response = res.json()

# print("status code, status")
# print("json_response", json_response)