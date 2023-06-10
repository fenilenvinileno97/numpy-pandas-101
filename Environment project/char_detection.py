#!usr/bin/env python3
from chardet import detect

def char_type(filepath):
    with open(filepath, 'rb') as f:
        result = detect(f.read())
    return result['encoding']

def run():
    co2_dataset = char_type('../../Datasets/CO2_emission_by_countries.csv')
    threatened_species = char_type('../../Datasets/Threatened_species.csv')
    carbon_dioxide = char_type('../../Datasets/Carbon_dioxide_emission_estimates.csv')
    food_production = char_type('../../Datasets/Food_Production.csv')
    land_usage = char_type('../../Datasets/Land.csv')
    water_sanitation = char_type('../../Datasets/Water_and_sanitation_services.csv')
    
    print(f'CO2 dataset encoding is {co2_dataset}')
    print(f'Threatened species database encoding is {threatened_species}')
    print(f'Carbon dioxide dataset encoding is {carbon_dioxide}')
    print(f'Food production dataset encoding is {food_production}')
    print(f'Land usage dataset dataset encoding is {land_usage}')
    print(f'Water sanitation usage encoding {water_sanitation}')
    
if __name__ == '__main__':
    run()