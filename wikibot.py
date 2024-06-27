import wikipedia

def scrape(name= "Microsoft", length = 2):
    result = wikipedia.summary(name,length)
    return result

print(scrape("Wikipedia"))