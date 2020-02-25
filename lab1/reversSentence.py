sen=input('typt keer een zinneke:')
# spit da zinneke
split=sen.split()
# draai al de woorden om
split.reverse()
# zet ze terug samen 
rs = " ".join(split)
# TADA
print(rs)