import imdb
x=imdb.IMDb()
name=input("Please enter movie name")
movies=x.search_movie(str(name))
for m in range(0,len(movies)):
	print(m+1,movies[m])

print("\n")

#values lo
index=input("Please enter the index")
ind=movies[int(index)-1].getID()
movie = x.get_movie(ind)
title = movie['title']
year = movie['year']
genre = movie['genres']
director = movie['director']
cast = movie['cast']
listofcast = ','.join(map(str,cast))
plot = movie['plot']
#rating = movie['rating']
runtimes = movie['runtimes']
boxoffice = movie['box office']

#details

#print(movie.keys())
print("Title:",title)
print("\n")
print("Year: ",year)
print("\n")
print("Genre:")
for g in genre:
	print(g, end =" ")
print("\n")
print("Directors:")
for d in director:
 print(d,end= " ")
print("\n")

print("Plot:")
for p in plot:
 print(p)

#print("\nRating:",rating,"out of 5")

print("\nRuntimes:",runtimes[0], "minutes")


print("\nList Of Cast: ",listofcast)


print("\n BoxOffice: ")
for k,v in boxoffice.items():
    print(k,v)
#print("\nBox Office",boxoffice.keys(),boxoffice.values())
