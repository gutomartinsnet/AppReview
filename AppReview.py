#REVIEWS APPLE STORE SEM A VERSÃO DO APP
import pandas as pd
import numpy as np
import json
#import unicodecsv as csv

from app_store_scraper import AppStore
pptdigital = AppStore(country='br', app_name='pptdigital', app_id = '1480051058')

pptdigital.review(how_many=2000)
pptdigital.reviews


pptdigitaldf = pd.DataFrame(np.array(pptdigital.reviews),columns=['review'])
pptdigitaldf2 = pptdigitaldf.join(pd.DataFrame(pptdigitaldf.pop('review').tolist()))
pptdigitaldf2.head()

pptdigitaldf2.to_csv('pptdigital-apple-reviews.csv',encoding='utf-8-sig')
#pptdigitaldf2.to_excel('pptdigital-apple-reviews.xlsx', sheet_name='apple store',encoding='utf-8-sig')

#REVIEWS APPLE STORE COM A VERSÃO DO APP
import pprint
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import pytz as pytz

from app_store.app_store_reviews_reader import AppStoreReviewsReader

# app_id, and country of xcode
reader = AppStoreReviewsReader(
    app_id="1480051058",
    country="br"
)

# To fetch reviews entered in past 5 days
since_time = datetime.utcnow().astimezone(pytz.utc) + timedelta(days=-660)

# fetch_reviews will fetch all reviews if not parameters are passed.
# If `after` is passed then it will fetch all reviews after this date
# If `since_id` is passed then it will fetch all reviews after this review_id
reviews = reader.fetch_reviews(
    #after=since_time
)



pp = pprint.PrettyPrinter(indent=4)
#for review in reviews:
#    pp.pprint(review.__dict__)
g_df = pd.DataFrame(np.array(reviews),columns=['review'])
print("Created dataframe: \n{}".format(g_df))
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))
g_df2.head()

g_df2.to_csv('pptdigital-apple-reviewsv2.csv',encoding='utf-8-sig')
#g_df.to_excel('pptdigital-appgoogle-reviews_teste.xlsx', sheet_name='apple store',encoding='utf-8-sig')
