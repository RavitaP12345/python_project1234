from textblob import TextBlob
y=input("Type your sentences:")
edu=TextBlob(y)
x=edu.sentiment.polarity
if x<0:
    print("Negative")
elif x==0:
    print("Netural")
elif x>0 and x<=1:
    print("positive")       