"""
This module contains neccessary data and structure information for 
schiffsregister app
"""
import streamlit as st

nations_order_dict = {
    "JAPAN": 1,
    "USA": 2,
    "UDSSR": 3,
    "DEUTSCHLAND": 4,
    "GB": 5,
    "FRANKREICH": 6,
    "ITALIEN": 7,
    "PANASIEN": 8,
    "EUROPA": 9,
    "DIE NIEDERLANDE": 10,
    "COMMONWEALTH": 11,
    "PANAMERIKA": 12,
    "SPANIEN": 13,
}

type_option_list = ["standard", "elite", "premium", "spezial"]

class_order_dict = {
    "U-Boot": 1,
    "Zerstörer": 2,
    "Kreuzer": 3,
    "Schlachtschiff": 4,
    "Flugzeugträger": 5,
}

tier_order_dict = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XI": 11,
}

# Hauptfelder des Schiffsregisters
main_columns = ["Nation", "Typ", "Klasse", "Stufe", "Name"]

# Felder zur Sortierung
order_value_columns = [
    "Ordnungswert_Nation",
    "Ordnungswert_Klasse",
    "Ordnungswert_Stufe",
]

# Alle Spalten
all_columns = main_columns + order_value_columns

# Sortierreihenfolge
sort_field_order = [
    "Ordnungswert_Nation",
    "Ordnungswert_Stufe",
    "Ordnungswert_Klasse",
    "Name",
]
