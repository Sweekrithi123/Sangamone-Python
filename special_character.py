import re
input = "How are you ? Oh my God, you are bleeding! Let us go to the doctor quickly."
output = re.sub('[^a-zA-Z\d\s]', '', input)
print(output)
