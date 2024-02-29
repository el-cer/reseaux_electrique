import pandas as pd
class Infra:
    def __init__(self,df):
        self.df = df
        self.data_clean()
    def data_clean(self):
        '''This function clean the dataset'''
        

        self.new_df =  self.df.copy()
        self.new_df.drop_duplicates(inplace=True) 
        
        self.preparation()
    def preparation(self):   
        # print(self.new_df.groupby('infra_type').count()/len(self.new_df)*100) 
        #see % of 2 types of infra

        self.new_df_copy = self.new_df.copy()
        self.all_infra_id = self.new_df_copy[['infra_id','infra_type']]
        self.all_infra_id = self.all_infra_id.drop_duplicates() #keep_unique infra id

        self.new_df_copy.drop(columns=['id_batiment','infra_type'],inplace=True)
        self.groupby_infra_id = self.new_df_copy.groupby('infra_id').sum().reset_index()
        self.get_dificulty_level()
    def get_dificulty_level(self):
        self.main = pd.merge(self.groupby_infra_id,self.all_infra_id,on='infra_id',how='left')  #to have infra type with unique infra
        self.main = self.main.loc[self.main['infra_type']=='a_remplacer',:]     
     #if a remplacer wee calcule the division
        #if intacte wee dont do division

        self.main.loc[:,'difficulty_infra'] = self.main.loc[:,'longueur'] / self.main.loc[:,'nb_maisons']
         #remplcar NaN to 0
        