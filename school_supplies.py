packet_of_pens = 5.80
packet_of_markers = 7.20
cleaning_detergent_per_litre = 1.20

number_of_packet_of_pens = int(input())
number_of_packet_of_markers = int(input())
litre_cleaning_detergent = int(input())
discount = int(input()) / 100

price_for_the_materials = (number_of_packet_of_pens * packet_of_pens + number_of_packet_of_markers * packet_of_markers
         + litre_cleaning_detergent * cleaning_detergent_per_litre)
final_price_with_dicount = (price_for_the_materials * (1 - discount))

print(final_price_with_dicount)