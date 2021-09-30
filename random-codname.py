import random
from flask import Flask

app = Flask(__name__)

wordlist = ["Fairweather","Waddington","Monarch","Robson","Sir-Wilfrid-Laurier","Sir-Sandford","Skihist","Ratz","Odin","Monashee","Columbia","Queen-Bess","Cooper","Ulysses","Wedge","Otter","Kwatna","Golden-Hinde","Scud","Farnham","Razorback","Oscar","Assiniboine","Jancowski","Gladsheim","Valpy","Dawson","Chatsquot","Buckwell","Priestley","Sharks-Teeth","Goodsir","Detour","Seven-Sisters","Howson","Silvertip","Saugstad","Brian-Boru","Victoria","Tsaydaychuz","Kootenay","Shedin","Atna","Birkenhead","Edziza","Sir-Alexander","Harrison","Chutine","Whitehorn","Thudaka","Unuk","Cond","Sittakanay","Pukeashun","Morton","Thunder","Devils-Paw","Perseus","Overseer","Farquhar","Talchako","Whiting","Faisal","The-Pinnacles","Thomlinson","Lehua","Lester-Jones","Jeanette","Sharktooth","Upper-Saddle","Judge-Howay","Pattullo","Tatlow","Hudson-Bay","Corsan","Basement","Monmouth","Ovington","Addenbroke","Estero","Seton","Kaza","Cronin","Rugged","Kispiox","Sylvia","Crysdale","Vile","Wotzke","Hkusam","Whitecap","Dunn","Ida","Monkley","Horn","Tod","Gataga","Joffre","Robertson","Van-der-Est","Ambition","Clemenceau","Kitlope"]

@app.route("/")
def index():
    """Return a random word from the list"""
    return random.choice(wordlist)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
