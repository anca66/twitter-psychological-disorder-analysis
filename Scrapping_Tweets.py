import twint
twitter = twint.Config()
twitter.Limit = 5000

# Crearea csv-ului pentru tweet-urile neutre
twitter.Search ="sun OR actor OR horoscope OR music OR rainbow "
twitter.Store_csv = True
twitter.Lang = "en"
twitter.Output = 'Dataset/Neutral.csv'

twint.run.Search(twitter)
