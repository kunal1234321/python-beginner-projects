text = input("Enter some text: ")

words = text.lower().split()

positive_words = ["good", "great", "amazing", "happy", "excellent", "love"]
negative_words = ["bad", "sad", "terrible", "hate", "awful", "angry"]

positive = 0
negative = 0

for word in words:
    if word in positive_words:
        positive += 1
    elif word in negative_words:
        negative += 1

print("\nText Analysis")
print("------------")
print("Words:", len(words))
print("Positive words:", positive)
print("Negative words:", negative)

if positive > negative:
    print("Sentiment: Positive")
elif negative > positive:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")