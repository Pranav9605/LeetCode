import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # dup=pd.DataFrame()
    # dup['Email'] = person['email'].duplicated()
    # print(dup)
    # return dup.drop_duplicates()



    results = pd.DataFrame()
    results = person.loc[person.duplicated(subset=['email']), ['email']]
    return results.drop_duplicates()
    
