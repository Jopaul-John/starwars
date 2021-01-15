### Assumptions

- All the starships in the movies are given in [wiki](https://en.wikipedia.org/wiki/List_of_Star_Wars_spacecraft "wiki") and [CNet](https://www.cnet.com/pictures/star-wars-spaceships-ranked-by-power-speed/ "CNet")
- All the starship information is given in the [starwar fandom](https://starwars.fandom.com/wiki/Main_Page "starwar fandom") page
- Ships that has no info in [starwar fandom](https://starwars.fandom.com/wiki/Main_Page "starwar fandom") page is assumed to have rating 100.

### Tech Used
##### Project developed in Django and Angular for better User Experience
- **Django** - Acts as a python backend framework
- **Angular** - Frontend Framework
- **Docker** - Builds the Django and Angular frameworks
- **Websockets** - For better user experience. User does not have to wait until entire ship rating are fetched. Instead the scrapped data is displayed ASAP.

### How to Use
- Pull the repository [starwars](https://github.com/Jopaul-John/starwars "starwars")
- install [Docker](https://docs.docker.com/engine/install/ "Docker") and [Docker - Compose](https://docs.docker.com/compose/install/ "compose") 
- Run Commands
`$ docker-compose build`
`$ docker-compose up`
- This will setup both the front and backend frameworks
- After server has started go to [localhost:1337](http://localhost:1337/ "localhost:1337") to view the table.
- Click on **Get Data** to load the data and once entire data is loaded, it is sorted according to the hyperdrive rating.
### Results
- 77 Ship Names and their hyperdrive rating was found
- Screen shots are included in the repo
[Screen Shot 1](starwars1.png)
[Screen Shot 2](starwars 2.png)