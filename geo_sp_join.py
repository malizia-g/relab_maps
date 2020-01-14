
import geopandas as gpd
import pandas as pd



lombardia = gpd.read_file('istat/R03_11_WGS84.shp')
print(lombardia.head())

cened2 = pd.read_csv('results/res.csv')
print(cened2.head())

#Conversione del dataframe in geodataframe, aggiungendo la colonna geometry 
#che serve per memorizzare in un unico campo POINT la posizione geografica dell'indirizzo.
#Il tipo di riferimento cartografico (Coordinate Reference System, crs) 
#deve essere quello delle coordinate geografiche (latitudine e longitudine) 
#e cioè WGS84 (corrispondente all'EPSG 4326). Per ulteriori info sui codici https://epsg.io/

from shapely.geometry import Point 
geometry = [Point(xy) for xy in zip(cened2['lng'], cened2['lat'])]


Cened2crs = {'init': 'epsg:4326'}

cened2GDF = gpd.GeoDataFrame(cened2, crs=Cened2crs, geometry=geometry)
print(cened2GDF.head())

print(lombardia.crs)

lombardia.to_csv("results/lombardia.csv")

#Convertiamo ora le coordinate dei punti nello stesso sistema di riferimento del dataframe della lombardia. 
cened2GDF = cened2GDF.to_crs({'init': 'epsg:32632'}) 
cened2GDF.head()

#Convertiamo invece lombardia in epsg:4362, per usare i polygons?


#Per poter effettuare la sjoin (cioe' per associare ad un punto - cioe' ad un indirizzo
# - il poligono in cui si trova - cioe' la sezione del censimento in cui si trova) 
#dobbiamo assicurarci che il campo geometry del primo geodataframe sia di tipo POINT 
#mentre quello del secondo geodataframe sia di tipo POLYGON

print(type(cened2GDF.geometry[0])) #Verifico i dati del cened (Point)

print(type(lombardia.geometry[0])) #Verifico i dati istat (Polygon)

#Effettuiamo ora la sjoin
indirizzoSezione = gpd.sjoin(left_df=cened2GDF, right_df=lombardia, how="right", op="intersects")

#print(indirizzoSezione.head())


# Reproject the geometries by replacing the values with projected ones
indirizzoSezione['geometry'] = indirizzoSezione['geometry'].to_crs(epsg=4326)



print(indirizzoSezione.head())

#Salva risultato su file
#indirizzoSezione.to_csv("results/res_2_conv.csv")