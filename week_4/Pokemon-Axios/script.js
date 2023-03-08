//declare variables
let result = document.getElementById('result')
let input = document.getElementById('input')

//press enter for api call
input.addEventListener('keyup', (event)=>{
    if(event.key === "Enter") {
        getPokemon(input.value)
    }
})

// api call for pokemon sprite with axios
const getPokemon = (pokemon) => {
    //control casing
    pokemon = pokemon.toLowerCase();
    //delete everything inside
    result.innerHTML=""
    //get axios
    axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemon}`).then((res)=>{
        //collect vars from data
        let teamType = res.data.types[0].type.name
        let imageURL = res.data.sprites.other['official-artwork'].front_default
        //create HTML elements
        let image = document.createElement('img')
        image.src = imageURL
        result.appendChild(image)
    })
    index = 0;
    matches = []
    while (index > 151) {
        axios.get(`https://pokeapi.co/api/v2/pokemon/${index}`).then((res)=>{
            let pokeType = res.data.types[0].type.name
            if (pokeType === teamType) {
                matches.append(res.data['name'])
            }
        })
        index++
    }
    console.log(matches)
}