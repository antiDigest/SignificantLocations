# SignificantLocations

## User Specific Patterns

### Give Locations Ranks :

1. Get all locations for a user in series. Find all jump points with Dt = 10 minutes. <strong>#1 feature</strong>

2. Store duration of stay <strong>#2 feature</strong>

3. Store the time of day (Morning, Afternoon, Evening or Night, maybe) <strong>#3 feature</strong> (Even though we are not yet classifying, based on the time users visit a particular kind of location, which could actually have been good)

4. We need two graphs : Location-Location graph (adjacency matrix) - Use PageRank approach here; User-Location Graph (I haven't thought about it yet)

5. Location-Location Graph: One LL graph for one user

	* Uses GPS data as well as checkin-data ! (Not using checkin data for the moment)

	* In a way, we make a graph of location to location traversal. From where did the person start and where did he end.

	* Find names of each locations using geopy, if the latitude and longitudes are given for it. Actually, I still have to test what output geopy is giving, we might be able to make it more extensive if we get more data. (Use geopy with a bit more care)

	* So, graph C = [a(i,j)] where a = number of times user has travelled from i to j.

6. User-Location vector: one UL vector

	* So, vector M = [v(i)] where v = number of stops user has made at i. (Might even have to take a graph of all users).

7. Rank-By-Visits: The rank of a place increases by the number of visits to that place. Directly proportional. <strong>#4 feature</strong>

8. Rank-By-Distance: tiered wedding-cake approach. Inversely proportional to distance. <strong>#5 feature</strong>

9. Rank-By-Durations: I think the rank of a place is going to be proportional to the duration of stay at a particular place. <strong>#2 feature</strong>

10. Rank-By-Users: If a place has more number of users visiting it, it is more significant. <strong>#6 feature -- probably best to leave it in class patterns</strong>

### SAMASYA with the approach:

1. We are only using the locations which we have in the location-location graph. Can we find a way to use all the locations, and in some way find the rank of a location that has not been cited in the LL graph ?<strong> -- solved, new paper solves this</strong>

2. We have to find a list of locations, which are nearby a particular area (the search term specifies the area, and the locations inside and near it are those we are going to visit). BUT HOW DO WE RANK THESE ? because these need to be already ranked for the re-ranking algo to work, and for that we have to have a graph connecting these locations, in order to make the modified PageRank on these work -- big problem, this. Find some other way for this./ Consult sir <strong>-- solved, new paper solves this</strong>

## Class Patterns:

1. This is the part, that we'll have to think about ourselves. <strong>HOW DO WE CLASSIFY USERS INTO A CLASS ????</strong>

2. Classify Users:

	1. Users are classified on the basis of their authority. Authority and Hub scores for users. <strong>#1 feature</strong>

	2. Assumption : More the authority of a user, more is his tendency to visit a hot location and vica-versa

	3. So, we use HITS algorithms in the UL graph to find out which user was most authoritative. The hub scores give us the travel experience and authority scores give us the significance of the locations the user is visiting.

	4. In a way, HITS is also useful in finding the significance of a location with respect to a user. Authority and hub score for each location. <strong>#2 feature ( why ? )</strong>.

	5. For users in the same class, it is important that the number of locations here are much more than the number of locations for any particular user.

## SAMASYA with Classify Users:

1. Why are we even finding locations for a particular user <strong>-- for user specific recommendations </strong>, if we have to recommend the locations from a group (since that is what has more locations). <strong>For each class, the same strategy as mentioned for each user.</strong>

2. How do we extract taste from a set of locations, which have been ranked on the basis of a modified PageRank algorithm ? And how do we use those places in a set of similar users ?

We want this and for <strong>each class of users</strong>:

Score|Specification
---|---|
2|Very interesting to Class/User and recommended
1|An OK location to Class/User
0|Neutral to Class/User
-1|Not interesting to Class/User and not recommended
-2|I have no idea of what it is


# TODO :

S.No|Task|Done ?|
:---:|:---:|:---:|
1.|Create LL graph using location-location travels|done
2.|Create UL graph, using user location relationships|done
3.|Apply modified PageRank on LL graph and rank the locations|-
4.|Apply randomised HITS on UL and LL graph--classify users|-
5.|Develop a re-ranking algorithm|-
6.|Pass the list of ranks on the new search area, through the re-ranking algorithm|-

