import pandas as pd
import uuid
import datetime

class CuboReport:

    def __init__(self):
        self.pd = pd
    
    def create_df_startup(self):
        data = {
            'id': [],
            'Link cubo':  [],
            'Nome': [],
            'Core business': [],
            'Area': [],
            'Vertical': [],
            'What problem do we solve': [],
            'Pitch': [],
            'Link': [],
            'Market Differentials': [],
            'Bussiness Model': [],
            'Founders': [],
            'Clients': [],
            'Instagram': [],
            'Facebook': [],
            'Twitter': [],
            'Linkedin': [],
            'Website': [],
            'Address': [],
            'Time':[]
        }
        self.df_startup = self.pd.DataFrame(data)

    def insert_startup(self, link_cubo, name, core, area, vertical,
                       problem, link_pitch, pitch, diff,
                       business, founders, clients, 
                       instagram, facebook, twitter, linkedin,
                       website, address):

        self.df_startup = self.df_startup.append({
            'id': str(uuid.uuid4()),
            'Link cubo': str(link_cubo),
            'Nome': str(name),
            'Core business': str(core),
            'Area': str(area),
            'Vertical': str(vertical),
            'What problem do we solve': str(problem),
            'Pitch': str(pitch),
            'Link': str(link_pitch),
            'Market Differentials': str(diff),
            'Bussiness Model': str(business),
            'Founders': str(founders),
            'Clients': str(founders),
            'Facebook': str(facebook),
            'Instagram': str(instagram),
            'Facebook': str(facebook),
            'Twitter': str(twitter),
            'Linkedin': str(linkedin),
            'Website': str(website),
            'Address': str(address),
            'Time': str(datetime.datetime.utcnow())
        }, ignore_index=True)