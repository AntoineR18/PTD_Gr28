import pandas as pd

df_nocs = pd.read_csv("donnees_jeux_olympiques/noc_regions.csv")


def noc_to_country(noc_code):
    """Convertit un code NOC en nom de pays."""
    result = df_nocs[df_nocs['NOC'] == noc_code]['region']
    return result.values[0] if not result.empty else None


def country_to_noc(country_name):
    """Convertit un nom de pays en code NOC."""
    result = df_nocs[df_nocs['region'] == country_name]['NOC']
    return result.values[0] if not result.empty else None
