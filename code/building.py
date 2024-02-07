import pandas as pd
class Batiment:
    def __init__(self,infra):
        self.main = infra.main
        self.new_df = infra.new_df
        self.df = None
        self.merging_data()
    def merging_data(self):
        """this function merge the datasets and add difficulty infra to the main df , to after calcule the sum """

        self.list_e = []
        
        self.dataset_with_difficulty = self.new_df.merge(self.main[['infra_id','difficulty_infra']],on='infra_id',how='left')
        
        self.get_bulding_difficulty()
    def get_bulding_difficulty(self):  
        
        self.df_building_dificulty = self.dataset_with_difficulty[['id_batiment','nb_maisons','difficulty_infra']].groupby('id_batiment').sum().reset_index()
        print(self.df_building_dificulty)
        self.df_building_dificulty = self.df_building_dificulty.rename(columns={'difficulty_infra': 'difficulty_batiment'})
        self.agolrithm()
    def agolrithm(self):
        """this function contain the main algorithm, 
        with a iterative processus :
        At the beginning filter with values who the difficulty buildings is >0 so all the 'a_remplacer'
        put on a list all the buildings who contains infra 'a_remplacer'
        Same for the values.
        for loop with range of the len of building dificulty (85)
        
        minimum value with min() function 
        take the index of the minimum value
        example:
        min(i) = 10 and index 3
        index_min_value = self.building_dificulty.index(10) 
        index_min_value = 3

        self.list_e.append(self.id_batiment_list[3])
        it will append a value like 'E000381'
        --------------------
        self.id_batiment_list.remove(self.id_batiment_list[index_min_value])
        self.df_building_dificulty.remove(minimum_value)

        Remove is very important because if you not remove the minimum value will be the same
        Same for the id_batiment

        Once the infra of the building is repared we delete of this list
        --------------------
        """
        cleaned = self.df_building_dificulty.loc[self.df_building_dificulty['difficulty_batiment']>0,:]
        self.id_batiment_to_fix_list = cleaned['id_batiment'].to_list()
        
        self.building_dificulty = cleaned['difficulty_batiment'].to_list()
        
        for _ in range(0,len(self.building_dificulty)):            
            minimum_value = min(self.building_dificulty)
            index_min_value = self.building_dificulty.index(minimum_value)

            self.list_e.append(self.id_batiment_to_fix_list[index_min_value])
            self.id_batiment_to_fix_list.remove(self.id_batiment_to_fix_list[index_min_value])
            self.building_dificulty.remove(minimum_value)
            minimum_value = None
            self.see_index()

    def see_index(self):
        for i in range(0,len(self.list_e)):
            self.df = self.dataset_with_difficulty.loc[(self.dataset_with_difficulty['id_batiment'] == self.list_e[i])]
            if len(self.df)>0:
                self.list_eliot = self.df['infra_id'].to_list()
        
        self.change_state_infra()
        self.list_eliot = []
        
    def change_state_infra(self):
        for i in self.list_eliot:
            self.dataset_with_difficulty.loc[self.dataset_with_difficulty['infra_id'] == i, 'infra_type'] = 'infra_intacte'
        #print(self.dataset_with_difficulty.loc[self.dataset_with_difficulty['infra_type']=='a_remplacer',:])
        self.dataset_with_difficulty.to_csv('dataset.csv')
        



        
            