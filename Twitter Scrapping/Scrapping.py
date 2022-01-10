import twint

c = twint.Config()
c.Limit = 5000

# Crearea csv-ului pentru tweet-urile neutre
c.Search ="sun OR actor OR horoscope OR music OR rainbow "
c.Store_csv = True
c.Lang = "en"
c.Output = "Neutre.csv"

twint.run.Search(c)

# Crearea csv-ului pentru tweet-urile depresive
c.Search ="depression OR depressed OR sadness OR dead OR suicide OR suicidal OR misery"
c.Store_csv = True
c.Lang = "en"
c.Output = "depression.csv"

twint.run.Search(c)


# Crearea csv-ului pentru tweet-urile anxioase
c.Search ="anxiety OR stress OR struggle"
c.Store_csv = True
c.Lang = "en"
c.Output = "anxiety.csv"

twint.run.Search(c)


# Crearea csv-ului pentru tweet-urile bipolare
c.Search ="bipolar OR bi-polar OR crazy OR irritable"
c.Store_csv = True
c.Lang = "en"
c.Output = "bipolar.csv"

twint.run.Search(c)


# Crearea csv-ului pentru tweet-urile PTSD
c.Search ="ptsd OR traumatic OR post traumatic stress disorder"
c.Store_csv = True
c.Lang = "en"
c.Output = "PTSD.csv"

twint.run.Search(c)


