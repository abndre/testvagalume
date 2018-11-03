# Desafio Foundation

Um dos maiores problemas foi conseguir usar o heroku corretamente, perdi demasiado
tempo nele.

O primeiro desafio foi entender como funciona o site do vagalume e posteriomente
obter os dados. Para tal utilizei o jupyter notebook para testar tal procedimento,
houve a necessidade de se usar o selenium em sua maioria.

Minha proposta de API é utilizar métodos GET com os parametros na URL para fazer as requisições.

### Exemplo de se utilização da API

```
get music artist

http://localhost:5000/vagalume/?artista=ramones&&limit=10

return

{
    "01.": "Pet Sematary",
    "02.": "Blitzkrieg Bop",
    "03.": "Poison Heart",
    "04.": "I Believe In Miracles",
    "05.": "Rock'n'Roll High School",
    "06.": "I Wanna Be Sedated",
    "07.": "I Don't Want To Grow Up",
    "08.": "Spiderman",
    "09.": "Surfin' Bird",
    "10.": "Beat On The Brat"
}


get all music artist

http://localhost:5000/vagalume/?artista=ramones&&limit=00

{
    "01.": "Pet Sematary",
    "02.": "Blitzkrieg Bop",
    "03.": "Poison Heart",
    "04.": "I Believe In Miracles",
    "05.": "Rock'n'Roll High School",
    "06.": "I Wanna Be Sedated",
    "07.": "I Don't Want To Grow Up",
    "08.": "Spiderman",
    "09.": "Surfin' Bird",
    "10.": "Beat On The Brat",
    "11.": "Let's Go",
    "12.": "Needles And Pins",
    "13.": "Sheena Is A Punk Rocker",
    "14.": "I Wanna Be Your Boyfriend",
    "15.": "Rockaway Beach",
    "16.": "I Love You",
    "17.": "Come Back, She Cried",
    "18.": "Psycho Therapy",
    "19.": "Now I Wanna Sniff Some Glue",
    "20.": "R.A.M.O.N.E.S",
    "21.": "I Wanna Live",
    "22.": "Teenage Lobotomy",
    "23.": "Animal Boy",
    "24.": "She Talks To Rainbows",
    "25.": "Out Of Time"
}


get top15 music artist

http://localhost:5000/vagalumetop/?artista=ramones

{
    "1": "Pet Sematary",
    "2": "Blitzkrieg Bop",
    "3": "Poison Heart",
    "4": "I Believe In Miracles",
    "5": "I Wanna Be Sedated",
    "6": "Rock'n'Roll High School",
    "7": "Spiderman",
    "8": "Surfin' Bird",
    "9": "Let's Go",
    "10": "I Don't Want To Grow Up",
    "11": "I Wanna Be Your Boyfriend",
    "12": "Sheena Is A Punk Rocker",
    "13": "Needles And Pins",
    "14": "Rockaway Beach",
    "15": "Beat On The Brat"
}

get music letra

http://localhost:5000/vagalumeletra/?artista='mamomas'&letra='Jumento Celestino'

{
    "letra": "Tava ruim lá na Bahia, profissão de bóia-fria\n\nTrabalhando noite e dia, num era isso que eu queria\nEu vim-me embora pra \"Sum Paulo\",\nEu vim no lombo dum jumento com pouco conhecimento\nEnfrentando chuva e vento e dando uns peido fedorento\nAté minha bunda fez um calo\n\nChegando na capital, uns puta predião legal\nAs mina pagando um pau, mas meu jumento tava mal\n\nPrecisando reformar\nFiz a pintura, importei quatro ferradura\nTroquei até dentadura e pra completar a belezura\nEu instalei um Road-Star!\n\nDescendo com o jumento na mó vula\nUltrapassei farol vermelho e dei de frente com uma mula\nSaí avuando, parecia um foguete\nSó não estourei meu côco pois tava de capacete\n\nMe alevantei, o dono da mula gritando\nO povo em volta tudo olhando e ninguém pra me socorrer\n\nFugi mancando e a multidão se amontoando\nEm coro tudo gritando: \"Baiano, cê vai morreêeê !\"\n\nDepois desse sofrimento, a maior desilusão\nPra aumentar o meu lamento, foi-se embora meu jumento\nE me deixou com as prestação\nE hoje eu tô arrependido de ter feito imigração\nVolto pra casa fudido, com um monte de apelido\nO mais bonito é cabeção!"
}
```
# Segunda etapa
## Aplicando e utilizando o heroku

utilizar o ChromeDriver foi um pouco complicado e ainda ocorrem alguns erros.
Em suma o heroku possui alguns buildpacks que sendo adicionados corretamente evitam
estes tipo de erros.

Alguns casos ocorre timeout ou o chromedriver trava e é necessário restartar a aplicação.
Mas em suma esta seria as urls de teste

```
# urls para teste usando heroku
https://andreteste1234.herokuapp.com/vagalume/?artista=ramones&&limit=10
https://andreteste1234.herokuapp.com/vagalumeletra/?artista='mamomas'&letra='Jumento Celestino
https://andreteste1234.herokuapp.com/vagalumetop/?artista=ramones
```
