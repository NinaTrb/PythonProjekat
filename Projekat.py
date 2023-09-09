from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import pandas as pd

ukBrStanovnika = 11760

#Ucitavanje granice naselja na karti

shapefile_path = r'C:\Users\Nina\Desktop\GIS Programiranje\Batocina Naselja.shp'
naselja= gpd.read_file(shapefile_path)

#provera koordinatnog sistema
naselja.crs = 'epsg:6316'

naselja.crs
print(naselja.crs)
naselja.crs = from_epsg(6316)
naselja.crs
print(naselja.crs)

#prikaz granice naselja na karti

naselja.plot(color='lightgray', edgecolor='black')
plt.title("Batocina Naselja")
plt.show()

#ucitavanje excel tabele sa brojem umrlih i rodjenih za svako naselje

df = pd.read_excel('C:\\Users\\Nina\\Desktop\\GIS Programiranje\\Book1.xlsx')

#racunanje prirodnog prirastaja, stope nataliteta i stope mortaliteta

prirodniPrirastaj = []
df['PRIRODNI PRIRASTAJ'] = df['RODJENI'] - df['UMRLI']
df['STOPA NATALITETA'] = (df['RODJENI'] / ukBrStanovnika) * 1000
df['STOPA MORTALITETA'] = (df['UMRLI'] / ukBrStanovnika) * 1000

print(df)

#ucitavanje excel tabele sa kooridnatama

sf = pd.read_excel('C:\\Users\\Nina\\Desktop\\GIS Programiranje\\Koordinate.xlsx')
print(sf)

# Kreiranje GeoDataFrame za tačke
gdf_tacke = gpd.GeoDataFrame(sf, geometry=gpd.points_from_xy(sf['x (lat)'], sf['y (lon)']), crs='epsg:6316')

# Kreiranje mape
fig, ax = plt.subplots(figsize=(10, 8))

# Prikaz granica naselja na karti
naselja.plot(ax=ax, color='lightgray', edgecolor='black')

# Prikaz tačaka na mapi
gdf_tacke.plot(ax=ax, marker='o', color='red', markersize=5, label='Tacke')

# Postavljanje titule
ax.set_title("Batocina Naselja i Tacke")

# Prikaz legende
ax.legend()

# Prikaz mape
plt.show()

